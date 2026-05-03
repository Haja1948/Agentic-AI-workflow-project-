import os
from dotenv import load_dotenv

load_dotenv()

# RSS Feeds for AI News (Targeting sectors recommended in the assignment)
RSS_FEEDS = [
    # General Aviation/Logistics AI
    "https://news.google.com/rss/search?q=artificial+intelligence+aviation+logistics&hl=en-US&gl=US&ceid=US:en",
    
    # Venture Capital (Y Combinator, a16z, Sequoia)
    "https://a16z.com/feed/",
    "https://news.google.com/rss/search?q=%22Y+Combinator%22+AI+insights&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22Sequoia+Capital%22+AI+reports&hl=en-US&gl=US&ceid=US:en",
    
    # Investment Banks (Goldman Sachs, JPMorgan, Morgan Stanley)
    "https://news.google.com/rss/search?q=%22Goldman+Sachs%22+AI+research&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22JPMorgan%22+AI+insights&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22Morgan+Stanley%22+AI+investment&hl=en-US&gl=US&ceid=US:en",
    
    # Consulting (McKinsey, BCG, Bain)
    "https://www.mckinsey.com/Insights/rss.aspx",
    "https://news.google.com/rss/search?q=%22BCG%22+AI+thought+leadership&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22Bain%22+AI+innovation&hl=en-US&gl=US&ceid=US:en",
    
    # Business Schools & Academic (HBR, MIT, Stanford)
    "https://news.google.com/rss/search?q=%22Harvard+Business+Review%22+AI&hl=en-US&gl=US&ceid=US:en",
    "https://feeds.feedburner.com/MITTechnologyReviewAI",
    "https://news.google.com/rss/search?q=%22Stanford%22+AI+human-centered&hl=en-US&gl=US&ceid=US:en",
    
    # Tech Giants (Google, Microsoft, OpenAI)
    "https://openai.com/news/rss.xml",
    "https://news.google.com/rss/search?q=%22Google+AI%22+blog&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22Microsoft%22+AI+breakthrough&hl=en-US&gl=US&ceid=US:en"
]

# Database configuration
DB_PATH = "news_vault.db"

# Domain Configuration
DOMAIN_CONFIG = {
    "role": "Strategy Consultant",
    "industry": "Aviation, Logistics, and Supply Chain Management",
    "target_audience": "Airline executives, Logistics and supply chain managers, Strategy Consultants",
    "relevance_criteria": [
        "Strategic impact on airline operations",
        "Operational efficiency in logistics",
        "Competitive advantage in supply chain management",
        "Revenue or cost implications for transport industries",
        "Regulatory or governance considerations in aviation"
    ]
}

# Classification Categories
CATEGORIES = [
    "Strategy and Executive Decision-Making",
    "Product and Service Innovation",
    "Infrastructure, Models, and Platforms",
    "Governance, Ethics, and Regulation",
    "Industry-Specific AI Use Cases (Aviation/Logistics)"
]

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
