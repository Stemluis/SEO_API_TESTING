import requests
userTxt = input()
myobj = {'text': userTxt}
url = "http://text-processing.com/api/sentiment/"
response = requests.post(url, data = myobj)
print(response.json())