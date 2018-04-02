import urllib.request
#import BeautifulSoup
from bs4 import BeautifulSoup

# get lastSet and lastSubset numbers from DB_check
from DB_Check import *
lastSet
lastSubset

################################################################################
#Function to return html details grabbed from given url
################################################################################
setExists = True
subsetNum = 1

while(setExists == True):

    #specify url
    urlStart = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"

    setCode = "sm" # sm / xy / bw
    urlEnd = "?" + str(subsetNum )+ "-" + setCode + "=on"
    url = urlStart + urlEnd
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    print(url)

    def scrapeUrl(url):
        webpage = urllib.request.urlopen(url)
        page = BeautifulSoup(webpage, "html.parser")
        return page

    webpage = urllib.request.urlopen(url)

    #Parse html in 'page' & store in BS format
    page = BeautifulSoup(webpage, "html.parser")

#####NOT FINDING, MUST FIND IN SUBSET 6 TO BE WORKING CORRECTLY
    divFind = page.findAll('div', class_='content-block')
    imgFound = divFind[1].find('img')
    if imgFound is not None:
        print(imgFound)
    else:
        print('FAILURE')
    #manectric = divCheck.find('img')

    ##checking if manectric card is displayed, if so then set does not exist
    ## set beginging with manetric card is displayed when a non existing set is searched
    if imgFound is not None:
        print(manectric)
        print('Nada!')
        setExists = False

    else:
        print('SubSet Exists!')
        print(subsetNum)
        subsetNum = subsetNum + 1
################################################################################
