import json
import csv
import nltk
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string 

with open('log.csv', 'r+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Job overview','Responsibilities','Qualifications','JD'))

stop= stopwords.words('english') + list(string.punctuation) +['etc', 'ect' , 'using' , 'across', "'re" , "'s"]

with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        with open('newjso.json', 'r+') as f:
            data = json.load(f)
            for i in data:
              Jbo= word_tokenize(i["Job_overview"]) 
              req= i["Responsibilities"]
              str1=" "
              str2=" "
              for j in req:
                       if(str1[-1]==" "):
                               str1=str1+ j
                       else:
                               str1=str1+" "+ j
              qual=i["Qualifications"]
              for j in qual:
                     if(str2[-1]==" "):
                               str2=str2+ j
                     else:
                               str2=str2+" "+ j
              str1=word_tokenize(str1)
              str2=word_tokenize(str2)
              str1fil = [x.lower() for x in str1 if x.lower() not in stop ]
              str2fil = [x.lower() for x in str2 if x.lower() not in stop]
              Jbofil = [x.lower() for x in Jbo if x.lower() not in stop] 

              Jd= (i['Title'])
              writer.writerow([" ".join(Jbofil), " ".join(str1fil) , " ".join(str2fil) , Jd.lower()])
     

