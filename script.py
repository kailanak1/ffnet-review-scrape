from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as Soup
import re
import time 


def scrape_page(url):
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wd.get(url)
    try:
        # check if the site loads
        wait = WebDriverWait(wd,20)
        html_page = wd.page_source
        # parse the site
        page = Soup(html_page,'html.parser')
        return page
    finally:
        wd.quit()


# get reviews
def get_reviews(page):
    # get title
    title = page.find(class_='thead').get_text()
    reviews_table = page.find(class_='table-striped').tbody
    reviews_tds = reviews_table.find_all('td')
    reviews = []
    for review_td in reviews_tds:
        match = re.search(r'href="/u/(.*)/.*">(.*)</a>', str(review_td))
        if match is not None:
            user_id = int(match.groups()[0])
            user_name = str(match.groups()[1])
        else:
            user_id = None
            user_name = str(review_td.find('small').previous_sibling)
        time = review_td.find('span', attrs={'data-xutime': True})
        time = int(time['data-xutime'])
        chapter_and_date = review_td.find('small').get_text()
        review = {
            'time': time,
            'chapter': chapter_and_date.split('.')[0],
            'date': chapter_and_date.split('.')[1],
            'user_name': user_name,
            'user_id': user_id,
            'text': review_td.div.text.encode('utf8')
        }
        reviews.append(review)
    print(title, reviews)


def scrape_reviews(url):
    get_reviews(scrape_page(url))

