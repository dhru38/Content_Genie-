import os
import asyncio
from google import genai
from Reddit_API import get_link
from Reddit_API import get_title
from Reddit_API import get_post
from TextToSpeech import main
from Video_Editing import create_video
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow


client = genai.Client(api_key="")
CLIENT_SECRETS_FILE = "client_secret.json"  
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

post = get_post()
title =  get_title()
link = get_link()



tags = f"Generate 10–15 short, relevant, and catchy YouTube tags for this video title: {title}. Return only the tags, with hashtags, separated by spaces, no explanations, no numbering."

description = f"Write a short, catchy, and simple YouTube video description for this title: {title}. Make it engaging and easy to read, under 2-3 sentences. give only one without anything no explanations , numberings etc just plain and simple description according to the title "



des_response =  client.models.generate_content(
    model="gemini-2.5-flash", contents= description
)

tags_response = client.models.generate_content(
    model="gemini-2.5-flash", contents= tags
)


file_path = "C:\\Users\\varsh\\OneDrive\\Desktop\\Hub\\Content Creator\\final_video.mp4"
vid_title = title
vid_description = f"Link : {link} \n {des_response.text}"
vid_tags = tags_response.text
privacy_status = "public"  # Can be "public", "unlisted", "private"
category_id = "27"  # Education. See YouTube categories for more

# # -----------------------------
# # 2️⃣ Authenticate & Build Client
# -----------------------------
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server(port=0)

youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)


def run_all ():
    main()
    create_video()

if __name__ == "__main__":
    run_all()
# -----------------------------
# 3️⃣ Upload Video
# -----------------------------
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": vid_title,
            "description": vid_description,
            "tags": vid_tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    },
    media_body=MediaFileUpload(file_path)
)

response = request.execute()
print("Upload Successful! Video ID:", response["id"])
print("Watch at: https://youtu.be/" + response["id"])

if os.path.exists(file_path):
    os.remove(file_path)
    print("Removed File ")
