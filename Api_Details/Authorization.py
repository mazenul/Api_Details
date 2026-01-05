import requests 
Token = "my_secret_token"

headers ={
    "Authorization": f"Bearer {Token}" # this is an authorization token     
}

url = "you_url_here"

try:
    response =  requests.get(url, headers= headers, timeout= 10)
    response. raise_for_status()
    print("Status_code:", response.status_code)
    print("url:", response.url)

    try:
        data = response.json()
        print("data:", data)
    except ValueError:
        print("Response is not in JSON format")

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("request failed:",e)

