import requests
url = 'https://jsonplaceholder.typicode.com/posts'
obj = {'title':'Special Agent', 'body':'Leroy Jethro Gibbs', 'userId':'1'}
response = requests.post(url, data = obj)
print(response.status_code)
print(response.json())