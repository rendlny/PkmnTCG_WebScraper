class Attack:
    def __init__(self,a_id,name,desc,dmg,cost):
        self.a_id = a_id
        self.name = name
        self.desc = desc
        self.dmg = dmg
        self.cost = cost

    def get_a_id(self):
        return self.a_id

    def set_a_id(self, a_id):
        self.a_id = a_id
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc
        return

    def get_dmg(self):
        return self.dmg

    def set_dmg(self, dmg):
        self.dmg = dmg
        return

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost
        return

    def display_attack(self):
        return 'ID: ' + self.a_id ', Name: ' + self.name +  ', Description: ' + self.desc + ', Damage: ' + str(self.dmg) + ', Cost: ' + self.cost
