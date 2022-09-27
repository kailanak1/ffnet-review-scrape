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
        html_page = wd.page_source
        soup = Soup(html_page, 'html.parser')
    finally:
        wd.quit()
        get_reviews(soup)


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
        chapter_and_date = review_td.find('small').get_text()
        review = {
            'chapter': chapter_and_date.split('.')[0],
            'date': chapter_and_date.split('.')[1],
            'user_name': user_name,
            'user_id': user_id,
            'text': review_td.div.text.encode('utf8')
        }
        reviews.append(review)
    center = soup.find('center')
    title = soup.find(class_='thead')
    if center:
        if 'b' in str(center.contents[-1]):
            title = title.find_all('a')[-1].get_text()
            title = f'Reviews for {title}'
            # return(title, reviews)
            create_txt_file(title, reviews)
        else:
            root_url = 'https://www.fanfiction.net'
            next_page = center.b.next_sibling.next_sibling.get('href')
            scrape_page(root_url + next_page)
    else:
        # return(title, reviews)
        title = title.get_text()
        create_txt_file(title, reviews)


def create_txt_file(title, reviews):
    with open(f'{title}.txt', 'w') as f:
        for review in reviews:
            review_text = str(review["text"]).replace('b', '', 1)
            f.write(f'Chapter: {review["chapter"]}\n')
            f.write(f'Date: {review["date"]}\n')
            f.write(f'Username: {review["user_name"]}\n')
            f.write(f'User ID: {review["user_id"]}\n')
            f.write(f'Review: {review_text}\n\n')


scrape_page(' ')

