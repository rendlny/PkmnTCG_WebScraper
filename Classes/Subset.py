class Subset:
    def __init__(self,ss_id,name,year,size,desc, setID):
        self.ss_id = ss_id
        self.name = name
        self.year = year
        self.size = size
        self.desc = desc
        self.setID = setID

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

    def get_setID(self):
        return self.setID

    def set_setID(self, setID):
        self.setID = setID
        return

    def display(self):
        return 'ID: ' + self.ss_id + ', Name: ' + self.name + ', Year: ' + self.year + ', Size: ' + self.size + ', Desc: ' + self.desc + ', Set ID: ' + self.setID
