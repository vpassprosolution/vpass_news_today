from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get_today_news")
def get_today_news():
    # Temporary placeholder for testing
    return JSONResponse(content={
        "status": "success",
        "message": "VESSA PRO News API is working ✅",
        "image_url": None,
        "news_text": None
    })
