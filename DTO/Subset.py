class Subset:
    def __init__(self, ss_id=None, name="", year=None, size=None, desc="", set_id=None):
        self.ss_id = ss_id
        self.name = name
        self.year = year
        self.size = size
        self.desc = desc
        self.set_id = set_id

    def get_ss_id(self):
        return self.ss_id

    def set_ss_id(self, ss_id):
        self.ss_id = ss_id
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year
        return

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size
        return

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc
        return

    def get_set_id(self):
        return self.set_id

    def set_set_id(self, set_id):
        self.setID = set_id
        return

    def display(self):
        return 'ID: ' + str(self.ss_id) + ', Name: ' + str(self.name) + ', Year: ' + str(self.year) + ', Size: ' \
               + str(self.size) + ', Desc: ' + str(self.desc) + ', Set ID: ' + str(self.set_id)
