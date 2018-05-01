import scrapy
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
        # Get the intro of the tv show
        tv_intro = response.xpath(".//div[@class='post-content']/p/text()").extract_first()
        tv_name = response.xpath('.//div[@id="ShowInfo"]//img/@alt').extract_first()
        if tv_name is None:
            tv_name = response.xpath("//div[@id='ShowInfo']//h3/a/text()").extract_first()
        episodes = response.xpath(".//div[@class='col-xs-12 col-sm-6 episode-item']")
        for episode in episodes:
            yield {
                'tv_intro' : tv_intro,
                'tv_name' : tv_name,
                'tv_link' : episode.xpath("./a/@href").extract_first(),
                'tv_img' : episode.xpath(".//img/@src").extract_first(),
                'tv_title' : episode.xpath("./a[@class='title']/text()").extract_first(),
                'tv_episode_number' : episode.xpath("./a[@class='ep-num']/text()").extract_first(),
                'tv_air_date' : episode.xpath("./a[@class='airdate']/text()").extract_first(),
            }
