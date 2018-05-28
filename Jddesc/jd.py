# -*- coding: utf-8 -*-
import scrapy
import json

class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["www.glassdoor.com"]
    start_urls = (
        'https://www.glassdoor.com/Job-Descriptions/Data-Scientist.htm',
    )

    def parse(self, response):
        self.log('Scrapping started' + response.url)
        with open('Jddesc.json', 'a+') as f:
             json.dump([], f)
        a=response.css("div.module  p::text").extract()
        Job_overview= str(a[1])
        Responsibilities = []
        b= response.css("div.contentBody ul >li::text").extract()
        for i in b[:8]:
          Responsibilities.append(str(i))
        Qualifications =[]
        for i in b[8:]:
            Qualifications.append((i))
        items={
         "Job_overview":Job_overview,
         "Responsibilities":Responsibilities,
         "Qualifications": Qualifications
             }
        with open('Jddesc.json', 'r+') as f:
            f1 =json.load( f)
            print(type(f1))
        with open('Jddesc.json', 'r+') as f:
             f1.append(items)
             json.dump(f1,f)


    
             


             
