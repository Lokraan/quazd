# Quizlet API

import requests
from bs4 import BeautifulSoup
import os
from Modules import functions


# finds all the terms in the set, and saves it to a list
def quizlet_term(soup):
    terms = []
    for term in soup.find_all('span', {'class': 'TermText qWord lang-en'}):
        terms.append(term.text)
    return terms


# finds all the definitions in the set, and saves it to a list
def quizlet_def(soup):
    definitions = []
    for definition in soup.find_all('span', {'class': 'TermText qDef lang-en'}):
        definitions.append(definition.text)
    return definitions


# Writes all the terms and definitions to a single file
def file_write(termList, defList, file):
    # Bypass to '\' not working
    bs = '\ '.strip(' ')
    # Because the terms in quizlet are saved like so
    # term | def
    # term | def
    # there should be the same amount of defs as terms.
    for x in range(len(defList)):
        # Sometimes there's un-writeable characters
        try:
            f.write(termList[x] + " :|: " + defList[x] + '\n')
            # visual separator
            f.write("-" * 10 + '\n')
        except:
            f.write('\n')

def quizlet_sets_search(max_sets):
    # hehehehe
    bs = '\ '.strip(' ')
    if not os.path.exists(os.getcwd() + bs + 'quizletSets'):
        os.mkdir(os.getcwd() + bs + 'quizletSets')
    file = input('file name to store sets in: ')
    sets = 1
    source_code = functions.get_content('https://quizlet.com/subject/' + input('sets to look up: '))
    while sets <= int(max_sets):
        soup = functions.get_soup(source_code)
        for link in soup.find_all('a', {'class': 'SearchResult-link'}):
            f = open(os.getcwd() + bs + 'quizletSets' + bs + file + '.txt', 'w')
            global f
            href = "https://quizlet.com" + link.get('href')
            href_content = functions.get_content(href)
            set_soup = functions.get_soup(href_content)
            f.write(href + '\n')
            f.write("-" * len(href) + '\n')
            file_write(quizlet_term(set_soup), quizlet_def(set_soup), file)
            sets += 1

