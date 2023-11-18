"""Web scraping and crawling.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

#%%
# Setup / Data
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from util import utility
from settings import *

#%%
# Getting started

# The Website to work with, i.e. to scrape info from and crawl over it - Ultimate Classic Rock.
# The starting URL refers to articles about The Rolling Stones.
start_url = 'https://ultimateclassicrock.com/search/?s=The%20Rolling%20Stones'

# Location of the chromedriver used to work with selenium and Chrome
chromedriver_location = r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe'

#%%
# Create Response object from GET request, using requests.get(<url>, allow_redirects=False)

#%%
# Get response text from Response object, using <response>.text

#%%
# Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')


#%%
def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)

    # Get text from the Response object, using <response>.text

    # Create and return the corresponding BeautifulSoup object from the response text; use features='html.parser'

#%%
# Test get_soup(url)

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace').

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>'); e.g., find the first 'span' tag.

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>').find('<nested tag>'); e.g., find the 'a' tag in an 'article' tag.

#%%
# Demonstrate getting a tag with specific attributes
# using <BeautifulSoup object>.find('<tag>', {'<attribute>': '<value>'});
# e.g., find a 'span' tag with the 'visually-hidden' attribute.

#%%
# Demonstrate getting values of tag attributes,
# e.g. <BeautifulSoup object>.find('<tag>').text for an 'a' tag and for a 'visually-hidden' tag.

#%%
# Demonstrate <BeautifulSoup object>.find_all(<tag>), e.g. for the 'article' tag; returns a ResultSet object.

#%%
# The following lines demonstrate that getting the soup with requests.get() does not capture all tags
# (those filled with JavaScript, e.g. 'time'). That's when using selenium.webdriver is better.

#%%
# Selenium version, needed for extracting the <time> tag info

# # Guidelines - a deprecated version
# # (still OK if the chromedriver.exe version downloaded does not make Chrome-version problems):
# # Before running the following line(s), make sure to download and unzip
# # THE LATEST version of chromedriver (i.e., tho one compatible with your version of Chrome)
# # and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# # e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python310\Scripts.
# # The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# # Then you need not provide the path of the driver, just run: driver = webdriver.Chrome().
# # Alternatively, you can put the downloaded driver at a desired folder, e.g.
# # M:\Vladan\Downloads\chromedriver.exe, and get the driver by running:
# # driver = webdriver.Chrome('M:\\Vladan\\Downloads\\chromedriver.exe')
# # (Adapted from https://stackoverflow.com/a/60062969/1899061.)
#
# from selenium import webdriver
# driver = webdriver.Chrome()

# Alternatively, you can put the downloaded driver at a desired folder, e.g.
# M:\Vladan\Downloads\chromedriver.exe, and get the driver by running:
# driver = webdriver.Chrome('M:\\Vladan\\Downloads\\chromedriver.exe')

# # Guidelines - a version from
# # https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python/70099102#70099102:
# # The approach based on using the Service object.
# # Apparently, no need to download the driver, it gets downloaded by ChromeDriverManager.
# # However, you need to install the webdriver-manager package beforehand.
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://www.google.com")

# # Guidelines - a version from
# # https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python/69892580#69892580:
# # The approach based on using the Service object.
# # Before running the following line(s), make sure to download and unzip
# # THE LATEST version of chromedriver (i.e., tho one compatible with your version of Chrome)
# # and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# # e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python310\Scripts.
# # The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# # Create the required Service object explicitly, using the Service class constructor,
# # and passing the absolute path of the chromedriver.exe.
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service = Service(r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# Guidelines - a version from
# https://stackoverflow.com/a/69885677:
# The approach based on using the Service object, but skips the ChromeOptions() object.
# Before running the following line(s), make sure to download and unzip
# THE LATEST version of chromedriver (i.e., tho one compatible with your version of Chrome)
# and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python310\Scripts.
# The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# Create the required Service object explicitly, using the Service class constructor,
# and passing the absolute path of the chromedriver.exe.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service = Service(r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe')
service = Service(chromedriver_location)
driver = webdriver.Chrome(service=service)

# Once any of these approaches to get the Chrome driver is made to work,
# the following two lines get the page source (the HTML code) and turn it into a BeautifulSoup object:

driver.get(start_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace').


#%%
def get_soup_selenium(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Makes an HTTP GET request, using driver = webdriver.Chrome() from the selenium package and its driver.get(url).
    Then uses the page_source field of the driver object and the 'html.parser' to create and return the BeautifulSoup o.
    """


#%%
# Test get_soup_selenium(url)

#%%
# Demonstrate occasional anomalies in the ResultSet returned by <BeautifulSoup object>.find_all(<tag>);
# note that they may be appearing only in the selenium version, not in the requests version.

# The following lines find all 'article' tags and show that there are 11 articles on the page, not 10.
# The 11th one is something else, not visible on the page at the first glance and should be eliminated from
# further processing.

#%%
# The following line shows an anomaly in the articles ResultSet.

#%%
# Compare it to any of the other results from the Result set returned by ResultSet
# returned by <BeautifulSoup object>.find_all(<tag>).

#%%
# Demonstrate different ways of getting an attribute value for a tag (a bs4.element.Tag object),
# e.g. <tag>.find('<subtag>'), filtered with <{'class': "<class name>"}>;
# alternatively: <tag>.find('<tag>')['<attr>'], <tag>.find('<subtag>').get('<attribute>'),
# <tag>.find('<subtag>').<attribute>,... (<attribute>: e.g. text)

#%%
# Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
# <tag>.find_next_sibling() (returns just the first one);
# e.g., use the 'div' tag, class='rowline clearfix', and find the first 'span' tag in that div (and then its siblings).

#%%
# Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
# using BeautifulSoup(str(<bs4.element object>), features='html.parser').

#%%
# Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text, e.g. for an 'article' tag.

#%%
# Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last).


#%%
def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """


#%%
# Test get_specific_page(start_url, page)


#%%
def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """


#%%
# Test get_next_soup(start_url: str, page=1)


#%%
def get_next_soup_selenium(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest, using selenium instead of requests.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup_selenium(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """


#%%
# Test get_next_soup_selenium(start_url: str, page=1)


#%%
def crawl(url: str, max_pages=1):
    """Web crawler that collects info about specific articles from Ultimate Classic Rock,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup() or get_next_soup_selenium())
    from multi-page article lists.
    Parameters: the url of the starting page and the max number of pages to crawl in case of multipage lists.
    """


#%%
# Test crawl(url: str, max_pages=1)


#%%
def get_article_info_list(start_url: str, max_pages=1):
    """
    Returns structured information about articles related to The Rolling Stones from a multi-page article list.
    :param start_url: the url of the starting page of a multi-page article list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the articles from a multi-page article list
    Creates and uses the following data:
    - article_title - the title of an article
    - article_author - the author of an article
    - article_date - the date when an article has been published
    - featured_image_url - the URL of the featured image of an article
    - article_info - the 4-tuple (article_title, article_author, article_date, featured_image_url) describing an article
    - article_info_list - the list of article_info tuples for all articles on the site
    """


#%%
# Test get_articles_info(start_url: str, max_pages=1)

#%%
# Put everything in a csv file
# import csv
# csv_file = DATA_DIR / 'articles.csv'
# header_row = ['Title', 'Author', 'Date', 'Featured image']
# with open(csv_file, 'w', newline='', encoding='utf-8') as f:    # newline: avoid blank rows; encoding: enable ш,š...
#     out = csv.writer(f)
#     out.writerow(header_row)
#     out.writerows(article_info_list)
