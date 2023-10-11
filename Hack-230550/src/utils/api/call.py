import os
import requests
from uagents import Context, Model

class Call():
    def __init__(self,url):
        self.url=url
    def getdata(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            ctx:Context.logger.info(f"Error fetching weather data: {e}")
            return None

def call(city):
    base_url = os.getenv("BASE_URL").rstrip("\r\n")
    api_key = os.getenv("API_KEY")
    point = f"{base_url}appid={api_key}&q={city}"
    return Call(point)
    