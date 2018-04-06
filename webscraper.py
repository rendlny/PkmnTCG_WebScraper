import urllib.request

# import BeautifulSoup
from bs4 import BeautifulSoup

from DAO.SubsetDao import SubsetDao
from DAO.CardDao import CardDao
from DTO.Subset import Subset
from DTO.Card import Card
from core import Data
from set_and_subset_scraper import subset_array, setCode
from DB_Check import lastSet
from upload_elements import fire, water, grass, darkness, psychic, fighting, lightning, colourless, metal, fairy, dragon


################################################################################
# Function to return html details grabbed from given url
################################################################################


def scrape_url(url_to_scrape):
    web_page = urllib.request.urlopen(url_to_scrape)
    scraped_page = BeautifulSoup(web_page, "html.parser")
    return scraped_page


print()
if subset_array is None:
    print("No new subsets")

else:
    # go through each new subset and get details &cards
    for value in subset_array:
        subset = Subset()
        subset.set_ss_id = value
        subset.set_set_id(lastSet)

        print()
        print("Getting card data for subset [" + str(value) + "] ...")
        url = Data.URL_START + "?" + str(value) + "-" + setCode + "=on"
        print(url)
        page = scrape_url(url)

        # getting span that contains the number of pages
        soup = page.find('div', id='cards-load-more')
        soup = soup.findAll('span')
        spanTxt = soup[1].string

        # getting the number from the string by splitting by whitespace
        text = spanTxt.split()
        numOfPagesTxt = text[2]
        numOfPages = int(numOfPagesTxt)
        # not including last page as it may not have a full grid of 12 numOfCards
        # need to be counted and added seperated
        numOfCards = (numOfPages - 1) * 12

        subset.set_size(numOfCards)
        print("Card Count: " + str(numOfCards))

        # to get subset name, need to checked-box that is check then retrieve the <span> within it
        nameID = str(value) + '-' + setCode

        # retrieves the subsets name
        soup = (page.find('input', id=str(nameID))).findNextSibling().find('span')
        subsetName = str(soup)[6:]
        subsetName = subsetName[:-7]
        print('Name: ' + str(subsetName))
        subset.set_name(subsetName)

        subset.set_desc('Test')
        subset.set_year('2018')

        subset = Subset(str(value), str(subsetName), '2018', str(numOfCards),
                        'Test', str(lastSet))
        print(subset.display())

        # upload new subsets to Database, don't run until ready
        subsetDao = SubsetDao()
        added = subsetDao.add_subset(subset)
        print("added: " + str(added))

        if added is None:
            print("Failed to upload new subset to Database")
        else:
            print("Subset [" + subsetName + "] successfully uploaded to Database")

        cardCount = 1
        pageCount = 1
        # loop through each page
        while pageCount <= numOfPages:

            url = Data.URL_START + str(pageCount) + "?" + str(value) + "-" + setCode + "=on"
            page = scrape_url(url)
            # finding section that contains all cards on current page
            cardsSection = page.find('ul', id='cardResults')

            # loop through cards on current page getting scraping data and pushing to DB
            for cards in cardsSection.findAll('a'):

                # GETTING CARD IMAGE ###########################################
                imgContainer = cards.find('div')
                image = imgContainer.find('img')
                # GETTING LINK TO IMAGE FROM IMG TAG
                imgDetails = str(image).split('src=')
                imgUrl = imgDetails[1]
                # Removing tags on start & end of url
                imgUrl = imgUrl[1:]
                imgUrl = imgUrl[:-3]
                print(imgUrl)

                # CREATING URL TO CARD INFO ###########################################
                # cards
                url = Data.URL_START + str(setCode) + "-series/" + str(setCode) + str(value) + "/" + str(cardCount) + \
                      "/"
                print(url)
                page = scrape_url(url)
                # GETTING CARD NAME ###########################################
                name = str(page.find('h1'))
                name = name[4:]
                name = name[:-5]
                # Checking if name contains GX then removing <em> tags from name
                gx = False
                if "GX" in name:
                    gx = True
                    nameParts = name.split('<em>')
                    name = (nameParts[0])[:-1]
                    name = name + " " + nameParts[1]
                    name = name[:-5]

                print("NAME:  " + name)

                # GETTING CARD STAGE ###################################################
                stage = str(page.find('h2'))

                # Checking if card is a trainer instead of Pokemon
                if 'Trainer' not in stage and 'Energy' not in stage:
                    # crashes when it gets to trainer card NEEDS FIX
                    stage = stage[4:]
                    stage = stage[:-5]
                    print("STAGE: " + stage)

                    # GETTING CARD HP #####################################################
                    hp = str(page.find('span', class_='card-hp'))
                    hp = hp.split('</span>')
                    hp = hp[1]
                    print("HP:    " + hp)

                    # GETTING CARD TYPE ###################################################
                    pkmnType = str(page.find('i'))
                    pkmnType = pkmnType.split('icon-')
                    pkmnType = pkmnType[1]
                    pkmnType = pkmnType[:-6]
                    print("TYPE:  " + pkmnType)

                    # GETTING TYPE ID FROM TYPE
                    type_id = None
                    pkmnType = pkmnType.lower()
                    if pkmnType is (fire.get_name()).lower():
                        type_id = fire.get_id()
                    elif pkmnType is (water.get_name()).lower():
                        type_id = water.get_id()
                    elif pkmnType is (grass.get_name()).lower():
                        type_id = grass.get_id()
                    elif pkmnType is (colourless.get_name()).lower():
                        type_id = colourless.get_id()
                    elif pkmnType is (darkness.get_name()).lower():
                        type_id = darkness.get_id()
                    elif pkmnType is (psychic.get_name()).lower():
                        type_id = psychic.get_id()
                    elif pkmnType is (fighting.get_name()).lower():
                        type_id = fighting.get_id()
                    elif pkmnType is (lightning.get_name()).lower():
                        type_id = lightning.get_id()
                    elif pkmnType is (metal.get_name()).lower():
                        type_id = metal.get_id()
                    elif pkmnType is (fairy.get_name()).lower():
                        type_id = fairy.get_id()
                    elif pkmnType is (dragon.get_name()).lower():
                        type_id = dragon.get_id()

                    # GETTING ATTACKS ####################################################
                    atkCount = 0
                    # for each attack
                    for atk in page.findAll('div', class_='ability'):
                        atkCount = atkCount + 1

                        if atkCount > 1:

                            # Getting attack energy cost
                            totalCost = ""
                            for energyCost in atk.findAll('li'):
                                energyCost = energyCost["title"]
                                totalCost = totalCost + str(energyCost) + " "

                            print("ENERGY COST: " + totalCost)

                            # finding attack name
                            # if the Pokemon is a GX, getting GX attack
                            if gx and atkCount is 4:
                                # getting GX attack name
                                atkName = str(atk.find('h4', class_='left label'))
                                atkName = atkName.split('>')
                                atkName = atkName[1]
                                atkName = atkName[:-4]

                                atkName = (atkName + " GX")
                                # getting normal attacks
                            else:
                                atkName = str(atk.find('h4', class_='left label'))
                                atkName = atkName[:-5]
                                atkName = atkName.split('>')
                                atkName = atkName[1]

                            # finding attack DESCRIPTION
                            atkDesc = str(atk.find('p'))
                            atkDesc = atkDesc[3:]
                            atkDesc = atkDesc[:-4]
                            # finding attack damage
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
                            if dmg:
                                print("DAMAGE: " + atkDmg)

                    # GETTING WEAKNESS & RESISTANCE & RETREAT COST ########################
                    pkmnStats = page.find('div', class_='pokemon-stats')
                    stats = pkmnStats.findAll('div', class_='stat')
                    statCount = 0
                    for stat in stats:
                        statCount = statCount + 1

                        # getting status heading (weakness/RESISTANCE)
                        statName = stat.find('h4')
                        statName = statName.contents[0]

                        # getting WEAKNESS / WEAKNESS
                        if statCount is 1 or statCount is 2:
                            details = stat.find('li')
                            # when there is no RESISTANCE or weakness
                            if details is None:
                                print(str(statName) + ": NONE")
                            else:
                                eng = details["title"]
                                times = (details.contents[2]).strip()
                                print(str(statName) + ": " + str(eng) + " " + str(times))

                        # Getting retreat COST
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

                    # get retreat cost and desc

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
                        element = element[1]
                        print("ELEMENT: " + element)

                        name = "Basic " + element + " Energy"

                # Trainer Cards, checking trainer type
                else:
                    if 'Item' in stage:
                        print("Trainer - Item")
                        rule = Data.ITEM_RULE

                    elif 'Tool' in stage:
                        print("Trainer - Tool")
                        rule = Data.TOOL_RULE
                        specialRule = Data.TOOL_SPECIAL_RULE

                    elif 'Stadium' in stage:
                        print("Trainer - Stadium")
                        rule = Data.STADIUM_RULE

                    elif 'Supporter' in stage:
                        print("Trainer - Supporter")
                        rule = Data.SUPPORTER_RULE

                    elif 'Technical' in stage:
                        print("Technical Machine")
                        rule = Data.TM_RULE

                    elif 'Secret' in stage:
                        print("Rocket's Secret Machine")
                        rule = Data.SECRET_RULE

                    desc = page.find('div', class_='ability')
                    desc = str(desc.find('p'))
                    desc = desc[3:]
                    desc = desc[:-4]
                    print("DESCRIPTION: " + desc)

                # GETTING CARD ILLUSTRATOR ############################################
                # checking card is not an energy card as these do not have an illustrator
                if 'Energy' not in stage:
                    illus = str((page.find('div', class_='illustrator')).find('a'))
                    illus = illus[3:]
                    illus = illus[:-4]
                    illus = illus.split('>')
                    illus = illus[1]
                    print("ILLUSTRATOR: " + illus)

                # GETTING CARD SET TOTAL NUMBER (Excluding secret cards) ##############
                setTotal = str((page.find('div', class_='stats-footer')).find('span'))
                setTotal = setTotal[6:]
                setTotal = setTotal[:-7]

                # increase count to go onto next card
                print("CARD NUMBER: " + setTotal)

                # creating card with web-scraped data and uploading to DB
                card = Card(str(cardCount), name, "test desc", str(setTotal), illus, '1', imgUrl, str(lastSet), str(value), str(type_id))
                cardDao = CardDao()
                added = cardDao.add_card(card)
                if added is None:
                    print("Failed to upload new card to Database")
                else:
                    print("Card [" + name + "] successfully uploaded to Database")

                cardCount += 1

            # increase page count to go to next page of cards
            pageCount += 1
