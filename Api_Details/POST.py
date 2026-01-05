import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload= {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=payload)

print("status_code:", response.status_code)

data = response.json()
print("data:", data)    