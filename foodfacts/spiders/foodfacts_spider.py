from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from foodfacts.items import foodfactsItem
class foodfactsSpider(BaseSpider):
    name = "foodfacts" # Name of the spider, to be used when crawling
    allowed_domains = ["foodfacts.com"] # Where the spider is allowed to go
    start_urls = [
        "http://www.foodfacts.com/index.php?option=com_products&view=products_search&id=-999&searchWord=Azodicarbonamide&searchType=Ingredients&page_limit=1142"
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response) # The XPath selector
        products = hxs.select('//div[@class="product-item"]')
        items = []
        for product in products:
            item = foodfactsItem()
            item['productTitle'] = product.select('div[@class="product-item-content"]/div[@class="product-item-info"]/h2/a/text()').extract()
            item['productLink'] = product.select('div[@class="product-item-image"]/a/@href').extract()
            item['productImage'] = product.select('div[@class="product-item-image"]/a/img/@src').extract()
            items.append(item)
        return items
