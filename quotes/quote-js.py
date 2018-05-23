# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuoteJsSpider(scrapy.Spider):
     name = "quotesjs"

     def start_requests(self):
      yield SplashRequest(
url ='http://quotes.toscrape.com/js',
callback = self.parse,

)
    

     def parse(self, response):
        self.log('Scrapping started' + response.url)        
        for quote in response.css("div.quote"):
            yield{
           "text": quote.css("span.text::text").extract_first(),
           "author": quote.css("small.author::text").extract_first(),
           "tags":quote.css("div.tags >a.tag::text").extract_first(),}

