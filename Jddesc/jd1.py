# -*- coding: utf-8 -*-
import scrapy
import json

lis=['python', 'java' ,'nodejs', 'web']
z=0

class Jd1Spider(scrapy.Spider):
    name = "jd1"
    #allowed_domains = ["toptal.com"]
    urls ='https://www.toptal.com/{}/job-description'
    start_urls=[urls.format(lis[z])]

    def parse(self, response):
        global lis,z
        self.log('Scrapping started' + response.url)
        a=response.css("h3 ~ p::text").extract()
        Job_title= lis[z]
        Job_overview= str(a[0])
        Responsibilities = []
        Qualifications=[]
        b=response.css("h3 ~ ul")
        b=b[:2]
        for i in b[:1]:
           c= (i.css("li::text").extract())
           for j in c:
            Responsibilities.append(str(j))
        
        for i in b[1:]:
            c= (i.css("li::text").extract())
            for j in c:
             Qualifications.append(str(j))
        
        items={
         "Title":Job_title,
         "Job_overview":Job_overview,
         "Responsibilities":Responsibilities,
         "Qualifications": Qualifications
             }
        with open('jddesc1.json', 'r+') as f:
            f1 =json.load(f)
            print(type(f1))
        with open('jddesc1.json', 'r+') as f:
             f1.append(items)
             json.dump(f1,f)
        z=z+1
        if(z<4):
           yield scrapy.Request(url =self.urls.format(lis[z]), callback= self.parse )
