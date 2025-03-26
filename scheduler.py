from apscheduler.schedulers.background import BackgroundScheduler
from generate_today_news import generate_today_news
import time

scheduler = BackgroundScheduler()

# ✅ Clearly schedule to run EVERY 1 hour
scheduler.add_job(generate_today_news, 'interval', hours=1)

scheduler.start()
print("🚀 VESSA NEWS SCHEDULER CLEARLY RUNNING (every 1 hour)! 🚀")

try:
    while True:
        time.sleep(60)  # Keeps scheduler running clearly
except KeyboardInterrupt:
    scheduler.shutdown()
