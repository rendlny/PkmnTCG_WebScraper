class CardType:
    def __init__(self,ct_id,name,desc):
        self.ct_id = ct_id
        self.name = name
        self.desc = desc

        def get_ct_id(self):
            return self.ct_id

        def set_ct_id(self,ct_id):
            self.ct_id = ct_id
            return

        def get_name(self):
            return self.name

        def set_name(self,name):
            self.name = name
            return

        def get_desc(self):
            return self.desc

        def set_desc(self,desc):
            self.desc = desc
            return

        def display_cardType(self):
            return 'ID: ' + self.ct_id + ', Name: ' + self.name + ', Desc: ' + self.desc 
