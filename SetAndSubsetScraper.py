import urllib.request
#import BeautifulSoup
from bs4 import BeautifulSoup

# get lastSet and lastSubset numbers & setCode from DB_check
from DB_Check import *
lastSet
lastSubset
setCode
newSubset = lastSubset + 1
################################################################################
#Function to return html details grabbed from given url
################################################################################
setExists = True
urlStart = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"

print("Checking for new sets and subsets...")
while(setExists == True):

    #specify url , this url is for the first card of the given set
    urlEnd = str(setCode) + "-series/" + str(setCode) + str(newSubset) + "/1/"
    url = urlStart + urlEnd
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    def scrapeUrl(url):
        webpage = urllib.request.urlopen(url)
        page = BeautifulSoup(webpage, "html.parser")
        return page

    try:
        page = scrapeUrl(url)
        print("Subset [" + str(newSubset) + "] exists!")
        newSubset +=1

    except Exception:
        print("Subset [" + str(newSubset) + "] does not exist.")
        setExists = False
