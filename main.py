import requests
from bs4 import BeautifulSoup

# Imports functions from separate modules so
# it doesn't have to all be in one big file
from Modules import pictures  # Contains functions to download pictures
from Modules import quizlet # Contains functions to download sets off quizlet
from Modules import functions  # Contains base functions
