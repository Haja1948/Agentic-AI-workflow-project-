import feedparser
import sqlite3
import datetime
from src.config import RSS_FEEDS, DB_PATH

def init_db():
    """Initializes the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT UNIQUE NOT NULL,
            summary TEXT,
            published_date TEXT,
            source TEXT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_relevant INTEGER DEFAULT 0,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_news():
    """Fetches news from RSS feeds and stores unique items in the database."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    new_articles_count = 0
    
    for url in RSS_FEEDS:
        print(f"Fetching from: {url}")
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            title = entry.get('title', 'No Title')
            link = entry.get('link', '')
            summary = entry.get('summary', '')
            published = entry.get('published', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            source = feed.feed.get('title', url)
            
            try:
                cursor.execute('''
                    INSERT INTO articles (title, link, summary, published_date, source)
                    VALUES (?, ?, ?, ?, ?)
                ''', (title, link, summary, published, source))
                new_articles_count += 1
            except sqlite3.IntegrityError:
                # Link already exists
                continue
    
    conn.commit()
    conn.close()
    print(f"Task Complete: Fetched {new_articles_count} new articles.")

if __name__ == "__main__":
    fetch_news()
