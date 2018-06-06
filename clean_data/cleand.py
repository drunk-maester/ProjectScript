import csv
import threading
import json


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
             map2[row[1]]= row[0]
      else:
             map2[row[1]]=map2[row[1]] + row[0]

def initialize1():
 with open('stopwordslog.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('JD', 'FinalContent'))




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
   with open('stopwordslog.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((i," ".join(list(lis1))))
   lis.clear()       


map1={}  
map2={}
preparedic(map1,map2)
initialize1()
cleanlog(map1)

