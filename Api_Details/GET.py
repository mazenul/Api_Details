import requests

url_1 = "https://jsonplaceholder.typicode.com/posts/1"
url_2 = "https://reqres.in/api/users"

params = {
    "page": 2
}

response_1 = requests.get(url_1)
response_2 = requests.get(url_2, params=params)




# for response 1
print("status_code:", response_1.status_code)
print("Contact:",response_1.headers.get("Content-Type"))
data = response_1.json()
print("data:", data)
print(data['title'])
print(data['body'])


# for response 2
response_2.raise_for_status()
print("status_code:", response_2.status_code)
print("final url:", response_2.url)

for value in data.values():
    print(value)