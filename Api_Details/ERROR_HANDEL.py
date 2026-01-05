import requests

try:
    url= "https://httpbin.org/delay/3"
    response = requests.get(url, timeout= 30)
    response.raise_for_status()
    print("success:", response.json())

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("request failed:",e)