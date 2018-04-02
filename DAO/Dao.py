import pyrebase

from core.Data import Data

class Dao:
    def __init__(self):
        self.db_name = Data.DB

    def get_connection(self):
        url = "https://" + self.db_name + ".firebaseio.com"
        domain = self.db_name + ".firebaseapp.com"
        bucket = self.db_name + ".appspot.com"
        api_key = "AIzaSyB0XFXwXUjWEgKAR1nxCxxbHkJlZRy_IOk"
        username = "ren.delaney@gmail.com"
        password = "1P@ssword"
        db = None

        config = {
            "apiKey": api_key,
            "authDomain": domain,
            "databaseURL": url,
            "storageBucket": bucket
        }
        ##try to get connection to DB
        try:
            firebase = pyrebase.initialize_app(config)
            # Authentication

            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(username, password)
            print("Reached middle of try")

            db = firebase.database()

        except:
            print("Failed to get Connection to DB")

        return db


db = Dao()
db = db.get_connection()
if db is not None:
    all_elements = db.child("elements").get(user['idToken'])
    for element in all_elements.each():
        print(str(element.key()) + ": " + str(element.val()))
