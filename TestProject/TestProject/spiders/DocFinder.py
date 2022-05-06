from matplotlib.pyplot import text
from numpy import extract, tile
import scrapy
import itertools

class DocfinderSpider(scrapy.Spider):
    name = 'DocFinder'
    allowed_domains = ['www.docfinder.at/suche/plastischer-chirurg?whatType=search_group&whatId=b415a43f-decd-436d-b2a6-e98830700269&userSubmitted=1&originalWhat=Plastischer+Chirurg']
    start_urls = ['https://www.docfinder.at/suche/plastischer-chirurg?whatType=search_group&whatId=b415a43f-decd-436d-b2a6-e98830700269&userSubmitted=1&originalWhat=Plastischer+Chirurg']

    def parse(self, response):
        
        doctors = response.css('div.search-results')
            
        names = doctors.css('div.name::text').extract()
        professions = [doc.strip() for doc in doctors.css('span.professions::text').extract()]
        ratings = [doc.strip() for doc in doctors.css('div.df-rating::text').extract()]
        rcounts = [doc.strip() for doc in doctors.css('span.count::text').extract()] 
        locations = [doc.strip() for doc in doctors.css('div.location-text::text').extract()]
        
        for name,profession,rating,rcount,location in zip(names,professions,ratings,rcounts, locations):
            yield {
                "Doctor's name" : name,
                "Profession" : profession,
                "Doctor's rating" : rating,
                "Number of people reviewed" : rcount,
                "Address" : location
            }
        