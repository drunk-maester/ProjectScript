# Multinomial model to classify resumes
from pdfmine import pdfcontent
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np





def checkJD(example):
     content= vectorizer.transform(example)
     JDPre = classifier.predict(content)
     return JDPre

def suitabledata(group):
     df1=  df.get_group(group)
     df1= df1.drop_duplicates()
     
#def bagofwords(group):
      


df1= pd.read_csv("log.csv")
df = pd.read_csv('log1.csv')
#df = df.drop_duplicates()
#np1= np.array()  
#for i in set(df['JD'].values):
#     if(i!= 'JD'):
#       a = suitabledata(i)
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(df1['Qualifications'].values)
lis=list()
classifier = MultinomialNB()
targets = df1['JD'].values
classifier.fit(counts, targets)

a= pdfcontent("/home/shubhi/09ac1673-6c31-43ab-891c-d8fa1b736c67-170105194520.pdf")
lis.append(a)
a1= pdfcontent("/home/shubhi/Shubham's Resume (13).pdf")
lis.append(a1)
b=checkJD(lis)
print(b)
#np1=np.array(b)
#np1 = np1.reshape(2,1)
#d = classifier.score( vectorizer.transform(lis), ['Java Developer' , 'Data Scientist'])
#print(d)
