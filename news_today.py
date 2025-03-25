from fastapi import FastAPI
from fastapi.responses import JSONResponse
import init_db

app = FastAPI()

# 🧠 Auto-create the table at startup
init_db.create_table()

@app.get("/get_today_news")
def get_today_news():
    # Temporary placeholder for testing
    return JSONResponse(content={
        "status": "success",
        "message": "VESSA PRO News API is working ✅",
        "image_url": None,
        "news_text": None
    })
