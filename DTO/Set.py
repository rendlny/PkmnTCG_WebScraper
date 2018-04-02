class Set:
    def __init__(self,s_id,name,year,size,desc):
        self.s_id = s_id
        self.name = name
        self.year = year
        self.size = size
        self.desc = desc

    def get_s_id(self):
        return self.s_id

    def set_s_id(self, s_id):
        self.s_id = s_id
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

    def display(self):
        return 'ID: ' + self.s_id + ', Name: ' + self.name + ', Year: ' + self.year + ', Size: ' + self.size + ', Desc: ' + self.desc
