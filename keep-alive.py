import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

def make_get_request(url):
    try:
        response = requests.get(url)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            pass
    except Exception as e:
        print(f"An error occurred: {e}")

url = os.getenv('ALIVE_URL')

if url:
    while True:
        make_get_request(url)
        time.sleep(180)
else:
    print("ALIVE_URL environment variable is not set or .env file is missing.")
