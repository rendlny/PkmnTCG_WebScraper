class Pokemon:
    def __init__(self,p_id,stage,hp,retreat,weak,res,res_num,evolves_from,card_id,element1_id,element2_id,atk1_id,atk2_id,atk3_id):
        self.p_id = p_id
        self.stage = stage
        self.hp = hp
        self.retreat = retreat
        self.weak = weak
        self.res = res
        self.res_num = res_num
        self.evolves_from = evolves_from
        self.card_id = card_id
        self.element1_id = element1_id
        self.element2_id = element2_id
        self.atk1_id = atk1_id
        self.atk2_id = atk2_id
        self.atk3_id = atk3_id

    def get_p_id(self):
        return self.p_id

    def set_p_id(self,p_id):
        self.p_id = p_id
        return

    def get_stage(self):
        return self.stage

    def set_stage(self,stage):
        self.stage = stage
        return

    def get_hp(self):
        return self.hp

    def set_hp(self,hp):
        self.hp = hp
        return

    def get_retreat(self):
        return self.retreat

    def set_retreat(self,retreat):
        self.retreat = retreat
        return

    def get_weak(self):
        return self.weak

    def set_weak(self,weak):
        self.weak = weak
        return

    def get_res(self):
        return self.res

    def set_res(self,res):
        self.res = res
        return

    def get_res_num(self):
        return self.res_num

    def set_res_num(self,res_num):
        self.res_num = res_num
        return

    def get_evolves_from(self):
        return self.evolves_from

    def set_evolves_from(self,evolves_from):
        self.evolves_from = evolves_from
        return

    def get_card_id(self):
        return self.card_id

    def set_card_id(self,card_id):
        self.card_id = card_id
        return

    def get_element1_id(self):
        return self.element1_id

    def set_element1_id(self,element1_id):
        self.element1_id = element1_id
        return

    def get_element2_id(self):
        return self.get_element2_id

    def set_get_element2_id(self,get_element2_id):
        self.get_element2_id = get_element2_id
        return

    def get_atk1_id(self):
        return self.atk1_id

    def set_atk1_id(self,atk1_id):
        self.atk1_id = atk1_id
        return

    def get_atk2_id(self):
        return self.atk2_id

    def set_atk2_id(self,atk2_id):
        self.atk2_id = atk2_id
        return

    def get_atk3_id(self):
        return self.atk3_id

    def set_(self,atk3_id):
        self.atk3_id = atk3_id
        return

    def display_pokemon(self):
        msg1 = 'ID: ' + self.p_id + ', Stage: ' + self.stage + ', HP: ' + self.hp + ', Retreat Cost: ' + self.retreat
        msg2 = ', Weakness: ' + self.weak + ', Resistance: ' + self.res + ', Resistance Power: ' + self.res_num
        msg3 = ', Evolves From: ' + self.evolves_from + ', Card ID: ' + self.card_id + ', Element: ' + self.element1_id + ', Extra Element: ' + self.element2_id
        msg4 =  + ', Attack 1: ' + self.atk1_id + ', Attack 2: ' + self.atk2_id + ', Attack 3: ' + self.atk3_id
        msg = msg1 + msg2 + msg3 + msg4
        return msg
