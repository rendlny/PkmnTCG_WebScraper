# Pokemon TCG WebScraper

This program grabs pages from the official Pokemon Card Database Webpage and runs through each cards grabbing data to be added
to the database.

## Setup

First install the requirements

```
pip install -r requirements.txt
```

## Usage

Run webscrape.py to start the webscraper

```
python webscrape.py
```

## Details Scraped

- Url to card image
- Card name
- Stage
- HP
- Type
- Attack:
  - Energy Cost
  - Attack Name
  - Attack Description
  - Attack Damage
- Weakness
- Resistance
- Retreat Cost
- Illustrator
- Card Number

Card Set & Subset numbers must be set in the code & it will run through that subset

## Other Features

    run through all sets
    check for new sets
    seperate cards by type (Pokemon, Trainer, Eneregy)
