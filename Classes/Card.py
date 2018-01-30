class Card:
    def __init__(self,c_id,name,desc,setnum,artist,rarity,art,set_id,subset_id,type_id):
        self.c_id = c_id
        self.name = name
        self.desc = desc
        self.setnum = setnum
        self.artist = artist
        self.rarity = rarity
        self.art = art
        self.set_id = set_id
        self.subset_id = subset_id
        self.type_id = type_id

        def get_id(self):
            return self.c_id

        def set_id(self,c_id):
            self.c_id = c_id
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

        def get_setnum(self):
            return self.setnum

        def set_setnum(self,setnum):
            self.setnum = setnum
            return

        def get_artist(self):
            return self.artist

        def set_artist(self,artist):
            self.artist = artist
            return

        def get_rarity(self):
            return self.rarity

        def set_rarity(self,rarity):
            self.rarity = rarity
            return

        def get_art(self):
            return self.art

        def set_art(self,art):
            self.art = art
            return

        def get_set_id(self):
            return self.set_id

        def set_set_id(self,set_id):
            self.set_id = set_id
            return

        def get_subset_id(self):
            return self.subset_id

        def set_subset_id(self,subset_id):
            self.subset_id = subset_id
            return

        def get_type_id(self):
            return self.type_id

        def set_type_id(self,type_id):
            self.type_id = type_id
            return

        def display_card(self):
            msg1 = 'ID: ' + self.c_id + ', Name: ' + self.name + ', Description: ' + self.desc + ', SetNum: ' + self.setnum + ', Artist: ' + self.artist + ', Rarity: ' + self.rarity
            msg = msg1 + ', Art: ' + self.art + ', Set ID: ' + self.set_id + ', Subset ID: ' + self.subset_id + ', Type ID: ' + self.type_id
            return  msg
