class Attack:
    def _init_(self,name,desc,dmg,cost):
        self.name = name
        self.desc = desc
        self.dmg = dmg
        self.cost = cost

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

    def get_cost(cost):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost
        return    

    def displayAttack(self):
        return "Name: ", self.name, " , Description: ", self.desc, ", Damage: ", self.dmg, ", Cost: ", self.cost
