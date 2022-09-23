from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as Soup
import re

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = ''
wd.get(URL)

try:
    # check if the site loads
    wait = WebDriverWait(wd,20)
    html_page = wd.page_source
    # parse the site
    page = Soup(html_page,'html.parser')
    # get titles
    title = page.find(class_='thead').get_text()
    # get reviews
    reviews_table = page.find(class_='table-striped').tbody
    reviews_tds = reviews_table.find_all('td')
    reviews = []
    for review_td in reviews_tds:
        match = re.search(r'href="/u/(.*)/.*">.*</a>', str(review_td))
        if match is not None:
            user_id = int(match.groups()[0])
        else:
            user_id = None
        time = review_td.find('span', attrs={'data-xutime': True})
        time = int(time['data-xutime'])
        review = {
            'time': time,
            'user_id': user_id,
            'text': review_td.div.text.encode('utf8')
        }
        reviews.append(review)
    print(title, reviews)

finally:
    wd.quit()