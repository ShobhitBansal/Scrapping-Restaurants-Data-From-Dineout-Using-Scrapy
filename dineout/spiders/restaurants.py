# -*- coding: utf-8 -*-
import scrapy


class RestaurantsSpider(scrapy.Spider):
    name = 'restaurants'
    allowed_domains = ['www.dineout.co.in']
    #start_urls = ['https://www.dineout.co.in/mumbai-restaurants']
    

    def start_requests(self):
        page_number=1
        yield scrapy.Request(url="https://www.dineout.co.in/{0}-restaurants?p={1}".format(self.city,page_number),callback=self.parse,headers= {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }, meta = {'page': page_number})

    def parse(self, response):
        page_number = response.request.meta['page']
        for relative_url in response.xpath("//a[@class='restnt-name ellipsis']/@href").getall():

            yield response.follow(url=relative_url, callback=self.parse_restaurant)

        page_number +=1
        total_rests = int(response.xpath("//*[@id='w1-sorter']/h1/span/text()").get()[1:-1])
        if page_number<=int(total_rests/21)+1:
            yield scrapy.Request(url="https://www.dineout.co.in/{0}-restaurants?p={1}".format(self.city,page_number),callback=self.parse,headers= {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            }, meta = {'page': page_number})

    def parse_restaurant(self, response):
        name = response.xpath("//h1/text()").get()
        cuisine = response.xpath("//*[@id='about']/div/div/div[1]/div[2]/a/text()").getall()
        res_type = response.xpath("//*[@id='about']/div/div/div[2]/div[2]/p/text()").get()
        cost = response.xpath("//*[@id='about']/div/div/div[3]/div[2]/p/text()").get()
        facilities = response.xpath("//*[@id='about']/div/div/div[4]/div[2]/ul/li/a/text()").getall()
        rating = response.xpath("//*[@id='review-section']/div[1]/div[1]/div[1]/div[1]/text()").get()
        no_of_votes = response.xpath("//*[@id='review-section']/div[1]/div[1]/div[1]/div[2]/div[1]/text()").get()
        no_of_reviews = response.xpath("//*[@id='review-section']/div[1]/div[1]/div[1]/div[2]/div[2]/text()").get()
        location = response.xpath("//*[@id='detailDiv']/section[1]/div[1]/div[2]/a[1]/text()").get()

        yield {
            'Name' : str(name),
            'Cuisine' : str(cuisine),
            'Type' : str(res_type),
            'Cost' : str(cost),
            'Facilities' : str(facilities),
            'Rating' : str(rating),
            'Votes' : str(no_of_votes),
            'No. of Reviews' : str(no_of_reviews),
            'Location' : str(location)
        }

