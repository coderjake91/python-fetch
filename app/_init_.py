import requests

#make a test GET request to GitHub's Root REST API (source: https://realpython.com/python-requests/#getting-started-with-requests)
response = requests.get('https://api.github.com')

#print requests status 
print(f'The response status code is {response.status_code}')

if response:
    print('Request Successful!')
else:
    print('An error has occurred.')