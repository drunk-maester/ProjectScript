# -*- coding: utf-8 -*-
import scrapy

lis=['project-manager', 'qa-engineer' ,'business-analyst']
z=0
class Jd2Spider(scrapy.Spider):
    name = "jd2"
    allowed_domains = ["resources.workable.com"]
    start_urls = (
        'https://resources.workable.com/{}-job-description',
    )

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
     #   b=response.css('li.public-DraftStyleDefault-unorderedListItem span span::text').extract()
#modify the above call :) ,,,,akkkka bakka
     # 
