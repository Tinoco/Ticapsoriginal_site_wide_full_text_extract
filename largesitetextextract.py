# IMPORT BEAUTIFULSOUP TO READ WEB CONTENT
from bs4 import BeautifulSoup

# IMPORT REQUESTS TO GET RESPONSES
import requests

# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemap15.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()


# FUNCTION TO GET URL RESPONSES
def get_code(url) -> requests.Response:
    return requests.get(url)


# START EMPTY WORDLIST
wordlist = ''

# WALK ON ALL URLS
for item in tqdm(urls):
    urlg = (get_code(item))
    soup = BeautifulSoup(urlg.text, 'html.parser')
    tagmanager = ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for item in tagmanager:
        counter = (soup.find_all(item))
        for item in counter:
            strings = (item.string)
            if strings != (None):
                wordlist += str(item.string)
with open('textdata.txt', 'w') as f:
    f.write(wordlist)
