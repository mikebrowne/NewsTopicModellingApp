'''

To ensure that the app stays within the bounds of biopharmaceuticals, need to extract
the industry and sector of the company in question.

'''

from selenium import webdriver
import os

from BackEnd.DataCollection.market_watch_scraper_functionality import scrape_site


class MarketWatchScraper:
    def __init__(self, test=True):
        self.test = test

    def collect(self, company_name, ticker):
        if self.test:
            browser = self.open_test_browser()
        else:
            browser = self.open_browser()

        article_search_results = self._scrape_data__(company_name.lower(), ticker.upper(), browser)
        browser.quit()
        return article_search_results

    @staticmethod
    def open_test_browser():
        chrome_driver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chrome_driver

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

    @staticmethod
    def open_browser():
        GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
        CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    @staticmethod
    def _scrape_data__(company_name, ticker, browser):

        result = scrape_site(company_name, ticker, browser)

        return result


def test_function():
    scraper = YahooFinanceScraper()
    res = scraper.collect("Acadia Pharmaceuticals", "ACAD")

    return str(res)


if __name__ == "__main__":
    print(test_function())
