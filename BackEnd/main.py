from BackEnd.DataCollection.business_wire_scraper import BusinessWireScraper


class BackEndInterface:
    def __init__(self):
        self.bw_scraper = BusinessWireScraper()

    def get(self, company_name, ticker, date):

        try:
            article_data = self.bw_scraper.collect(company_name, ticker, date)
            article_data["company_name"] = company_name

        except Exception as e:
            # would normally log e and if building an API, return a proper call
            # will add this later on
            print(str(e))
            return None

        return article_data
