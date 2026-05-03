import sqlite3
from openai import OpenAI
from src.config import DB_PATH, DOMAIN_CONFIG, OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
)

def get_unprocessed_articles():
    """Fetches articles that haven't been routed yet."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # We use is_relevant = 0 as default, but we need a way to know if it's been processed.
    # Let's add a 'processed' column or just check if is_relevant is still the default.
    # To be safe, let's assume if category is NULL, it hasn't been fully processed.
    # Actually, let's just add a 'status' column to the DB.
    # For now, I'll just fetch a few for testing.
    cursor.execute("SELECT id, title, summary FROM articles WHERE is_relevant = 0 LIMIT 10")
    articles = cursor.fetchall()
    conn.close()
    return articles

def evaluate_relevance(title, summary):
    """Uses LLM to evaluate article relevance."""
    prompt = f"""
    You are an expert AI Relevance Router for a {DOMAIN_CONFIG['role']} in the {DOMAIN_CONFIG['industry']} industry.
    Your target audience is {DOMAIN_CONFIG['target_audience']}.
    
    Evaluate the following news article for relevance based on these criteria:
    {chr(10).join(['- ' + c for c in DOMAIN_CONFIG['relevance_criteria']])}
    
    Article Title: {title}
    Article Summary: {summary}
    
    Return ONLY 'YES' if the article is relevant and 'NO' if it is not.
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
            temperature=0
        )
        content = response.choices[0].message.content
        if content is None:
            return 0
        result = content.strip().upper()
        return 1 if "YES" in result else -1 # -1 for irrelevant
    except Exception as e:
        print(f"Error evaluating article: {e}")
        return 0

def route_articles():
    """Processes unprocessed articles and updates their relevance status."""
    articles = get_unprocessed_articles()
    if not articles:
        print("No new articles to process.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    relevant_count = 0
    for art_id, title, summary in articles:
        print(f"Routing: {title[:50]}...")
        relevance = evaluate_relevance(title, summary)
        cursor.execute("UPDATE articles SET is_relevant = ? WHERE id = ?", (relevance, art_id))
        if relevance == 1:
            relevant_count += 1
            print("  -> RELEVANT")
        else:
            print("  -> NOT RELEVANT")
            
    conn.commit()
    conn.close()
    print(f"Routing Complete: {relevant_count} relevant articles found out of {len(articles)} processed.")

if __name__ == "__main__":
    route_articles()
