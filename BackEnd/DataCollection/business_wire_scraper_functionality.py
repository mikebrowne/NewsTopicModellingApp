'''

scraper_functionality.py

Module contains the functions used to implement the data scraper. The public functions are:
    * scrape_search_pages()
    * scrape_articles

Developer: Michael Browne
Email: mikelcbrowne@gmail.com

'''

# IMPORTS
import pandas as pd
import numpy as np
import re
import time
from bs4 import BeautifulSoup
import datetime as dt


# PUBLIC FUNCTIONS
def find_article(company_name, date, browser):
    '''
    Searches and scrapes the resulting pages for article data. If it does not exist, returns None
    :param company_name: (str) - Company Name
    :param browser: (Selenium WebBrowser)
    :param num_pages: (int) - How many pages to go through
    :return: (pd.DataFrame)
    '''
    return get_search_pages(company_name, date, browser)


def scrape_articles(link, browser):
    '''
    Goes through each article and collects the post
    :param article_links: (list) - A list of the article URLs
    :param browser: (Selenium WebBrowser)
    :return: (list) - A list of the article writings as strings
    '''
    return scrape_individual_article(link, browser)


# PRIVATE HELPER FUNCTIONS
def get_search_pages(company_name, date, browser):
    soups = {}  # The key will be the page number, the value will be the data

    # First get the number of pages
    first_page_url = search_page_url(company_name, 1)
    first_page_soup = get_page_as_soup(first_page_url, browser)
    results = first_page_soup.find(class_="bw-search-results")
    num_pages = int(results.find_all("div")[-1].find_all("a")[-1].text)

    # Iterate through the pages and get the soup objects
    # for i in range(1, num_pages + 1):
    for i in range(1, 3):
        try:
            url = search_page_url(company_name, i)
            search_page_soup = get_page_as_soup(url, browser)

            list_items = soup_to_list_items(search_page_soup)

            parsed_list_items = [list_item_to_data(li) for li in list_items]

            for li in parsed_list_items:
                if li["date"] == date:
                    return li

        except Exception as e:
            # Note: Will build in a better system here for exception handling...
            print("Scraper failed for {} on search page: {}.".format(company_name, i))
            print("\t", str(e))

    return None


def soups_to_data(soup_dict):
    list_items = []
    for i in soup_dict:
        list_items += soup_to_list_items(soup_dict[i])
    return {i: list_item_to_data(li) for i, li in enumerate(list_items)}


def soup_to_list_items(soup):
    results = soup.find(class_="bw-search-results")
    list_items = results.find_all("li")
    return list(list_items)


def list_item_to_data(li):
      return {
        "date": dt.datetime.strptime(li.time.text, '%B %d, %Y'),
        "title": li.h3.text,
        "link": li.a["href"]
    }


def search_page_url(company_name, page_number):
    '''
    Get's the URL for the search page of a company
    :param company_name: (str)
    :param page_number: (int)
    :return: (str) - Formatted URL
    '''
    company_name = company_name.replace(" ", "%20")
    url_template_1 = r"https://www.businesswire.com/portal/site/home/search"
    url_template_2 = r"/?searchType=news&searchTerm={}&searchPage={}"
    return (url_template_1 + url_template_2).format(company_name, page_number)


def scrape_individual_article(url, browser):
    try:
        soup = get_page_as_soup(url, browser)
        section = soup.find(class_="bw-release-story")
        s = section.text
        s = re.sub('\s+', ' ', s)
        return s

    except Exception as e:
        print("Could not scrape the article data for : ", url)
        print("\t", str(e))


def get_page_as_soup(url, browser):
    '''
    Returns a BeautifulSoup object from a URL
    :param url: (str) - URL link to a web page
    :param browser: (obj) - Selenium Webdriver object
    :return: (obj) - BeautifulSoup object
    '''
    browser.get(url)

    time.sleep(np.random.randint(1, 6))

    content = browser.page_source

    soup = BeautifulSoup(content, "lxml")
    return soup