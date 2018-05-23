# -*- coding: utf-8 -*-
import scrapy


class PdflinkscrapSpider(scrapy.Spider):
      name = "pdflinkscrap"
      allowed_domains = ["nith.ac.in"]
      start_urls = (
        'http://www.nith.ac.in/',
    )

      def parse(self, response):
               a=str(response.css('div.fusion-column-wrapper ul a[href*="14888"]::attr(href)').extract_first())

               url = a
               yield scrapy.Request(url=a , callback= self.again)


      def again(self,response):
         lis1=[]
         lis=response.css('div.computersci a::attr(href)').extract()
         for i in lis:
            lis1.append(str(i))
         j=4
         k=1
         for i in lis1:
               if(k>j):
                 break       
               url = response.urljoin(i)
               k=k+1
               yield scrapy.Request(url=url , callback= self.pdfdown)
               
      def pdfdown(self , response):
           
         path = response.url.split('/')[-1]
         self.logger.info('Saving PDF %s', path)
         with open(path, 'wb') as f:
            f.write(response.body)             
 
