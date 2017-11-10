import urllib.request
#import BeautifulSoup
from bs4 import BeautifulSoup

################################################################################
#Function to return html details grabbed from given url
################################################################################
setExists = True

while(setExists == True):

    #specify url
    urlStart = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"

    setNum = 1
    setCode = "sm" # sm / xy / bw
    urlEnd = "?" + str(setNum )+ "-" + setCode + "=on"
    url = urlStart + urlEnd
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    def scrapeUrl(url):
        webpage = urllib.request.urlopen(url)
        page = BeautifulSoup(webpage, "html.parser")
        return page

    webpage = urllib.request.urlopen(url)

    #Parse html in 'page' & store in BS format
    page = BeautifulSoup(webpage, "html.parser")

    categories = page.findAll('fieldset', class_='expansions-category')
    ##checking if categories exist, if they don't then set does not exist
    if categories is not None:
        for category in categories:
            setName = category.find('h2')
            print(str(setName))
            subsets = category.findAll('li')

        setNum = setNum + 1
    else:
        setExists = False
################################################################################
