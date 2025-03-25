from database import save_today_news

# 🔥 Sample hardcoded news text
news_text = """
📊 TODAY’S MARKET MOVERS

- 8:30am USD Core Retail Sales (Expected: 0.2%)
- 10:00am USD Fed Interest Rate Decision
- 11:30am GBP BoE Gov Bailey Speaks

Volatility expected on USD, GBP.
"""

# Call save function
save_today_news("today_news_final.png", news_text)
