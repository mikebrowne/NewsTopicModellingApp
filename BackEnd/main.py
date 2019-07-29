from BackEnd.DataCollection.business_wire_scraper import BusinessWireScraper
from BackEnd.DataCollection.market_watch_scraper import MarketWatchScraper

import sys


class BackEndInterface:
    def __init__(self):
        sys.stdout.write("Starting BW Scraper")
        self.bw_scraper = BusinessWireScraper()

        sys.stdout.write("Starting MW Scraper")
        self.mw_scraper = MarketWatchScraper(test=False)

    def get(self, company_name, ticker, date):

        article_data = self.bw_scraper.collect(company_name, ticker, date)
        article_data["company_name"] = company_name

        sys.stdout.write("article keys before mw scraper: {}".format(article_data.keys()))

        try:
            company_data = self.mw_scraper.collect(company_name, ticker)
            #for key, val in company_data.items():
            #    article_data[key] = val

            #article_data["Industry"] = self.mw_scraper.collect(company_name, ticker)

        except Exception as e:
            # would normally log e and if building an API, return a proper call
            # will add this later on
            print(str(e))
            return None

        return article_data
