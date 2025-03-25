from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from database import load_today_news
import init_db

app = FastAPI()

# ✅ Create table on startup
@app.on_event("startup")
def startup_event():
    init_db.create_table()

# ✅ MAIN ENDPOINT
@app.get("/get_today_news")
def get_today_news():
    image_data, news_text = load_today_news()

    if image_data and news_text:
        return {
            "status": "success",
            "message": "News data loaded ✅",
            "image_base64": image_data.hex(),  # Will convert to image in bot
            "news_text": news_text
        }
    else:
        return JSONResponse(content={
            "status": "error",
            "message": "No news found in database."
        })

from database import save_today_news

@app.get("/save_sample_news")
def save_sample():
    news_text = """
    📊 TODAY’S MARKET MOVERS

    - 8:30am USD Core Retail Sales (Expected: 0.2%)
    - 10:00am USD Fed Interest Rate Decision
    - 11:30am GBP BoE Gov Bailey Speaks

    Volatility expected on USD, GBP.
    """
    save_today_news("today_news_final.png", news_text)
    return {"status": "success", "message": "Sample news saved to DB ✅"}
