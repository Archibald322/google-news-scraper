"""
Google News Scraper - Client Showcase & API Runner
Runs the high-speed Google News Actor remotely on the Apify cloud platform.
"""

import os
import sys
from dotenv import load_dotenv
from apify_client import ApifyClient

# 1. Load APIFY_TOKEN from environment
load_dotenv()
token = os.getenv("APIFY_TOKEN")
if not token:
    print("[ERROR] APIFY_TOKEN is not set.")
    print("Please get your API token from https://console.apify.com/account#/integrations and set it in your .env file:")
    print("APIFY_TOKEN=your_apify_token_here")
    sys.exit(1)

client = ApifyClient(token)

# 2. Configure parameters
run_input = {
    "search": "artificial intelligence",
    "topic": "NONE",
    "timeRange": "1d",
    "language": "en-US",
    "country": "US",
    "maxItems": 10,
}

print("=" * 60)
print("🚀 Launching Google News Scraper on Apify Cloud...")
print(f"📊 Parameters: {run_input}")
print("=" * 60)

try:
    # 3. Call Actor on Apify platform
    run = client.actor("archibald322/google-news-scraper").call(run_input=run_input)
    status = run.get("status") if isinstance(run, dict) else getattr(run, "status", "UNKNOWN")
    dataset_id = run.get("defaultDatasetId") if isinstance(run, dict) else getattr(run, "default_dataset_id", "")

    print(f"\n✅ Execution Finished! Status: {status}")
    print(f"📦 Dataset ID: {dataset_id}")

    # 4. Fetch and display results
    dataset_items = client.dataset(dataset_id).list_items().items
    print(f"🎯 Total articles extracted: {len(dataset_items)}\n")

    for i, item in enumerate(dataset_items[:5], 1):
        title = item.get("title", "Unknown")
        source = item.get("source", "")
        pub = item.get("publishedAt", "")
        link = item.get("link", "")
        print(f"  [{i}] {title}")
        print(f"      Publisher: {source} | Published: {pub}")
        print(f"      🔗 {link}")

    print("\n👉 Export full data (JSON/CSV/Excel) from your Apify Console:")
    print(f"   https://console.apify.com/storage/datasets/{dataset_id}")

except Exception as e:
    print(f"\n[ERROR] Failed to run Actor: {e}")
    sys.exit(1)
