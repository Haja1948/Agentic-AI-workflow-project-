import sqlite3
from openai import OpenAI
from src.config import DB_PATH, OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
)

def get_articles_for_generation():
    """Fetches articles from unique categories for generation."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Fetch one article from each unique category available
    cursor.execute("""
        SELECT category, title, summary 
        FROM (
            SELECT category, title, summary,
            ROW_NUMBER() OVER(PARTITION BY category ORDER BY fetched_at DESC) as rn
            FROM articles 
            WHERE category IS NOT NULL AND category != 'Other' AND is_relevant = 1
        ) t
        WHERE rn = 1
        LIMIT 3
    """)
    articles = cursor.fetchall()
    conn.close()
    return articles

def generate_linkedin_post(category, title, summary, guidelines):
    """Generates a LinkedIn post using the guidelines and article info."""
    prompt = f"""
    You are a Strategy Consultant in Aviation and Logistics. 
    Your goal is to write a high-impact LinkedIn post for Airline executives and Logistics managers.
    
    Use the following Reverse-Engineered KOL Guidelines:
    {guidelines}
    
    Article Context:
    - Category: {category}
    - Title: {title}
    - Summary: {summary}
    
    Requirements:
    - Translates AI developments into clear business implications.
    - Demonstrates depth of analysis and strategic thinking.
    - Concise, engaging, and professional.
    - Specify the Target Audience, Tone, and Positioning at the top.
    - Include a description for a suggested Visual/Image at the end.
    
    Generate the post:
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating post: {e}")
        return None

def run_generation():
    """Main generation loop."""
    # Read guidelines
    try:
        with open("src/guidelines.md", "r") as f:
            guidelines = f.read()
    except FileNotFoundError:
        print("Guidelines file not found. Please run Phase 4 research first.")
        return

    articles = get_articles_for_generation()
    if not articles:
        print("No classified articles found for generation.")
        return

    posts = []
    for category, title, summary in articles:
        print(f"Generating post for: {title[:50]}...")
        post = generate_linkedin_post(category, title, summary, guidelines)
        if post:
            posts.append(post)
    
    # Save to a file
    with open("final_linkedin_content.md", "w", encoding='utf-8') as f:
        f.write("# Final LinkedIn Content Design Samples\n\n")
        for i, post in enumerate(posts):
            f.write(f"## Post Sample {i+1}\n")
            f.write(post)
            f.write("\n\n---\n\n")
    
    print(f"Generation Complete: {len(posts)} posts saved to final_linkedin_content.md")

if __name__ == "__main__":
    run_generation()
