import os
import time
from googleapiclient.errors import HttpError
from uploader_youtube.auth import get_authenticated_service

def upload_video(file_path, title, description, tags, thumbnail_path=None):
    youtube = get_authenticated_service()

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "23"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }

    try:
        print("Uploading video...")
        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=file_path
        )
        response = request.execute()
        print(f"Upload successful! Video ID: {response['id']}")

        if thumbnail_path:
            youtube.thumbnails().set(
                videoId=response['id'],
                media_body=thumbnail_path
            ).execute()
            print("Thumbnail uploaded!")

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")