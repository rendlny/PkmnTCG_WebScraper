class Energy:
    def __init__(self,en_id,is_special):
        self.en_id = en_id
        self.is_special = is_special

    def get_en_id(self):
        return self.en_id

    def set_en_id(self, en_id):
        self.en_id = en_id
        return

    def is_special(self):
        return self.is_special

    def set_is_special(self, is_special):
        self.is_special = is_special
        return

    def display(self):
        return 'ID: ' + self.en_id + ', Special? ' + self.is_special
