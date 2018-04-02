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
#user = auth.refresh(user['refreshToken'])
db = firebase.database()

##sending data to db
#data = {"element_id": "1", "element_name": "fire", "element_icon": "https://lh4.googleusercontent.com/zpWtyQjPLzcg0Kr1ilkODWh9e_5eOPFq2qotN8iakf69DMA29DWK2gql7RNV5NUkTqSbtOcFUr8McuEAX5a8=w774-h905"}
#db.child("elements").push(data, user['idToken'])

##Getting and printing data
#all_elements = db.child("elements").get(user['idToken'])
#for element in all_elements.each():
#    print(str(element.key()) + ": " + str(element.val()))

#print('Reached end of file')

#data = {"set_id": "sm4", "set_name": "testSet", "set_year": "2018", "set_size": "52", "set_desc": "test set2"}
#db.child("sets", "2").set(data, user['idToken'])
