from fastapi import FastAPI, HTTPException
import yt_dlp
from fastapi.responses import FileResponse
import os
import re

app = FastAPI()

download_d = "./downloads"



def sanitize_filename(filename: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '', filename)

@app.get("/download/")
async def download(url: str):
    print(f"Attempting to download from URL: {url}")  # Debugging line
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_d, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            fp = os.path.join(download_d, f"{info_dict['title']}.mp4")
            sanitized_title = sanitize_filename(info_dict['title'])
            fp = os.path.join(download_d, f"{sanitized_title}.mp4")
        
        if not os.path.exists(fp):
            raise HTTPException(status_code=404, detail="File does not exist.")
        
        return FileResponse(fp)
    except Exception as e:
        print(f"Error occurred: {str(e)}")  
        raise HTTPException(status_code=400, detail=f"failed to download!! {str(e)}")
