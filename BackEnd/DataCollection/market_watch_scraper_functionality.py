from bs4 import BeautifulSoup


def scrape_site(company, ticker, browser):
    url = get_url(ticker)
    soup = get_page_as_soup(url, browser)

    return get_data(soup)


def get_data(soup):
    at_a_glance_div = soup.find("div", id="rightrail").find(class_="block")
    first_column = at_a_glance_div.find(class_="twowide addgutter")
    dict_results = [[item.text for item in div.find_all("p")]for div in first_column.find_all("div")]
    return {item[0].lower(): item[1] for item in dict_results if len(item)==2}


def get_page_as_soup(url, browser):
    '''
    Returns a BeautifulSoup object from a URL
    :param url: (str) - URL link to a web page
    :param browser: (obj) - Selenium Webdriver object
    :return: (obj) - BeautifulSoup object
    '''
    browser.get(url)

    content = browser.page_source

    soup = BeautifulSoup(content, "lxml")
    return soup


def get_url(ticker):
    return "https://www.marketwatch.com/investing/stock/{}/profile".format(ticker)
