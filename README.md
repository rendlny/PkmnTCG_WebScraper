# Pokemon TCG WebScraper

This program grabs pages from the official Pokemon Card Database Webpage and runs through each cards grabbing data to be added
to the database. This code is designed to be run as a cron job, once or twice a month to fetch the latest card releases from Pokemon.

## Setup

### Dependencies

This project has a requirements.txt file to allow you to easily install the dependencies.

```
pip install -r requirements.txt
```

The following packages will be installed:

- pycryptodome
- pyrebase
- beautifulsoup4
- python-dotenv
- mypy
- pycodestyle
- pylint

## Usage

Run start.py to start the webscraper

```
py start.py
```

## Static tests

- [MyPy](https://mypy.readthedocs.io/en/stable/getting_started.html): `mypy start.py`
- [Pylint](https://pypi.org/project/pylint/): `mypy start.py`
- [pycodestyle](https://pypi.org/project/pycodestyle/): `pycodestyle start.py`

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

- run through all sets
- check for new sets
- separate cards by type (Pokemon, Trainer, Energy)
