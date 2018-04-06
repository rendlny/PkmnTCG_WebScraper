from DAO import Dao, UserAuth


class CardDao:
    def __init__(self):
        self.data = "cardDao"

    @staticmethod
    def add_card(card):
        added = None

        try:
            db = Dao.Dao()
            db = db.get_connection()
            data = {"card_id": card.get_id(),
                    "card_name": card.get_name(),
                    "card_desc": card.get_desc(),
                    "card_set_num": card.get_set_num(),
                    "card_artist": card.get_artist(),
                    "card_rarity": card.get_rarity(),
                    "card_art": card.get_art(),
                    "set_id": card.get_set_id(),
                    "subset_id": card.get_subset_id(),
                    "card_type": card.get_type_id()}
            added = db.child("cards", (card.get_id())).set(data, UserAuth.user['idToken'])
        except Exception:
            print("Error occurred in addCard method in CardDao")

        return added
