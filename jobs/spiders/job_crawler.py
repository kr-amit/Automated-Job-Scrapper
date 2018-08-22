import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jobs.items import JobsItem

class JobCrwalerSpider(CrawlSpider):
    name = 'job_crawler'
    #allowed_domains = ['www.monsterindia.com/']
    start_urls = ['http://www.monsterindia.com/jobs-in-bhubaneshwar.html/']
    def parse(self,response):
        next_page=response.xpath('//a[@rel="next"]/href').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page,callback=self.parse_item)


    def parse_item(self, response):
        item=JobsItem()
        jobs=response.xpath('//div[@class="jobwrap "]')

        for job in jobs:
            item['company']=job.css('span[itemprop="hiringOrganization"]::text').extract_first()
            item['title']=job.css('span[itemprop="title"]::text').extract_first()
            item['experience']=job.css('span[itemprop="experienceRequirements"]::text').extract_first()
            item['location']=job.css('span[itemprop="jobLocation"]::text').extract_first()
            item['summary']=job.css('span[itemprop="description"]::text').extract_first()
            item['skills']=job.css('span[itemprop="skills"]::text').extract_first()
            yield item
