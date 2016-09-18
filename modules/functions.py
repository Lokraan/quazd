import requests
from bs4 import BeautifulSoup


def get_content(url):
    source_code = requests.get(url)
    return source_code.text


def get_soup(source_code):
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def page_info(url):
    plain_text = get_content(url)
    soup = BeautifulSoup(plain_text, 'html.parser')
    print(soup.find(id="page-description").text)
