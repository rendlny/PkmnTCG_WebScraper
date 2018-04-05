from DAO import Dao, UserAuth


class SubsetDao:
    def __init__(self):
        self.data = "subsetDao"

    @staticmethod
    def add_subset(subset):
        added = False

        try:

            print("Start of try")
            db = Dao.Dao()
            print("created isntance of DAO")
            db = db.get_connection()
            print("Got DB connection")

            print("set_id " + subset.get_set_id())

            data = {"set_id": subset.get_set_id(),
                    "subset_desc": subset.get_desc(),
                    "subset_id": subset.get_ss_id(),
                    "subset_name": subset.get_name(),
                    "subset_size": subset.get_size(),
                    "subset_year": subset.get_year()}
            print("Created data to be pushed to DB")
            added = db.child("subsets", str(subset.get_ss_id())).set(data, UserAuth.user['idToken'])
            print("Got to end of method")
        except Exception:
            print("Error occured in addSubset method in SubsetDao")

        return added
