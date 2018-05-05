# Data used across all files

URL_START = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"

DB = "poketools-tcg"

# Firebase Database Details
URL = "https://" + DB + ".firebaseio.com"
DOMAIN = DB + ".firebaseapp.com"
BUCKET = DB + ".appspot.com"
USERNAME = "ren.delaney@gmail.com"
PASSWORD = "1P@ssword"

# RULES for Trainer cards
ITEM_RULE = "You may play as many Item cards as you like during your turn (before your attack)"
TOOL_RULE = "You may play as many Item cards as you like during your turn (before your attack)"
TOOL_SPECIAL_RULE = "Attach a Pokemon Tool to 1 of your Pokemon that doesn't already have a Pokemon Tool attached to it"
STADIUM_RULE = "This card stays in play when you play it. Discard this card if another Stadium card comes into play. " \
               "If another card with the same name is in play, you can't play this card."
SUPPORTER_RULE = "You may play only 1 Supporter card during your turn (before your attack)"
TM_RULE = "Attach this card to 1 of your Pokemon"
SECRET_RULE = ""
