# -*- coding: utf-8 -*-
import scrapy
import json
lis=['project-manager', 'qa-engineer' ,'business-analyst']
z=0
class Jd2Spider(scrapy.Spider):
    name = "jd2"
    allowed_domains = ["resources.workable.com"]
    urls = 'https://resources.workable.com/{}-job-description'
    
    start_urls = [urls.format(lis[z]) ]
    def parse(self, response):
        global lis,z
        self.log('Scrapping started' + response.url)
        a=response.css('div.jd-content ~ p  span::text').extract()
        Job_title= lis[z]
        Job_overview=""
        for i in a:
          Job_overview = Job_overview + str(i)
        Responsibilities = []
        Qualifications=[]
        b=response.css('div.jd-content ~ ul ')
        str1=""
        b=b[:1]
        for i in b:
          c= i.css('li > div')
          for j in c:
              d= j.css('span span::text').extract()
              for k in d:
                  str1=str1+ (k)
              Responsibilities.append(str1)
              str1=""
        b=response.css('div.jd-content ~ ul ')
        b=b[1:2]
        for i in b:
          c= i.css('li > div')
          for j in c:
              d= j.css('span span::text').extract()
              for k in d:
                  str1=str1+ (k)
              Qualifications.append(str1)
              str1=""
        items={
         "Title":Job_title,
         "Job_overview":Job_overview,
         "Responsibilities":Responsibilities,
         "Qualifications": Qualifications
             }
        with open('Jddesc.json', 'r+') as f:
            f1 =json.load(f)
            print(type(f1))
        with open('Jddesc.json', 'r+') as f:
             f1.append(items)
             json.dump(f1,f) 

        z=z+1
        if(z<3):
           yield scrapy.Request(url =self.urls.format(lis[z]), callback= self.details )


    def details(self,response):
        global z, lis
        a=response.css('div.jd-content ~ p  span::text').extract()
        Job_title= lis[z]
        Job_overview=""
        for i in a:
          Job_overview = Job_overview + (i)
        Responsibilities = []
        Qualifications=[]
        b=response.css('div.jd-content ~ ul ')
        str1=""
        b=b[:1]
        for i in b:
          c= i.css('li::text').extract()
          for j in c:
              Responsibilities.append((j))
              str1=""
        b=response.css('div.jd-content ~ ul ')
        b=b[1:2]
        for i in b:
          c= i.css('li::text').extract()
          for j in c:
              Qualifications.append((j))
        items={
         "Title":Job_title,
         "Job_overview":Job_overview,
         "Responsibilities":Responsibilities,
         "Qualifications": Qualifications
             }
        with open('Jddesc.json', 'r+') as f:
            f1 =json.load(f)
            print(type(f1))
        with open('Jddesc.json', 'r+') as f:
             f1.append(items)
             json.dump(f1,f) 

        z=z+1
        if(z<3):
           yield scrapy.Request(url =self.urls.format(lis[z]), callback= self.details1 )
    def details1(self,response):
        global z, lis
        a=response.css('div.jd-content ~ p  span::text').extract()
        Job_title= lis[z]
        Job_overview=a[0]
        
        Responsibilities = []
        Qualifications=[]
        b=response.css('div.jd-content ~ ul ')
        str1=""
        b=b[:1]
        for i in b:
          c= i.css('li::text').extract()
          for j in c:
              Responsibilities.append((j))
              str1=""
        for i in b:
          c= i.css('li span::text').extract()
          for j in c:
              Responsibilities.append((j))
              str1=""
        
        b=response.css('div.jd-content ~ ul ')
        b=b[1:2]
        c= b.css('li span a::text').extract()
        c=c[0]
        d= b.css('li span::text').extract()
        d=d[0]
        c=c +d
        Qualifications.append(c)
        d= b.css('li span::text').extract()
        for i in d[1:]:
              Qualifications.append(i)
        items={
         "Title":Job_title,
         "Job_overview":Job_overview,
         "Responsibilities":Responsibilities,
         "Qualifications": Qualifications
             }
        with open('Jddesc.json', 'r+') as f:
            f1 =json.load(f)
            print(type(f1))
        with open('Jddesc.json', 'r+') as f:
             f1.append(items)
             json.dump(f1,f) 

        z=z+1
        if(z<3):
           yield scrapy.Request(url =self.urls.format(lis[z]), callback= self.details1 )

