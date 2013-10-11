# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class foodfactsItem(Item):
    # define the fields for your item here like:
    # name = Field()

    productTitle = Field() # product-item-info
    productLink = Field() # view-product-link
    productImage = Field() # product-item-image

    # pass
