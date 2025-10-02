export interface NewsArticle {
  id: number;
  title: string;
  description: string | null;
  url: string;
  source: string | null;
  published_at: string | null;
  image_url: string | null;
  fetched_at: string;
}

export interface Keyword {
  id: number;
  name: string;
  section_number: number;
  created_at: string;
  articles: NewsArticle[];
  article_count: number;
}
