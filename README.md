# News Aggregator

A full-stack news aggregation application built with React (TypeScript) and Django (Python).

## Features

- 10 keyword-based news sections (Technology, Business, Politics, etc.)
- Automatic hourly news updates
- Clean, responsive UI
- REST API backend
- Real-time news fetching from NewsAPI

## Tech Stack

**Frontend:**
- React with TypeScript
- Responsive CSS

**Backend:**
- Django 4.2
- Django REST Framework
- APScheduler for hourly updates
- SQLite database

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   ./venv/Scripts/pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   ./venv/Scripts/python manage.py migrate
   ```

4. Create 10 default keywords:
   ```bash
   ./venv/Scripts/python create_keywords.py
   ```

5. Create superuser for admin access:
   ```bash
   ./venv/Scripts/python manage.py createsuperuser
   ```

6. Start Django server:
   ```bash
   ./venv/Scripts/python manage.py runserver 8000
   ```

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start React development server:
   ```bash
   npm start
   ```

## URLs

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Django Admin: http://localhost:8000/admin/

## API Endpoints

- `GET /api/keywords/` - List all keywords with articles
- `POST /api/keywords/refresh_news/` - Manually refresh all news
- `GET /api/articles/` - List all articles
- `GET /api/articles/?keyword=<id>` - Filter articles by keyword

## Configuration

### News API Key

The application uses NewsAPI.org (free tier). To use your own API key:

1. Sign up at https://newsapi.org
2. Update `news_fetcher.py` with your API key:
   ```python
   self.api_key = 'YOUR_API_KEY_HERE'
   ```

### Keywords

Default 10 keywords can be modified via Django admin panel or by editing `create_keywords.py`.

## How It Works

1. Backend stores 10 keywords representing news categories
2. APScheduler runs hourly to fetch latest news for each keyword
3. News articles are stored in SQLite database
4. React frontend fetches and displays articles organized by sections
5. Users can manually refresh news using the UI button

## License

MIT
