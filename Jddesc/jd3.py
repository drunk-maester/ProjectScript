# -*- coding: utf-8 -*-
import scrapy
import json
lis=['scrum-master','big-data-engineer']
z=0

class Jd3Spider(scrapy.Spider):
    name = "jd3"
    #allowed_domains = ["talentlyft.com"]
    urls ='https://www.talentlyft.com/en/resources/{}-job-description'
    start_urls = [urls.format(lis[z])]

    def parse(self, response):
        global lis,z
        self.log('Scrapping started' + response.url)
        a=response.css('div.post-desc p')
        a=a[-1]
        if(z==0):
         a=a.css('span::text').extract()
         Job_overview= (a[0])
        else:
         a=response.css('div.post-desc p::text').extract()
         Job_overview= (a[-1])
        Job_title= lis[z]
        Responsibilities = []
        Qualifications=[]
        b=response.css('div.post-desc ul')
        b=b[:1]
        for i in b:
           c= (i.css("li::text").extract())
           for j in c:
            Responsibilities.append((j))
        b=response.css('div.post-desc ul')
        for i in b[1:]:
            c= (i.css("li::text").extract())
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
        if(z<2):
           yield scrapy.Request(url =self.urls.format(lis[z]), callback= self.parse )
