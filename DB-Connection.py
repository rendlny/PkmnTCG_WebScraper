import pyrebase
# Database Connection
config = {
    "apiKey": "api_key_here",
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

##sending data to db
#data = {"element_id": "1", "element_name": "fire", "element_icon": "https://lh4.googleusercontent.com/zpWtyQjPLzcg0Kr1ilkODWh9e_5eOPFq2qotN8iakf69DMA29DWK2gql7RNV5NUkTqSbtOcFUr8McuEAX5a8=w774-h905"}
#db.child("elements").push(data, user['idToken'])

##Getting and printing data
#all_elements = db.child("elements").get(user['idToken'])
#for element in all_elements.each():
    #print(str(element.key()) + ": " + str(element.val()))
