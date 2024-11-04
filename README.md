# Video Downloader API

This project provides a RESTful API for downloading videos from various sources. It uses FastAPI to create endpoints and `yt-dlp` for downloading video content. The API accepts a URL, downloads the video in the best available format, and returns the file for the user to download.
![Screenshot 2024-11-04 201717](https://github.com/user-attachments/assets/5069b2d2-ea2e-4999-b1eb-3d2264701d38)

## Features

- **Download Videos**: Provide a URL to download the highest quality version of the video.
- **Filename Sanitization**: Ensures filenames are safe for the filesystem.
- **Simple REST API**: Easy integration with other applications.

## Requirements

- Python 3.8+
- `FastAPI`
- `yt-dlp`

Install the necessary libraries using:

```bash
pip install -r requirements.txt
```

## Endpoints

### GET /download/

Download a video by providing its URL.

**Parameters:**
- `url`: The URL of the video to download.

**Example:**
```http
GET /download/?url=https://example.com/video-url
```

**Response:**
Returns the video file for download.

## Directory Structure

- `main.py`: Main script containing the API logic.
- `downloads/`: Directory where downloaded videos are saved.

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Security

This project does not include authentication. For production use, consider adding authentication and rate limiting.
