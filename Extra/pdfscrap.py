# -*- coding: utf-8 -*-
import scrapy
import pymysql

class PdfscrapSpider(scrapy.Spider):
    name = "pdfscrap"
    allowed_domains = ["nith.ac.in"]
    start_urls = (
        'http://www.nith.ac.in/',
    )

    def parse(self, response):
         lis1=[]
         lis= response.css('div.vsel-content p.vsel-meta-link > a::attr(href)').extract()
         for i in lis:
            lis1.append(str(i))
         for i in lis1:
               url = response.urljoin(i)
               yield scrapy.Request(url=url , callback= self.pdfdown)

    def pdfdown(self , response):

         path = response.url.split('/')[-1]
         self.logger.info('Saving PDF %s', path)
         with open(path, 'wb') as f:
            f.write(response.body)             
 
