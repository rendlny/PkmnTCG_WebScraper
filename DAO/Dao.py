import pyrebase
from DAO import Data

class Dao:
    def __init__(self):
        self.db_name = Data.DB

    def get_connection(self):
        db = None

        config = {
            "apiKey": Data.API_KEY,
            "authDomain": Data.DOMAIN,
            "databaseURL": Data.URL,
            "storageBucket": Data.BUCKET
        }
        ##try to get connection to DB
        try:
            firebase = pyrebase.initialize_app(config)
            # Authentication

            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(Data.USERNAME, Data.PASSWORD)
            db = firebase.database()

        except:
            if user is None:
                print("Auth failed")
            else:
                print("Failed to get Connection to DB")

        return db

    def display(self):
        print("DAO DB Name: " + self.db_name)

#db = Dao()
#db = db.get_connection()

