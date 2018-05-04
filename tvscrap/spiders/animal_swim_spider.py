import scrapy
"""
No listed air dates so will be set to None
No individual images for each episode so will use the background image
The background image is set as a dictionary
No airdates
Have to join tv_air_date with season
Some episodes are locked and have to ignore them
"""

class AdultSwimSpider(scrapy.Spider):
    name="adultswim"
    start_urls = [
        "http://www.adultswim.com/videos/ballmastrz-9009/",
        "http://www.adultswim.com/videos/mike-tyson-mysteries/",
    ]

    def parse(self, response):
        tv_name = response.xpath('.//div[@class="show-header__root main__header"]//img/@alt').extract_first()
        episodes = response.xpath('.//div[@class="episode__root"]')
        season = response.xpath('.//h3[@class="season__seasonHeader"]/text()').extract_first()
        tv_img = response.xpath('.//div[@class="trailer__root show-hero__trailer"]/@style').extract_first()
        for episode in episodes:
            # Episode is locked
            if episode.xpath(".//div[@class='watch-as-logo__root episode__watchASLogo']"):
                pass
            else:
                yield {
                    'tv_intro' : episode.xpath(".//p[@class='episode__description']/text()").extract_first(),
                    'tv_name' : tv_name,
                    'tv_link' : episode.xpath(".//a[@class='episode__link']/@href").extract_first(),
                    'tv_img' : tv_img,
                    'tv_title' : episode.xpath(".//h4[@class='episode__title']/text()").extract_first(),
                    'tv_episode_number' : episode.xpath(".//span[@class='episode__identifier']/text()").extract(),
                    'tv_air_date' : None,
                    'tv_network' : 'Adult Swim',
                }
