import scrapy

class AdultSwimSpider(scrapy.Spider):
    name="adultswim"
    start_urls = [
        "http://www.adultswim.com/videos/ballmastrz-9009/",
        "http://www.adultswim.com/videos/mike-tyson-mysteries/",
    ]

    def parse(self, response):
        tv_name = response.xpath('.//div[@class="show-header__root main__header"]//img/@alt').extract_first()
        episodes = response.xpath('.//div[@class="episode__root"]')
        for episode in episodes:
            yield {
                'tv_intro' : tv_intro,
                'tv_name' : tv_name,
                'tv_link' : episode.xpath("").extract_first(),
                'tv_img' : episode.xpath("").extract_first(),
                'tv_title' : episode.xpath("").extract_first(),
                'tv_episode_number' : episode.xpath("").extract()),
                'tv_air_date' : episode.xpath().extract(),
            }
