from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import yt_dlp

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/download")
def download(url: str):

    ydl_opts = {"format": "best"}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info["url"]

    return RedirectResponse(video_url)
