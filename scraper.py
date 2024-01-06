from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from itemloaders.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Article(Item):
    title = Field()
    price = Field()
    new = Field()
    refurbished = Field()
    
class Crawler(CrawlSpider):
    name = 'mercadolibre'
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 100}
    
    download_delay = 1
    
    allowed_domains = ['listado.mercadolibre.com.mx', 'articulo.mercadolibre.com.mx']
    
    start_urls = ['https://listado.mercadolibre.com.mx/macbook-pro#D[A:macbook%20pro]']
    
    rules = (
        #Horizontal Rule
        Rule(LinkExtractor(allow=r'_Desde_'), follow=True),
        
        #Vertical Rule
        Rule(LinkExtractor(allow=r'/MLM-'), follow=True, callback='parse_items'),
        )
    
    def comma_remover(self, x):
        
        x = x.replace(',', '')
        
        return x
    
    def parse_items(self, response):
        item = ItemLoader(Article(), response)
        item.add_xpath('title', '//h1/text()')
        item.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]/text()', 
                       MapCompose(self.comma_remover))
        item.add_xpath('new', '//span[@class="ui-pdp-subtitle"]/text()')
        item.add_xpath('refurbished', '//p[@class="andes-badge__content"]/text()')
        
        yield item.load_item()
