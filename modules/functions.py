import requests
from bs4 import BeautifulSoup


def get_content(url):
    source_code = requests.get(url)
    
    # Gets the source code of the page
    # ex.
    # <!DOCTYPE HTML>
    # <html>
    #    <body>
    #        <p>blue</p>
    #    </body>
    # </html>

    return source_code.text


def get_soup(source_code):
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def page_info(url):
    plain_text = get_content(url)
    soup = BeautifulSoup(plain_text, 'html.parser')
    print(soup.find(id="page-description").text)


# Finds all the links in the page
def find_links(link):
    soup = get_soup(link)
    links = []
    for link in soup.find_all('a'):
        if link != '':
            links.append(link.text)
    print(links)
# Way to to run
# find_links("https://www.google.com")
