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

######## GETTING CARD IMAGE ####################################################
        imgContainer = cards.find('div')
        image = imgContainer.find('img')
        #GETTING LINK TO IMAGE FROM IMG TAG
        imgDetails = str(image).split('src=')
        imgUrl = imgDetails[1]
        #Removing tags on start & end of url
        imgUrl = imgUrl[1:]
        imgUrl = imgUrl[:-3]
        print(imgUrl)

########## CREATING URL TO CARD INFO ###########################################
        #cards
        url = urlStart + str(setCode) + "-series/" + str(setCode) + str(setNum) + "/" + str(cardNum) + "/"
        print(url)
        page = scrapeUrl(url)
########## GETTING CARD NAME ###########################################
        name = str(page.find('h1'))
        name = name[4:]
        name = name[:-5]
        #Checking if name contains GX then removing <em> tags from name
        gx = False
        if "GX" in name:
            gx = True
            nameParts = name.split('<em>')
            name = (nameParts[0])[:-1]
            name = name + " " + nameParts[1]
            name = name[:-5]

        print("NAME:  " + name)

########## GETTING CARD STAGE ###################################################
        stage = str(page.find('h2'))

        #Checking if card is a trainer instead of Pokemon
        if 'Trainer' not in stage and 'Energy' not in stage: ##crashes when it gets to trainer card NEEDS FIX
            stage = stage[4:]
            stage = stage[:-5]
            print("STAGE: " + stage)

########## GETTING CARD HP #####################################################
            hp = str(page.find('span', class_='card-hp'))
            hp = hp.split('</span>')
            hp = hp[1]
            print("HP:    " + hp)

########## GETTING CARD TYPE ###################################################
            pkmnType = str(page.find('i'))
            pkmnType = pkmnType.split('icon-')
            pkmnType = pkmnType[1]
            pkmnType = pkmnType[:-6]
            print("TYPE:  " + pkmnType)

########## GETTING ATTACKS ####################################################
            atkCount = 0
            #for each attack
            for atk in page.findAll('div', class_='ability'):
                atkCount = atkCount + 1

                if atkCount > 1:

                    #Getting attack energy cost
                    totalCost = ""
                    for energyCost in atk.findAll('li'):
                        energyCost = energyCost["title"]
                        totalCost = totalCost + str(energyCost) + " "

                    print("ENERGY COST: " + totalCost )

                ##finding attack name
                    #if the Pokemon is a GX, getting GX attack
                    if atkCount is 4 and gx == True :
                        #getting GX attack name
                        atkName = str(atk.find('h4', class_='left label'))
                        atkName = atkName.split('>')
                        atkName = atkName[1]
                        atkName = atkName[:-4]


                        atkName = (atkName + " GX")
                        #getting normal attacks
                    else:
                        atkName = str(atk.find('h4', class_='left label'))
                        atkName = atkName[:-5]
                        atkName = atkName.split('>')
                        atkName = atkName[1]

                    ##finding attack DESCRIPTION
                    atkDesc = str(atk.find('p'))
                    atkDesc = atkDesc[3:]
                    atkDesc = atkDesc[:-4]
                    ##finding attack damage
                    atkDmg = atk.find('span', class_='right')
                    dmg = False
                    if atkDmg is None:
                        dmg = False
                    else:
                        dmg = True
                        atkDmg = str(atkDmg)
                        atkDmg = atkDmg[:-7]
                        atkDmg = atkDmg.split('>')
                        atkDmg = atkDmg[1]

                    print("ATK: " + atkName)
                    print("ATK DESC: " + atkDesc)
                    if dmg == True:
                        print("DAMAGE: " + atkDmg )

########## GETTING WEAKNESS & RESISTANCE & RETREAT COST ########################
            pkmnStats = page.find('div', class_='pokemon-stats')
            stats = pkmnStats.findAll('div', class_='stat')
            statCount = 0
            for stat in stats:
                statCount= statCount + 1

                ##getting status heading (weakness/RESISTANCE)
                statName = stat.find('h4')
                statName = statName.contents[0]

                #getting WEAKNESS / WEAKNESS
                if statCount is 1 or statCount is 2:
                    details = stat.find('li')
                    #when there is no RESISTANCE or weakness
                    if details is None:
                        print(str(statName) + ": NONE")
                    else:
                        eng = details["title"]
                        times = (details.contents[2]).strip()
                        print(str(statName) + ": " + str(eng) + " " + str(times))

                #gETTING retreat COST
                elif statCount is 3:
                    energies = stat.findAll('li')
                    for eng in energies:
                        if eng is not None:
                            energy = eng["title"]
                            energyCost = ""
                            energyCost = energyCost + " " + str(energy)
                        else:
                            energyCost = "NONE"
                    print("RETREAT COST: " + energyCost)



            ##get retreat cost and desc

        # if Energy CARD
        elif 'Energy' in stage:
            energyCardType = str((page.find('div', class_='card-type')).find('h2'))
            energyCardType = energyCardType[4:]
            energyCardType = energyCardType[:-5]
            print("ENERGY TYPE: " + energyCardType)

            if 'Special' in energyCardType:
                energyDesc = str((page.find('div', class_='ability')).find('p'))
                energyDesc = energyDesc[3:]
                energyDesc = energyDesc[:-4]
                print("DESCRIPTION:" + energyDesc)

            else:

                element = str(page.find('span', class_='energy-symbol'))
                element = element[:-7]
                element = element.split(">")
                element =element[1]
                print("ELEMENT: " + element)

                name = "Basic " + element + " Energy"



        #Trainer Cards, checking trainer type
        else:
            if 'Item' in stage:
                print("Trainer - Item")
                rule = "You may play as many Item cards as you like during your turn (before your attack)"

            elif 'Tool' in stage:
                print("Trainer - Tool")
                rule = "You may play as many Item cards as you like during your turn (before your attack)"
                specialRule = "Attach a Pokemon Tool to 1 of your Pokemon that doesn't already have a Pokemon Tool attached to it."

            elif 'Stadium' in stage:
                print("Trainer - Stadium")
                rule = "This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."

            elif 'Supporter' in stage:
                print("Trainer - Supporter")
                rule = "You may play only 1 Supporter card during your turn (before your attack)"

            elif 'Technical' in stage:
                print("Technical Machine")

            elif 'Secret' in stage:
                print("Rocket's Secret Machine")

            desc = page.find('div', class_='ability')
            desc = str(desc.find('p'))
            desc = desc[3:]
            desc = desc[:-4]
            print("DESCRIPTION: " + desc)

########## GETTING CARD ILLUSTRATOR ############################################
        ##checking card is not an energy card as these do not have an illustrator
        if 'Energy' not in stage:
            illus = str((page.find('div', class_='illustrator')).find('a'))
            illus = illus[3:]
            illus = illus[:-4]
            illus = illus.split('>')
            illus = illus[1]
            print("ILLUSTRATOR: " + illus)

########## GETTING CARD SET TOTAL NUMBER (Excluding secret cards) ##############
        setTotal = str((page.find('div', class_='stats-footer')).find('span'))
        setTotal = setTotal[6:]
        setTotal = setTotal[:-7]

        #increase count to go onto next card
        print("CARD NUMBER: " + setTotal)

        print()
        cardNum +=1

    #increase count to go onto next page of cards
    count +=1
