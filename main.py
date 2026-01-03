# ---------- Import packages ---------- #
import requests
import os
from dotenv import load_dotenv
from email_functions import send_email

# ---------- Import environment variables ---------- #
load_dotenv()
api_key = os.getenv( "API_KEY" )
email_sender_pass = os.getenv( "GOOGLE_APP_PASSWORD" )

# ---------- Set API query parameters ---------- #
language = "en"
articles = 20

# ---------- Make API request ---------- #
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-12-02&sortBy=publishedAt&language={language}&pageSize={articles}&apiKey={api_key}"

response = requests.get( url )
content = response.json()

# ---------- Generate Email Message ---------- #
email_message = "Subject: Today's News \n"

for article in content["articles"]:
    if article["title"] is None or article["title"] == "":
        continue
    if article["description"] is None or article["description"] == "":
        continue
    email_message = email_message + f"{article["title"]}:\n{article["description"]} - {article["url"]}\n\n"
    
email_message = email_message.encode("utf-8")

# ---------- Setup mailing list ---------- #
mailing_list = ["<recipient-email-1>", "<recipient-email-2>"]

# ---------- Send email ---------- #
for receiver in mailing_list:
    send_email( message = email_message, sender_addr = "<sender-email>", sender_pass = email_sender_pass, receiver_addr = receiver)