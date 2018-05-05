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
user = auth.sign_in_with_email_and_password("testuser@test.com", "T3stPassword")
db = firebase.database()
