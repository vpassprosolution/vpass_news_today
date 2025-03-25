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

    # Current day
    today_str = datetime.utcnow().strftime("%Y-%m-%d")

    # Find all rows in calendar
    rows = soup.select("tr.js-event-item")

    news_items = []

    for row in rows:
        date_attr = row.get("data-event-datetime", "")
        if not today_str in date_attr:
            continue

        # Extract impact (3 bulls = high impact)
        impact = row.select_one(".importance span.grayFullBullishIcon")
        if not impact or len(row.select(".grayFullBullishIcon")) < 3:
            continue  # not high-impact (must be 3 bulls)

        # Extract time, currency, event title
        time = row.select_one(".time").get_text(strip=True)
        currency = row.select_one(".flagCur").get_text(strip=True)
        title = row.select_one(".event").get_text(strip=True)

        news_items.append(f"⏰ {time} | {currency} | 🔴 {title}")

    if not news_items:
        return "Today doesn't have any high-impact news."

    today_header = f"📅 HIGH-IMPACT NEWS – {datetime.utcnow().strftime('%A, %B %d')}\n\n"
    return today_header + "\n".join(news_items)
