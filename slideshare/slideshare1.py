import hashlib
import requests
import time
import bs4



api_key = '4otIvfgT'
shared_secret = 'hlSQjRtH'
hash1 = hashlib.sha1()
hash1.update(shared_secret.encode('utf-8'))
hash1.update(str(round(time.time())).encode('utf-8'))
payload = {'api_key': api_key, 'ts': round(time.time()), 'hash': hash1.hexdigest(), 'q': 'Hadoop developer resume pdf'} #'items_per_page' :35}
r = requests.get('https://www.slideshare.net/api/2/   search_slideshows', params=payload)
#soup = bs4.BeautifulSoup(r.text , 'html.parser' )
#lis =(soup.find_all('downloadurl'))
#lis1=[]
#for i in lis:
 # lis1.append(i[0].get_text())

#print(lis)
print(r.text)
