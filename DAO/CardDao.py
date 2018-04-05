from Dao import *
from Data import *

class CardDao(dao):
    def __init__(self):
        super(Data.DB)

    def addCard(self, card):
        added = False

        try:
            db = get_connection()
            data = {""}
            added = db.child("")
        except Exception:
            print("error")
