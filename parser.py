import httpx
from bs4 import BeautifulSoup
from datetime import datetime

def get_today_news_text():
    url = "https://www.investing.com/economic-calendar/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = httpx.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print("❌ Error fetching data:", e)
        return "Error loading news data."

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("tr.js-event-item")

    news_items = []

    for row in rows:
        # Check for 3 bull icons (high-impact)
        bulls = row.select(".grayFullBullishIcon")
        if len(bulls) < 3:
            continue

        # Extract time, currency, event
        time = row.select_one(".time")
        currency = row.select_one(".flagCur")
        event = row.select_one(".event")

        if not (time and currency and event):
            continue

        time_text = time.get_text(strip=True)
        currency_text = currency.get_text(strip=True)
        event_text = event.get_text(strip=True)

        news_items.append(f"⏰ {time_text} | {currency_text} | 🔴 {event_text}")

    if not news_items:
        return "Today doesn't have any high-impact news."

    today_header = f"📅 HIGH-IMPACT NEWS – {datetime.utcnow().strftime('%A, %B %d')}\n\n"
    return today_header + "\n".join(news_items)
