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

#data = {"element_id": "1", "element_name": "fire", "element_icon": "https://lh4.googleusercontent.com/zpWtyQjPLzcg0Kr1ilkODWh9e_5eOPFq2qotN8iakf69DMA29DWK2gql7RNV5NUkTqSbtOcFUr8McuEAX5a8=w774-h905"}
#data = {"element_id": "2", "element_name": "water", "element_icon": "https://lh3.googleusercontent.com/FVz0R9PNTnAxnnrhlkUMIhvy78bMmNAL0C4ydH9SR4gRZoKWu8Vmjvn-2cikn1_aROqev0olphRW2pE7wqOu=w774-h905"}
#data = {"element_id": "3", "element_name": "grass", "element_icon": "https://lh6.googleusercontent.com/Z4f318L0wQaSTkhIVMhgbtuWxeFPAJ5iSEDqHYn1kjLKHdUovqknqoc274Ujo5huTjfHlWpjtFBdMnE5JJU7=w774-h905"}
#data = {"element_id": "4", "element_name": "colourless", "element_icon": "https://lh5.googleusercontent.com/6KaPAQYG11Lwg23n9nAwSFqD303DidtkIPuV9fd2IICqLXcqjisJVQ7f0q0uRe9qwT8mZ_8obPm2T83oSYTB=w774-h905"}

#db.child("elements").push(data, user['idToken'])

###printing results
#all_elements = db.child("elements").get(user['idToken'])
#for element in all_elements.each():
#    print(str(element.key()) + ": " + str(element.val()))

data =

db.child("sets").push(data, user['idToken'])
