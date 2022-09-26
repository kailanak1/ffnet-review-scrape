from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Soup
import re
from random import randint
import time

reviews = []


def scrape_page(url):
    wait_time = randint(2, 5)
    time.sleep(wait_time)
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wd.get(url)
    try:
        # check if the site loads
        html_page = wd.page_source
        # parse the site
        soup = Soup(html_page, 'html.parser')
        get_reviews(soup)
    finally:
        wd.quit()


# get reviews
def get_reviews(soup):
    reviews_table = soup.find(class_='table-striped').tbody
    reviews_tds = reviews_table.find_all('td')
    for review_td in reviews_tds:
        match = re.search(r'href="/u/(.*)/.*">(.*)</a>', str(review_td))
        if match is not None:
            user_id = int(match.groups()[0])
            user_name = str(match.groups()[1])
        else:
            user_id = None
            user_name = str(review_td.find('small').previous_sibling)
        u_time = review_td.find('span', attrs={'data-xutime': True})
        u_time = int(u_time['data-xutime'])
        chapter_and_date = review_td.find('small').get_text()
        review = {
            'time': u_time,
            'chapter': chapter_and_date.split('.')[0],
            'date': chapter_and_date.split('.')[1],
            'user_name': user_name,
            'user_id': user_id,
            'text': review_td.div.text.encode('utf8')
        }
        reviews.append(review)
    center = soup.find('center')
    if center:
        root_url = 'https://www.fanfiction.net'
        if 'b' in str(center.contents[-1]):
            # designed for multi-page reviews
            print(reviews)
        else:
            next_page = center.b.next_sibling.next_sibling.get('href')
            scrape_page(root_url + next_page)
    else:
        # designed for single page reviews
        print(reviews)



scrape_page(' ')







