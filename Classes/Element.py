class Element:
    def __init__(self,e_id,name,icon):
        self.e_id = e_id
        self.name = name
        self.icon = icon

        def get_e_id(self):
            return self.e_id

        def set_e_id(self, e_id):
            self.e_id = e_id
            return

        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name
            return

        def get_icon(self):
            return self.icon

        def set_icon(self, icon):
            self.icon = icon
            return

        def display_element(self):
            return 'ID: ' + self.e_id + ', Name: ' + self.name + ', Icon: ' + self.icon
