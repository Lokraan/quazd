import requests
from bs4 import BeautifulSoup

# Imports functions from separate modules so
# it doesn't have to all be in one big file
from Modules import pictures
from Modules import quizlet


# Finds all the links in the page
def link_text(soup):
    links = []
    for link in soup.find_all('a'):
        if link != '':
            links.append(link.text)
    print(links)


# Gets the source code of the page
# ex.
# <!DOCTYPE HTML>
# <html>
#    <body>
#        <p>blue</p>
#    </body>
# </html>

def theNewBostonPages(max_pages):
    page = 0
    while page < max_pages:
        url = "https://thenewboston.com/search.php?type=1&sort=pop&page=" + str(page)
        source_code = get_content(url)
        soup = BeautifulSoup(source_code, 'html.parser')
        for link in soup.find_all('a', {'class': 'user-name'}):
            href = "https://thenewboston.com/" + link.get('href')
            title = link.string
            print(href, title, page_info(href))
            print(" ")
        page += 1


#trade_spider(1)
#pictures.download_web_image()
quizlet.quizlet_sets_search(2)