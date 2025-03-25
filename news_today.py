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

from generate_today_news import generate_today_news

@app.get("/generate_today_news")
def run_full_news_generator():
    generate_today_news()
    return {"status": "success", "message": "Today’s news image + text generated and saved ✅"}


