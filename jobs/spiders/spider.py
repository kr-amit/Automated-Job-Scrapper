from scrapy import Spider
#from scrapy import Request
import scrapy
#from scrapy_splash import SplashRequest
from jobs.items import JobsItem
class JobSpider(Spider):
    name="monster"
    #allowed_domains=["http://www.monsterindia.com/"]
    start_urls=[
    "http://www.monsterindia.com/jobs-in-bhubaneshwar-1.html",
    ]

    '''def start_requests(self):
        for url in self.start_urls:
            yield spalshRequest(url,self.parse,
            endpoint='render.html',args={'wait':0.5},)'''

    def parse(self,response):
        item=JobsItem()
        jobs=response.xpath('//div[@class="jobwrap "]')
        for job in jobs:
            item['company']=job.css('span[itemprop="hiringOrganization"]::text').extract_first()
            item['title']=job.css('span[itemprop="title"]::text').extract_first()
            item['experience']=job.css('span[itemprop="experienceRequirements"]::text').extract_first()
            item['location']=job.css('span[itemprop="jobLocation"]::text').extract_first()
            item['summary']=job.css('span[itemprop="description"]::text').extract_first()
            item['skills']=job.css('span[itemprop="skills"]::text').extract_first()
            item['date']=job.css('div[itemprop="datePosted"]::text').extract_first()
            item['url']=job.xpath('//a[@class="joblnk"]/@href').extract_first()
            yield item
        #page=str(response.xpath('//a[@rel="next"]/text()').extract_first())
        #next_page=str("http://www.monsterindia.com/jobs-in-bhubaneshwar-"+page+".html")
        #next_page=response.xpath('//a[@rel="next"]//@href').extract_first()
        #yield scrapy.Request(next_page,callback=self.parse)
