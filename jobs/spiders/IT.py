from scrapy import Spider
import scrapy
from jobs.items import JobsItem
class JobSpider(Spider):
    name="itjobs"
    #allowed_domains=["http://www.monsterindia.com/"]
    start_urls=[
    "http://www.monsterindia.com/it-jobs.html",
    ]

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
