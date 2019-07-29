from BackEnd.DataCollection.business_wire_scraper import BusinessWireScraper
from BackEnd.DataCollection.market_watch_scraper import MarketWatchScraper

import sys


class BackEndInterface:
    def __init__(self):
        self.bw_scraper = BusinessWireScraper()
        self.mw_scraper = MarketWatchScraper(test=False)

    def get(self, company_name, ticker, date):

        article_data = self.bw_scraper.collect(company_name, ticker, date)
        article_data["company_name"] = company_name

        company_data = self.mw_scraper.collect(company_name, ticker)
        for key, val in company_data.items():
            article_data[key] = val

        article_data["Industry"] = self.mw_scraper.collect(company_name, ticker)

        return article_data
