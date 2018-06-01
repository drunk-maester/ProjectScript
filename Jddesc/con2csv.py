import PyPDF2 as pd1
import os
import csv
def changepath(path):
  os.chdir('/home/shubhi/Data4model/'+path)

with open(file, 'rb') as f:
    a= pd1.PdfFileReader(f)
    b=a.numPages
    print(b)
    c= a.getPage(0)
    print(c.extractText())



flis=[]
dname=[]
for (dirpath , dirnames , filenames) in walk('/home/shubhi/Data4model/'):
        dname.extend(dirnames)

for i in dname:
  changepath(i)
  for  k in os.listdir("/home/shubhi/Data4model/"+i+"/"):
   with open(k,'rb') as in_file:

    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Skills', 'Experience,'JD'))
        writer.writerows(lines)
