from pyrebase import pyrebase

from DAO import Data

config = {
            "apiKey": Data.API_KEY,
            "authDomain": Data.DOMAIN,
            "databaseURL": Data.URL,
            "storageBucket": Data.BUCKET
}


firebase = pyrebase.initialize_app(config)
# Authentication
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(Data.USERNAME, Data.PASSWORD)