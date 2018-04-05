import urllib.request

#import BeautifulSoup
from bs4 import BeautifulSoup
from core.Data import *
from SetAndSubsetScraper import subset_array

print()
if subset_array is None:
    print("No new subsets")

else:
    print("New subsets: ")
    # go through each new subset and get details &cards
    for value in subset_array:
        print(value)

# get url
# for loop where it loops until it gets all cards

#  .getCardData
#  push to DB

# next card
