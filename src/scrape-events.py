import requests
from bs4 import BeautifulSoup

url="https://www.pokemon.com/us/play-pokemon/pokemon-events/leagues/5028/prerelease"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

################################################################################
#Function to return html details grabbed from given url
################################################################################
def scrapeUrl(url):

    #query the website and return html to var 'page'
    response = requests.get(f'{url}', headers=headers)
    webpage = response.text

    #Parse html in 'page' & store in BS format
    page = BeautifulSoup(webpage, "html.parser")
    return page
################################################################################

webpage = scrapeUrl(url)
titleCheck = webpage.find('title')
if titleCheck.string == "Pardon Our Interruption":
    print("WE'VE BEEN BLOCKED")
    quit()

# find the table that contains the data
eventTable = webpage.find('table')

if eventTable is None:
    print("NOTHING FOUND")
    quit()

for row in eventTable.findAll('tr'):
    print(row)
    for index, col in enumerate(row.findAll('td')):
        match index:
            case 0:
                print('Series')
                print(col)
            case 1:
                print('Cycle = {col}')
                print(col)
            case 2:
                print('Players = {col}')
                print(col)
            case 3:
                print('Date = {col}')
                print(col)
        print(index)
        
    quit()

