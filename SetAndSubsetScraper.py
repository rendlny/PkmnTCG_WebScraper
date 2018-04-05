import urllib.request
# import BeautifulSoup
from bs4 import BeautifulSoup
from array import array
from core.Data import *

# get lastSet and lastSubset numbers & setCode from DB_check
from DB_Check import *
# lastSet, lastSubset, setCode
newSubset = lastSubset + 1
subset_array = None
################################################################################
# Function to return html details grabbed from given url
################################################################################
setExists = True

print("Checking for new sets and subsets...")
while setExists:

    # specify url , this url is for the first card of the given set
    urlEnd = str(setCode) + "-series/" + str(setCode) + str(newSubset) + "/1/"
    url = URL_START + urlEnd

    def scrape_url(url):
        webpage = urllib.request.urlopen(url)
        page = BeautifulSoup(webpage, "html.parser")
        return page

    try:
        page = scrape_url(url)
        print("Subset [" + str(newSubset) + "] exists!")
        # if the array has not been initialized
        if subset_array is None:
            subset_array = array("i")
            subset_array.append(newSubset)
        # otherwise add int to existing array
        else:
            subset_array.append(newSubset)

        newSubset += 1

    except Exception:
        print("Subset [" + str(newSubset) + "] does not exist.")
        setExists = False
