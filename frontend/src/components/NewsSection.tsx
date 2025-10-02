import React from 'react';
import { Keyword } from '../types';
import './NewsSection.css';

interface NewsSectionProps {
  keyword: Keyword;
}

const NewsSection: React.FC<NewsSectionProps> = ({ keyword }) => {
  return (
    <div className="news-section">
      <h2 className="section-header">
        <span className="section-number">{keyword.section_number}.</span> {keyword.name}
        <span className="article-count">({keyword.article_count} articles)</span>
      </h2>
      <div className="articles-grid">
        {keyword.articles.slice(0, 5).map((article) => (
          <div key={article.id} className="article-card">
            {article.image_url && (
              <img src={article.image_url} alt={article.title} className="article-image" />
            )}
            <div className="article-content">
              <h3 className="article-title">
                <a href={article.url} target="_blank" rel="noopener noreferrer">
                  {article.title}
                </a>
              </h3>
              {article.description && (
                <p className="article-description">{article.description}</p>
              )}
              <div className="article-meta">
                {article.source && <span className="article-source">{article.source}</span>}
                {article.published_at && (
                  <span className="article-date">
                    {new Date(article.published_at).toLocaleDateString()}
                  </span>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NewsSection;
