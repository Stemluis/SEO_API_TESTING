import requests
url = 'http://movie-quote-api.herokuapp.com/v1/quote/'
response = requests.post(url)
print(response.json())