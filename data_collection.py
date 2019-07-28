from selenium import webdriver
from bs4 import BeautifulSoup
import os


def scrape():
    GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    prefs = {'profile.managed_default_content_settings.images': 2}
    chrome_options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    url = "https://en.wikipedia.org/wiki/Mathematics"

    browser.get(url)

    content = browser.page_source

    soup = BeautifulSoup(content, "lxml")

    browser.quit()

    return [item.text for item in soup.find_all("span", class_="mw-headline")]


if __name__ == "__main__":
    print(scrape())