import csv
import threading
import json
import pandas as pd
from collections import Counter
def preparedic(map1,map2):
 
 with open('log.csv' , 'r+') as f:
  read= csv.reader(f)
  read1=[]
  for row in read:
        read1.append(row)
  for row in read1[1:]:
     map1[row[3]]=row[0] +" "+ row[1] + " "+ row[2]


 with open('log1.csv' , 'r+') as f:
   read= csv.reader(f)
   read1=[]
   for row in read:
        read1.append(row)
   for row in read1[1:]:
      if row[1] not in map2:
             map2[row[1]]= []
             map2[row[1]].append(row[0])
      else:
             map2[row[1]].append(row[0])

def initialize1():
 with open('finalcontent.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('JD', 'FinalContent'))

def initialize2():
 with open('finalcontentjd.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('JD', 'Training Data'))

def initialize3():
 with open('stopwordsjd.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('JD', 'stopwords'))


def cleanlog(map1):
 lis=[]
 lis1=[]
 for i , j in map1.items():
   print('Cleaning words from ..' ,i)
   lis1=j.split(" ")
   print('Making list of required words.......')
  # print('Press Y for adding N for discarding ..')
   print(lis1)
   lis= input('Enter the words you do not need').split(' ')
   print(i , 'words adding to the file...')      
   for i in lis:
       if(i in lis1):
          lis1.remove(i)
   with open('finalcontent.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((i," ".join(list(lis1))))
   lis.clear()       



def prep(map3):
 df =pd.read_csv('finalcontent.csv')
 for i in df.itertuples():
    map3[i[1]]= i[2]

def writedata1(lis1):
    with open('finalcontentjd.csv', 'a+') as out_file:
          writer = csv.writer(out_file)
          writer.writerow((i," ".join(list(lis1))))

def writedata2(lis5):
 with open('stopwordsjd.csv', 'a+') as out_file:
          writer = csv.writer(out_file)
          writer.writerow((i," ".join(list(lis5))))

def cleanbylis(lis , lis2, lis1):
     for k in set(lis) :
               if k in lis2:
                 if(lis2.count(k)>1):
                      lis1.extend(k for x in range(lis2.count(k)))
                      a=lis2.count(k)
                      for m in range(a):
                       lis2.remove(k)
                 else:     
                   lis1.append(k)
                   lis2.remove(k)
               else:
                  lis1.append(k) 

def cleanbylis1(lis5 , lis2):
     for v in set(lis5):
               a=lis2.count(v)
               for m in range(a):
                  lis2.remove(v)

def cleanbylis2(lis4 , lis5 , lis1 , lis2):
     for i in lis4:
           lis1.extend(i for x in range(lis2.count(i)))
     
     cleanbylis1(lis4,lis2)
     lis5.extend(lis2)
           

def cleanlog1(map2, map3):
     lis1=[]
     lis5=[]
     initialize2()
     initialize3()
     for i in map2:
        print('Preparing data for', i)
        lis = (map3[i.lower()]).split(" ")
        for j in map2[i]:
         
         lis2=j.split(" ") 
         print('Cleaning starts, total number of words now ', len(lis2))
         cleanbylis1(lis1 , lis2)
         cleanbylis(lis , lis2 , lis1)
         
         
         cleanbylis1(lis5, lis2)
         c= Counter(lis2)       
         print('Remaining words in lis2 i.e ', i , len(lis2) , c)
         print('Enter words you want to keep ...')
         lis4= input("-----> ").split(' ')
         cleanbylis2(lis4 , lis5 , lis1 , lis2)
         #writedata1(lis1)
         writedata2(lis5)
        
       
        lis1.clear() 
        lis5.clear()
         
map1={}  
map2={}
map3={}
preparedic(map1,map2)
#initialize1()
#cleanlog(map1)
initialize2()
initialize3()
prep(map3)
cleanlog1(map2,map3)
