import scrapy
"""
CityTV shows
"""
class CityTVSpider(scrapy.Spider):
    name = "citytv"
    start_urls = [
        "https://www.citytv.com/vancouver/shows/bad-blood/",
        "https://www.citytv.com/vancouver/shows/black-ish/",
        "https://www.citytv.com/vancouver/shows/bobs-burgers/",
        "https://www.citytv.com/vancouver/shows/brooklyn-nine-nine/",
        "https://www.citytv.com/vancouver/shows/dancing-with-the-stars-athletes/",
        "https://www.citytv.com/vancouver/shows/family-guy/",
        "https://www.citytv.com/vancouver/shows/fail-army/",
        "https://www.citytv.com/vancouver/shows/ghosted/",
        "https://www.citytv.com/vancouver/shows/la-vegas/",
        "https://www.citytv.com/vancouver/shows/lethal-weapon/",
        "https://www.citytv.com/vancouver/shows/life-in-pieces/",
        "https://www.citytv.com/vancouver/shows/little-big-shots/",
        "https://www.citytv.com/vancouver/shows/meghan-markle-an-american-princess/",
        "https://www.citytv.com/vancouver/shows/modern-family/",
        "https://www.citytv.com/vancouver/shows/mom/",
        "https://www.citytv.com/vancouver/shows/new-girl/",
        "https://www.citytv.com/vancouver/shows/scorpion/",
        "https://www.citytv.com/vancouver/shows/speechless/",
        "https://www.citytv.com/vancouver/shows/the-blacklist/",
        "https://www.citytv.com/vancouver/shows/the-last-man-on-earth/",
        "https://www.citytv.com/vancouver/shows/the-mick/",
        "https://www.citytv.com/vancouver/shows/the-middle/",
        "https://www.citytv.com/vancouver/shows/the-resident/",
        "https://www.citytv.com/vancouver/shows/versailles/"
    ]

    def parse(self, response):
        pass
