import sqlite3
from openai import OpenAI
from src.config import DB_PATH, CATEGORIES, OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
)

def get_relevant_unclassified_articles():
    """Fetches articles that are relevant but not yet classified."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, summary FROM articles WHERE is_relevant = 1 AND category IS NULL")
    articles = cursor.fetchall()
    conn.close()
    return articles

def classify_article(title, summary):
    """Uses LLM to classify article into business categories."""
    categories_str = "\n".join([f"- {c}" for c in CATEGORIES])
    prompt = f"""
    You are an expert AI Content Classifier for a Strategy Consultant.
    Classify the following article into ONE of these categories:
    {categories_str}
    
    Article Title: {title}
    Article Summary: {summary}
    
    Return ONLY the category name.
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0
        )
        content = response.choices[0].message.content
        if content is None:
            print(f"Debug: Response content is None. Response object: {response}")
            return None
        result = content.strip()
        print(f"  Debug: Model returned: {result}")
        # Robust validation: check for key terms in the response
        lower_result = result.lower()
        for category in CATEGORIES:
            # Check if the full category name is in the result
            if category.lower() in lower_result:
                return category
            
            # Check for significant keywords from each category
            keywords = {
                "Strategy and Executive Decision-Making": ["strategy", "executive", "decision-making"],
                "Product and Service Innovation": ["product", "service", "innovation"],
                "Infrastructure, Models, and Platforms": ["infrastructure", "models", "platforms"],
                "Governance, Ethics, and Regulation": ["governance", "ethics", "regulation"],
                "Industry-Specific AI Use Cases (Aviation/Logistics)": ["industry-specific", "aviation", "logistics"]
            }
            
            category_keys = keywords.get(category, [])
            if any(key in lower_result for key in category_keys):
                # If we have at least 2 matching keywords, consider it a match
                match_count = sum(1 for key in category_keys if key in lower_result)
                if match_count >= 2 or (match_count >= 1 and len(category_keys) == 1):
                     return category

        return "Other"
    except Exception as e:
        print(f"Error classifying article: {e}")
        return None

def run_classification():
    """Processes relevant articles and updates their category."""
    articles = get_relevant_unclassified_articles()
    if not articles:
        print("No relevant unclassified articles found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    classified_count = 0
    for art_id, title, summary in articles:
        print(f"Classifying: {title[:50]}...")
        category = classify_article(title, summary)
        if category:
            cursor.execute("UPDATE articles SET category = ? WHERE id = ?", (category, art_id))
            classified_count += 1
            print(f"  -> {category}")
            
    conn.commit()
    conn.close()
    print(f"Classification Complete: {classified_count} articles categorized.")

if __name__ == "__main__":
    run_classification()
