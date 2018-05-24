import hashlib
import requests
import time
api_key = '#########'
shared_secret = '#######'

  
hash1 = hashlib.sha1()
hash1.update(shared_secret.encode('utf-8'))
hash1.update(str(round(time.time())).encode('utf-8'))
payload = {'api_key': api_key, 'ts': round(time.time()), 'hash': hash1.hexdigest(), 'username_for': 'ChetanKhatri'}
r = requests.get('https://www.slideshare.net/api/2/get_slideshows_by_user', params=payload)
print(r.text)
# print(hash1.hexdigest() ,"", round(time.time()))
