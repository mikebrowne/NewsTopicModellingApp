from BackEnd.DataCollection.business_wire_scraper import BusinessWireScraper
from BackEnd.DataCollection.market_watch_scraper import MarketWatchScraper


class BackEndInterface:
    def __init__(self):
        self.bw_scraper = BusinessWireScraper()
        self.mw_scraper = MarketWatchScraper()

    def get(self, company_name, ticker, date):

        try:
            article_data = self.bw_scraper.collect(company_name, ticker, date)
            article_data["company_name"] = company_name

            company_data = self.mw_scraper.collect(company_name, ticker)
            for key, val in company_data.items():
                article_data[key] = val

        except Exception as e:
            # would normally log e and if building an API, return a proper call
            # will add this later on
            print(str(e))
            return None

        return article_data
