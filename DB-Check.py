import pyrebase
# Database Connection
config = {
    "apiKey": "AIzaSyB0XFXwXUjWEgKAR1nxCxxbHkJlZRy_IOk",
    "authDomain": "poketools-tcg.firebaseapp.com",
    "databaseURL": "https://poketools-tcg.firebaseio.com",
    "storageBucket": "poketools-tcg.appspot.com"
    #"serviceAccount": "1090989907773",
}

firebase = pyrebase.initialize_app(config)

# Authentication
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("ren.delaney@gmail.com", "1P@ssword")

db = firebase.database()

# Check existing
# get existing subsets and + 1 to last and check if that new subset exists
# if not +1 to last set and check if that new set exists
#if either are existing it needs to upload them to DB
