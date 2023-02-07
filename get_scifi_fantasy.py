import requests 
# getting connection error 
resp = requests.get('https://www.foliosociety.com/ca/fiction/sci-fi-fantasy')
print(resp.status_code)
#print(resp.text)
