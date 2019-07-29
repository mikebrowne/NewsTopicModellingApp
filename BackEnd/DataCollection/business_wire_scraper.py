'''



'''

from selenium import webdriver
import sys
from BackEnd.DataCollection.business_wire_scraper_functionality import find_article, scrape_articles


class BusinessWireScraper:
    def __init__(self):
        GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
        CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.chromedriver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    def collect(self, company_name, ticker, date):
        browser = self.chromedriver
        article_search_results = self._scrape_individual_data__(company_name.lower(), ticker.upper(), date, browser)
        return article_search_results

    @staticmethod
    def _scrape_individual_data__(company_name, ticker, date, browser):
        result = find_article(company_name, date, browser)
        sys.stdout.write("After find Article: {}".format(result))
        result["article"] = scrape_articles(result["link"], browser)
        sys.stdout.write("Immediately after scraper: {}".format(result))
        result["ticker"] = ticker

        return result


def test_function():
    import datetime as dt
    # import pandas as pd
    scraper = BusinessWireScraper()
    res = scraper.collect("Acadia Pharmaceuticals", "ACAD", dt.datetime(2019, 5, 7))
    return str(res)


if __name__ == "__main__":
    print(test_function())
