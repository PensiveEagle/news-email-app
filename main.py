import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv( "API_KEY" )

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-12-02&sortBy=publishedAt&apiKey={api_key}"

response = requests.get( url )
content = response.json()

for article in content["articles"]:
    print( article["title"] )