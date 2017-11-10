import urllib.request
#import BeautifulSoup
from bs4 import BeautifulSoup

#specify url
urlStart = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"
setNum = "4"
setCode = "sm" # sm / xy / bw
urlEnd = "?" + setNum + "-" + setCode + "=on"
url = urlStart + urlEnd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

################################################################################
#Function to return html details grabbed from given url
################################################################################
def scrapeUrl(url):
    webpage = urllib.request.urlopen(url)
    page = BeautifulSoup(webpage, "html.parser")
    return page
################################################################################

#query the website and return html to var 'page'
page = urllib.request.urlopen(url)

#Parse html in 'page' & store in BS format
webpage = BeautifulSoup(page, "html.parser")

#getting span that contains the number of pages
soup = webpage.find('div', id='cards-load-more')
soup = soup.findAll('span')
spanTxt = soup[1].string

#getting the number from the string by splitting by whitespace
text = spanTxt.split()
numOfPagesTxt= text[2]
numOfPages = int(numOfPagesTxt)
#not including last page as it may not have a full grid of 12 numOfCards
#need to be counted and added seperated
numOfCards = (numOfPages-1)*12


#getting lastpage & counting cards there
lastPageUrl = urlStart + numOfPagesTxt + urlEnd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
lastPage = urllib.request.urlopen(lastPageUrl)
lastPage = BeautifulSoup(lastPage, "html.parser")
cardsSection = lastPage.find('ul', id='cardResults')

#counting number of a tags as they contain cards
count = 0
for aTags in cardsSection.findAll('a'):
    count += 1

#total number of cards in the set
numOfCards = numOfCards + count

print("TOTAL CARDS = " + str(numOfCards))

################################################################################
#GETTING EACH CARDS DETAILS
################################################################################
count = 1
cardNum = 1
#looping through each page(except last)
while count <= numOfPages:
    url = urlStart + str(count) + urlEnd
    webpage = urllib.request.urlopen(url)
    page = BeautifulSoup(webpage, "html.parser")
    #finding section that contains all cards on current page
    cardsSection = page.find('ul', id='cardResults')

    #looping through each card within the cards section

    for cards in cardsSection.findAll('a'):

######## GETTING CARD IMAGE ###################################################
        imgContainer = cards.find('div')
        image = imgContainer.find('img')
        #GETTING LINK TO IMAGE FROM IMG TAG
        imgDetails = str(image).split('src=')
        imgUrl = imgDetails[1]
        #Removing tags on start & end of url
        imgUrl = imgUrl[1:]
        imgUrl = imgUrl[:-3]

########## CREATING URL TO CARD INFO ############################################
        #cards
        url = urlStart + str(setCode) + "-series/" + str(setCode) + str(setNum) + "/" + str(cardNum) + "/"

        page = scrapeUrl(url)
        name = str(page.find('h1'))
        name = name[4:]
        name = name[:-5]
        #Checking if name contains GX then removing <em> tags from name
        if "GX" in name:
            nameParts = name.split('<em>')
            name = (nameParts[0])[:-1]
            name = name + " " + nameParts[1]
            name = name[:-5]
        print(name)
        #if cardNum == 111:
            #print(page) # h1 for trainer card names
        cardNum +=1
        #print(page.find('h5'))

    #increase count to go onto next page of cards
    count +=1

########## GETTING CARD TYPE ###################################################
