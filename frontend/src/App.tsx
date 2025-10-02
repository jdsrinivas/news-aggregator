import React, { useState, useEffect } from 'react';
import NewsSection from './components/NewsSection';
import { Keyword } from './types';
import './App.css';

const API_BASE_URL = window.location.hostname === 'localhost'
  ? 'http://localhost:8000/api'
  : 'https://notify-saved-asn-closing.trycloudflare.com/api';

function App() {
  const [keywords, setKeywords] = useState<Keyword[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const fetchKeywords = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/keywords/`);
      if (!response.ok) throw new Error('Failed to fetch keywords');
      const data = await response.json();
      // Handle paginated response from DRF
      const keywordsData = data.results || data;
      setKeywords(keywordsData);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const refreshNews = async () => {
    setRefreshing(true);
    try {
      const response = await fetch(`${API_BASE_URL}/keywords/refresh_news/`, {
        method: 'POST',
      });
      if (!response.ok) throw new Error('Failed to refresh news');
      await fetchKeywords();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to refresh news');
    } finally {
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchKeywords();
    // Auto-refresh every 5 minutes
    const interval = setInterval(fetchKeywords, 5 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="app">
        <div className="loading">Loading news...</div>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>News Aggregator</h1>
        <button 
          onClick={refreshNews} 
          disabled={refreshing}
          className="refresh-button"
        >
          {refreshing ? 'Refreshing...' : 'Refresh All News'}
        </button>
      </header>
      
      {error && <div className="error">{error}</div>}
      
      <main className="app-content">
        {keywords.length === 0 ? (
          <div className="no-keywords">
            No keywords configured. Please add keywords via the Django admin panel.
          </div>
        ) : (
          keywords.map((keyword) => (
            <NewsSection key={keyword.id} keyword={keyword} />
          ))
        )}
      </main>
    </div>
  );
}

export default App;
