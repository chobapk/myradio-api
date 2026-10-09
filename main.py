
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from urllib.parse import urlparse

app = FastAPI(title="MyRadio API")


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "MyRadio API"
    }


@app.get("/stream")
def get_stream():
    stream_url = os.getenv("AUDIO_STREAM_URL", "").strip()

    if not stream_url:
        raise HTTPException(
            status_code=503,
            detail="AUDIO_STREAM_URL is not configured"
        )

    parsed = urlparse(stream_url)

    if parsed.scheme != "https" or not parsed.netloc:
        raise HTTPException(
            status_code=500,
            detail="AUDIO_STREAM_URL must be a valid HTTPS URL"
        )

    return JSONResponse({
        "status": "success",
        "streamUrl": stream_url
    })
