import hashlib
import requests
import time
import bs4
import os
import json
import wget
import urllib.error as ue
import urllib.request
# Keys required to call Slideshare API's

api_key = '++++++++++'

shared_secret = '+++++++++'


# Strings to find and download data

con=['resume' , 'senior' , 'engineer', 'hadoop developer', 'cv', 'java developer', 'python developer','business analyst','project manager', 'qa' , 'data scientist' , 'scrum master', 'full stack developer' ]

#Strings to neglect data

notcon= ['training' , 'webinar','exam','why' , 'how' ,'meetup', 'books' , 'online' , 'ebook','ebooks' ,'books', 'tips', 'top','[download]','[recommendation]','hire' , 'opportunity','day' ,'help' , 'lessons', 'read', 'learning','company' , 'download','what','tools' , 'guide', 'things' , 'without' , 'vs.' , 'description' , 'journey', 'content', 'contents' , 'jobs', 'job','toolbox','view', 'bundle' , 'set', 'skill' , 'session']


# To change directory for downloading for diffrent JD's

def changepath(path):
  os.chdir('/home/shubhi/Data4model/'+path)

# Request using Slideshare API to get results according to query string

def getcontent(query, page_no,q1):
   hash1 = hashlib.sha1()
   hash1.update(shared_secret.encode('utf-8'))
   hash1.update(str(round(time.time())).encode('utf-8'))
   payload = {'api_key': api_key, 'ts': round(time.time()), 'hash':  hash1.hexdigest(),'detailed':1 ,'page':page_no,'q': query +q1}
   r = requests.get('https://www.slideshare.net/api/2/search_slideshows', params=payload)
   soup = bs4.BeautifulSoup(r.text , 'lxml' )
   print(soup.find('numresults'))
   return soup.find_all('slideshow')


# Create sets of downloadurrl and title of Slideshows

def createsets(lis, set1, set2):
   result = True
   for i in lis:
       if i.downloadurl:
          for j in con:
              if j in i.title.get_text().lower().replace('_'," "):
                 for k in notcon:
                   if k not in i.title.get_text().lower().replace('_'," "):
                      continue
                   else:
                      result=False
                 if(result):      
                  #set1.add(i.downloadurl.get_text())#.split('?')[0])
                  if(i.title.get_text() not in set2):
                   set2.add(i.title.get_text())
                   set1.add(i.downloadurl.get_text())#split('?')[0])
                 result=True
                 break

# Printing the sets

def printsets1(set1):
  for l in set1:
    print(l+'\n')
  print(len(set1))
def printsets2(set2):
  for l in set2:
    print(l+'\n')
  print(len(set2))


# Downloading the PDF's

def downloadpdfs(set1):
     k=0
     set4=set(set1)
     for i in set1:
      j=i.split('?')[0]
     # urllib.request.urlretrieve(i,j.split('/')[-1])
    # for i in set1:
      response = requests.get(j)
     # if(len(response.content)>10240):
      #     try:
       #      wget.download(str(i))
             
        #   except :
         #         i=i.split('?')[0]
          #        with open(i.split('/')[-1],'wb') as f:
           #              f.write(response.content)
           #except:
            #    print('error for link' , i.split('?')[0])
           #finally:
            # k=k+1
     #print('  ',k ,'Links were valid ')        
      if(len(response.content) >10240):
       with open(i.split('?')[0].split('/')[-1],'wb') as f:
         k=k+1
         f.write(response.content)
         set4.remove(i)
     print(k ,'Links were valid ') 
     return set4

def downloadpdfs1(set1):
  k=0
  set3=set()
  for i in set1:
      j=i.split('?')[0]
      try:
       response = urllib.request.urlretrieve(i,j.split('/')[-1])
      except:
          continue




#______________________main__________________________________________



with open('Jdfile.json', 'r+') as f:
   data = json.load(f)
   for i in data:
    set1=set()
    set2=set()
    changepath(i['JD']) 

    for b in range(1,i['num_of_pages']+1):
     for c in i['key_word']:
      lis = getcontent( i['JD'], b,c)
     
      createsets(lis,set1,set2)
   
    printsets1(set1)
    for i in range(2):
     if(i<1):
      set1=set(downloadpdfs(set1))
      printsets1(set1)
     else:
       (downloadpdfs1(set1))
     




