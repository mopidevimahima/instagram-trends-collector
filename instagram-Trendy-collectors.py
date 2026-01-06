import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Later.com Instagram Reels trends page [web:31]
TARGET_URL = "https://later.com/blog/instagram-reels-trends/"


def scrape_later_trends():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resp = requests.get(TARGET_URL, headers=headers)

    if resp.status_code != 200:
        print(f"Error: {resp.status_code}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find all <h3> tags that are likely trend/sound names
    trend_elements = soup.find_all("h3")

    results = []
    for elem in trend_elements:
        text = elem.get_text(strip=True)
        if len(text) > 5 and any(word in text.lower() for word in ["sound", "audio", "trend"]):
            results.append({
                "trend_name": text,
                "platform": "Instagram Reels",
                "source": TARGET_URL,
                "found_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return results


def save_results(results):
    if not results:
        print("No trends found.")
        return

    df = pd.DataFrame(results)

    # Save to CSV (append mode)
    try:
        existing = pd.read_csv("trends.csv")
        df = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv("trends.csv", index=False)
    print(f"Saved {len(results)} trends to trends.csv")


if __name__ == "__main__":
    trends = scrape_later_trends()
    print("Found trends:")
    for t in trends:
        print(f"- {t['trend_name']}")
    save_results(trends)
    print("Done! Check trends.csv")
