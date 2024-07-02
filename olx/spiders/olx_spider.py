import scrapy
from olx.items import OlxItem

class OlxSpider(scrapy.Spider):
    name = "olx"
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    
    
    

    def parse(self, response):
        for property in response.css('li.EIR5N'):
            yield {
                'property_name': property.css('span._2tW1I::text').get(),
                'property_id': property.css('a::attr(data-lurker_list_id)').get(),
                'price': property.css('span._89yzn::text').get(),
                'location': property.css('span._2oK7W::text').get(),
                'property_type': property.css('span._2Tv3q::text').get(),
                'bedrooms': property.css('span._2TV3Q::text').get(),
                'bathrooms': property.css('span._2TV3Q::text').get(),
                'description': property.css('span._2TV3Q::text').get(),
                'image_url': property.css('img::attr(src)').get(),
                'seller_name': property.css('span._3oOe9::text').get(),
            }

        next_page = response.css('a._3f7x4::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    
