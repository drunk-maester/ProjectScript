# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    #allowed_domains = ["toscrape.com"]
    api_url='http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [
        api_url.format(1)
    ]

    def parse(self, response):
        self.log('Scrapping started' + response.url)        
        data = json.loads(response.body)
        for quote in data['quotes']:
           yield{
            'author-name' : (quote[u'author'][u'name'])
,
            'text' : (quote[u'text']),
            'tags' : str(quote[u'tags'])
             }
        if data[u'has_next']:
            next_page= data[u'page'] +1
            yield scrapy.Request(url= self.api_url.format(next_page), callback= self.parse)  
        #for quote in response.css('div.quote'):
         #  items = {
          #    'author-name':quote.css         #('small.author::text').extract_first()
               #,'text':quote.css('span.text::text').extract_first#(),
#               'tags' : quote.css('a.tag::text').extract_first()
 #            }
  #         yield items'''

      #  urls= response.css('div.quote > span > a::attr(href)').extract()
       # for url in urls:
       #     url= response.urljoin(url)
       #     yield scrapy.Request(url= url , callback =self.details) 
        

       # next_page_url = response.css('li.next > a::attr(href)').extract_first()
       # if next_page_url:
       #   next_page_url= response.urljoin(next_page_url) 
       #   yield scrapy.Request(url=next_page_url , callback=self.parse)



   # def details(self, response):
    #   yield{
     #     'name ': response.css('h3.author-title ::text').extract_first(),
      #    'birth_date' : response.css('span.author-born-date').extract_first()

#}   

