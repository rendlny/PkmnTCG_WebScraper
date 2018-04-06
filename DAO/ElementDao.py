from DAO import Dao, UserAuth


class ElementDao:
    def __init__(self):
        self.data = "elementDao"

    @staticmethod
    def add_element(element):
        added = None

        try:
            db = Dao.Dao()
            db = db.get_connection()
            data = {"element_id": element.get_id(),
                    "element_name": element.get_name(),
                    "element_icon": element.get_icon()}
            added = db.child("elements", (element.get_id())).set(data, UserAuth.user['idToken'])
        except Exception:
            print("Error occurred in addElement method in ElementDao")

        return added
