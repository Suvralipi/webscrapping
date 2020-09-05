# -*- coding: utf-8 -*-
import scrapy

from webscrape.spiders.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  start_urls = [
     "https://www.amazon.in/dp/B006T8BXF8", "https://www.amazon.in/dp/B00D42XLGG",
     "https://www.amazon.in/dp/B00CQ41JE4/", "https://www.amazon.in/dp/B01M9EB7ZK/"
     ]
 
  def parse(self, response):
     items = AmazonItem()
     title = response.xpath('//h1[@id="title"]/span/text()').extract()
     sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
     category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
     brand = response.xpath('//a[@id="bylineInfo"]/text()').extract()
     keys = response.xpath('//tr[@class="a-span3"]/text()').extract()
     values = response.xpath('//tr[@class="a-span9"]/text()').extract()
     dict_items = {}
     for i in range(len(keys)):
        dict_items[keys[i]] = values[i]
     
     print(dict_items)
     items['product_name'] = ''.join(title).strip()
     items['product_sale_price'] = ''.join(sale_price).strip()
     items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     items['product_brand'] = ''.join(brand).strip()
     items['product_dict'].append(dict_items)
     
     yield items