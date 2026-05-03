from src.monitor import fetch_news
from src.router import route_articles
from src.classifier import run_classification
from src.generator import run_generation

def main():
    print("=== Phase 1: Monitoring ===")
    fetch_news()
    
    print("\n=== Phase 2: Relevance Routing ===")
    route_articles()
    
    print("\n=== Phase 3: Information Classification ===")
    run_classification()
    
    print("\n=== Phase 4 & 5: Content Generation ===")
    run_generation()
    
    print("\n=== Pipeline Complete ===")

if __name__ == "__main__":
    main()
