import requests

link = "https://jsonplaceholder.typicode.com/posts"
id = input("Digite um id")
titulo  = input("Digite um titulo")
body = input("body")

r = requests.put(f"{link}/1", json={"id": id, "title": titulo, "body": body})

print(r.status_code, r.json())

titulo_2 = input("Digite novo titulo")
r = requests.patch(f"{link}/1", json={"title": titulo_2})

print(r.status_code, r.json())

r = requests.delete(f"{link}/1")
print(r.status_code, r.json())