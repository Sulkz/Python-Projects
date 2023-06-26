import requests
import json

api_key = 'Y'  # Replace with your actual API key

url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/rugby?unitGroup=metric&key={api_key}&contentType=json'
response = requests.get(url)

print(response.status_code)
print(response.json())
