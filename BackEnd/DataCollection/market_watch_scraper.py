'''

To ensure that the app stays within the bounds of biopharmaceuticals, need to extract
the industry and sector of the company in question.

'''

import os
import sys

from BackEnd.DataCollection.market_watch_scraper_functionality import scrape_site


class MarketWatchScraper:
    def __init__(self):
        pass

    def collect(self, company_name, ticker):
        try:
            return scrape_site(company_name, ticker)

        except Exception as e:
            sys.stdout.write("Time out - BW...", str(e))
            return {}


def test_function():
    scraper = MarketWatchScraper()
    res = scraper.collect("Acadia Pharmaceuticals", "ACAD")

    return str(res)


if __name__ == "__main__":
    print(test_function())
