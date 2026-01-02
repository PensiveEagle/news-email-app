# ---------- Import packages ---------- #
import requests
import os
from dotenv import load_dotenv
from email_functions import send_email

# ---------- Import environment variables ---------- #
load_dotenv()
api_key = os.getenv( "API_KEY" )
email_sender_pass = os.getenv( "GOOGLE_APP_PASSWORD" )

# ---------- Make API request ---------- #
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-12-02&sortBy=publishedAt&apiKey={api_key}"

response = requests.get( url )
content = response.json()

# ---------- Generate Email Message ---------- #
email_message = "Hello testing 123"

# ---------- Setup mailing list ---------- #
mailing_list = ["pensiveeagle.dev@gmail.com"]

# ---------- Send email ---------- #
for receiver in mailing_list:
    send_email( message = email_message, sender_addr = "pensiveeagle.dev@gmail.com", sender_pass = email_sender_pass, receiver_addr = receiver)