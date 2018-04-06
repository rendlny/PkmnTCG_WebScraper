import DB_Connection

##getting DB - connection from DB_Connection file
db = DB_Connection.db
user = DB_Connection.user

#try to get a set w/ id 1 , if it exists then try for next set (id+1) and loop until last set is found

print("Searching for last set...")
lastSet = 1
setCode = None
lastSubset = 1

while True:
    setId = str(lastSet)
    returnedSet = db.child("sets").child(setId).get(user['idToken']).val()

    if returnedSet is not None:
        #get the set code
        setCode = db.child("sets").child(setId).child("set_id").get(user['idToken']).val()
        lastSet += 1
    else:
        lastSet -= 1
        print("Last set found: " + str(lastSet) + " -> " + setCode)
        print()
        print("Searching for last Subset...")

        while True:
            #now check for last subset
            subsetId = str(lastSubset)
            subset = db.child("subsets").child(subsetId).get(user['idToken']).val()

            if subset is not None:
                lastSubset += 1


            else:
                lastSubset -= 1
                print("Last Subset found: " + str(lastSubset))
                print()
                break
        break

#last set and subsets found. use these in webscraper to check for new sets & subsets
