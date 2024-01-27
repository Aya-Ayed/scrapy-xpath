import scrapy
from os.path import dirname, realpath, join
import json


"""current_dir = dirname(__file__)
url = join(current_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")"""


current_dir = dirname(__file__)
print(f"current dir: {current_dir}")
top_dir = dirname(dirname(dirname(current_dir)))
print(f"top dir {top_dir}")
url = join(top_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")



class MedalistsSpider(scrapy.Spider):
    name = 'medalists'
    allowed_domains = ['wikipedia.org']
    #start_urls = ["https://en.wikipedia.org/wiki/1992_World_Junior_Championships_in_Athletics_%E2%80%93_Men%27s_high_jump"]
    start_urls = [f'file://{url}']

    def parse(self, response):
        
        """table = response.xpath('//table')[1].xpath('tbody')
        try:
            for tr in table.xpath('tr'):
                print(tr.xpath('td/b/text()').extract()[0],
                    tr.xpath('td/a/text()').extract()[0])
        except IndexError:
            pass"""
        
        data= {}
        json_file = open('try_medalists.json','w')
        
        table = response.xpath('//table')[1].xpath('tbody')
        
        try:
            for tr in table.xpath('tr'):
                medal= tr.xpath('td/b/text()').extract()[0],
                athelete= tr.xpath('td/a/text()').extract()[0]
                data[medal[0]]= athelete
                print(data)
        except IndexError:
            pass
        print(data)
        json.dump(data,json_file)
        json_file.close()
