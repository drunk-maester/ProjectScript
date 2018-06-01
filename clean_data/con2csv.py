import PyPDF2 as pd1
import os
from os import walk
import csv
import nltk
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string 
import re

def changepath(path):
  os.chdir('/home/shubhi/Data4model/'+path)
  print('Current Directory : ' , os.getcwd())


def pdfcontent(file1):
 with open(file1, 'rb') as f:
    a= pd1.PdfFileReader(f)
    b=a.numPages
    lis=[]
    for i in range(b):
       c=a.getPage(i)
       lis.append(c.extractText().encode('ascii', 'ignore'))
    lis=cleanpdf(lis)
    return lis
def cleanpdf(lis):
  stop= stopwords.words('english') + list(string.punctuation) +['etc', 'ect' , 'using' , 'across', "'re" , "'s",'engineering' ,'language' , 'english' , 'hindi' , 'odia', 'xii' ,'school' , 'cgpa' , 'college' , 'playing', 'meeting' , 'people' ,"\n"]
  str2=" "
  for j in lis:
    if(str2[-1]==" "):
      str2=str2+ j.decode('utf-8')
    else:
      str2=str2+" "+ j.decode('utf-8')
  
  str2=str2.lower()
  p= re.compile('[a-zA-Z]+')
  str1= p.findall(str2)
 # str1=word_tokenize(str2)
  str1fil = [x for x in str1 if x not in stop ]
 # p= re.compile('\w+')
  #a= p.findall()
  str1fil = " ".join(str1fil)
  return str1fil
   

dname=[]
for (dirpath , dirnames , filenames) in walk('/home/shubhi/Data4model/'):
        dname.extend(dirnames)
jd=[]
lis1=[]
for i in dname:
  changepath(i)
  lis=[]
  print(i)
  for  k in os.listdir("/home/shubhi/Data4model/"+i+"/"):
    a=pdfcontent(k)
    if(type(a)!=None):
        if(len(a)>30):
          lis.append(a)
  jd.append(i)
  lis1.append(lis)
  
print(jd)
print(lis1)  
 
