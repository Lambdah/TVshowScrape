import scrapy
from scrapy.loader import ItemLoader
from tvscrap.items import TvShowItem
"""
This spider searches television episodes in Much
tv_episode_number has the structure s%d%de%d%d
tv_air_date has the structure AIRED Month %DDx, %YYYY
"""

class MuchSpider(scrapy.Spider):
    name = "much"
    start_urls = [
        "https://www.much.com/shows/tosh0/",
        "https://www.much.com/shows/south-park/",
        "https://www.much.com/shows/spotlight/",
        "https://www.much.com/shows/another-period/",
        "https://www.much.com/shows/broad-city/",
        "https://www.much.com/shows/sides/",
        "https://www.much.com/shows/nathan-for-you/",
        "https://www.much.com/shows/dan-for-a-week/",
        "https://www.much.com/shows/corporate/",
    ]

    def parse(self, response):
        tv_show_loader = ItemLoader(item = TvShowItem(), response=response)
        tv_show_loader.add_xpath('tv_intro', ".//div[@class='post-content']/p/text()")
        tv_show_loader.add_xpath('tv_name', './/div[@id="ShowInfo"]//img/@alt')
        tv_show_loader.add_xpath('tv_name', ".//div[@id='ShowInfo']//h3/a/text()")
        tv_show_loader.add_value('tv_network', 'Much')
        episode_loader = tv_show_loader.nested_xpath(".//div[@class='col-xs-12 col-sm-6 episode-item']")
        episode_loader.add_xpath('tv_link', './a/@href')
        episode_loader.add_xpath('tv_img', ".//img/@src")
        episode_loader.add_xpath('tv_title', "./a[@class='title']/text()")
        episode_loader.add_xpath('tv_episode_number', "./a[@class='ep-num']/text()")
        episode_loader.add_xpath('tv_air_date', "./a[@class='airdate']/text()")
        return tv_show_loader.load_item()
