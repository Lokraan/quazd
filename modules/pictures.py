# Picture API
from random import randint
import urllib.request
import os


# saves all pictures in a directory called 'webCrawlerPics'
# within the current directory

def download_web_image():
    # if you put '\' it doesn't register as a string this is a way around
    backslash = '\ '.strip(' ')

    # Checks to see if the directory exists already
    if not os.path.exists(os.getcwd() + backslash + 'webCrawlerPics'):
        # If it doesn't it makes it
        os.mkdir(os.getcwd() + backslash + 'webCrawlerPics')

    # Downloads the image to the specified file
    try:
        urllib.request.urlretrieve(input("URL: "), "webCrawlerPics" + backslash + input('file name: ') + ".png")
    # Returns an error if the link doesn't work
    except:
        print("\n ------------ \n Broken link! \n ------------ \n")

# This one you can just run within a web crawler to automatically download
# pictures on the web page without having to specify an individual name
# For each of them manually


def download_image_auto(url):
    # if you put '\' it doesn't register as a string this is a way around
    backslash = '\ '.strip(' ')
    # randomly assigns a name
    name = backslash + randint(0, 100000)
    full_name = "webCrawlerAutoPics/" + name + ".png"

    # Checks to see if the directory exists already
    if not os.path.exists(os.getcwd() + backslash + 'webCrawlerAutoPics'):
        # If it doesn't it makes it
        os.mkdir(os.getcwd() + backslash + 'webCrawlerAutoPics')

    # checks to see if the randomly assigned name is already assigned
    while os.path.isfile(full_name):
        # repeats until it finds one that isn't
        name = backslash + randint(0, 100000)
        full_name = "webCrawlerAutoPics/" + name + ".png"

    # Downloads the image
    urllib.request.urlretrieve(url, full_name)



