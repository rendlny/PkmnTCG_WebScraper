class Set:
    def __init__(self,id,name,year,size,desc):
        self.id = id
        self.name = name
        self.year = year
        self.size = size
        self.desc = desc

        def get_id(self):
            return self.id

        def set_id(self, id):
            self.id = id
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

        def displaySet(self):
            return 'ID: ' + self.id + ', Name: ' + self.name + ', Year: ' + self.year + ', Size: ' + self.size + ', Desc: ' + self.desc  
