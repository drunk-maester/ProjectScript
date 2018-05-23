# -*- coding: utf-8 -*-
import scrapy

class LoginSpider(scrapy.Spider):
    name = "login-spider"
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        self.log('Scrapping started' + response.url)        
        token= response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data = {
         'csrf_token' :token,
         'username': 'abc',
         'password' :'abc'

          }
        yield scrapy.FormRequest(url =self.login_url, formdata=data ,callback= self.parse_quotes) 

    def parse_quotes(self, response):
      #parse the main page after spider is logged in
       for q in response.css('div.quote'):
         yield{
           'author-name':q.css('small.author::text').extract_first(),
           'author-url' : q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()
          

           }  
