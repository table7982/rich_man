
class Country():
    def __init__(self, cost, position, name, color=None):
        self.position = position
        self.special_type = None
        self.color = color
        self.name = name
        self.situation = "none"
        self.holder_color = None
        self.cost = cost
        self.house_num = 0
    def buyed(self, holder_color):
        self.situation = "buyed"
        self.holder_color = holder_color

    def di_ya(self):
        self.situation = "di_ya"
    def set_price(self,empty_price,one_price,two_price, three_price, four_price, five_price, house_cost):
        self.empty_price = empty_price
        self.one_price = one_price
        self.two_price = two_price
        self.three_price = three_price
        self.four_price = four_price
        self.five_price = five_price
        self.house_cost = house_cost

    def get_give_price(self):
        give_price = None
        if self.house_num == 0:
            give_price = self.empty_price
        elif self.house_num == 1:
            give_price = self.one_price
        elif self.house_num == 2:
            give_price = self.two_price
        elif self.house_num == 3:
            give_price = self.three_price
        elif self.house_num == 4:
            give_price = self.four_price
        elif self.house_num == 5:
            give_price = self.five_price
        return give_price

    def set_special(self, special_type):
        self.special_type = special_type
        return self.special_type


class MapItem():
    def __init__(self, item_type, position, name, cost):
        self.item_type = item_type
        self.position = position
        self.name = name
        self.cost = cost
    def set_name(self, name):
        self.name = name
    def set_cost(self, cost):
        self.cost = cost