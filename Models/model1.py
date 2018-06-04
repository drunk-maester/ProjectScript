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


df = pd.read_csv('log1.csv')


vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(df['Content'].values)
lis=list()
classifier = MultinomialNB()
targets = df['JD'].values
classifier.fit(counts, targets)

a= pdfcontent("/home/shubhi/09ac1673-6c31-43ab-891c-d8fa1b736c67-170105194520.pdf")
lis.append(a)
a1= pdfcontent("/home/shubhi/#####################")
#lis.append(a1)
b=checkJD(lis)
print(b)
#np1=np.array(b)
#np1 = np1.reshape(2,1)
#d = classifier.score( vectorizer.transform(lis), ['Java Developer' , 'Data Scientist'])
#print(d)
