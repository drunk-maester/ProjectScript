from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os
from os import walk
import csv
import nltk
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string 
import re

def pdfcontent(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    parser = PDFParser(fp )
    document =PDFDocument(parser, "")
    if not document.is_extractable:
       print("Pdf's text is not extractable")
       return None
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    text = cleanpdf(word_tokenize(text))
    return text.decode('utf-8')

def cleanpdf(lis):
  stop= stopwords.words('english') + list(string.punctuation) +['etc', 'ect' , 'using' , 'across', "'re" , "'s",'engineering' ,'language' , 'english' , 'hindi' , 'odia', 'xii' ,'school' , 'cgpa' , 'college' , 'playing', 'meeting' , 'people' ,"\n",'com', 'hostel' , 'civil' , 'lines', 'email', 'sep', 'june', 'jun' , 'jul', 'till' , 'date','name', 'kumar', 'vijay' , 'visa', 'a' ,'e', 'x', 'z','g','mar','gmail','linkedin','like','september', 'february', 'university', 'gurgaon ', 'haryana','http' ,'street', 'gyanasurya', 'nayak' ,'plot', 'sgr' ,'rd' ,'th' ,' road' 'shantiniketan' ,'layout',' munnekolala', 'marathahalli' 'phone', 'e mail' ,'gyana', 'nk','shubham', 'goswami', 'address','seeking','alll', 'noida']
  str2=" "
  for j in lis:
    if(str2[-1]==" "):
      str2=str2+ j
    else:
      str2=str2+" "+ j
  
  str2=str2.lower()
  p= re.compile('[a-zA-Z]+')
  str1= p.findall(str2)

  str1fil = [x for x in str1 if x not in stop ]
 
  #a= p.findall()
  str1fil = " ".join(str1fil)
  return str1fil.encode('ascii' , 'ignore')
   
def changepath(path):
  os.chdir('/home/shubhi/Data4model/'+path)
  print('Current Directory : ' , os.getcwd())


dname=[]
for (dirpath , dirnames , filenames) in walk('/home/shubhi/Data4model/'):
        dname.extend(dirnames)
jd=[]
lis1=[]
with open('log1.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Content','JD'))
        for i in dname:
         changepath(i)
         lis=[]
         print(i)
         for k in os.listdir("/home/shubhi/Data4model/"+i+"/"):
           a=pdfcontent(k)
           if(a==None) :
             continue
           if(len(a)>80 and type(a)!=None):
               writer.writerow([a, i])
          

