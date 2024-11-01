import random

class Country():
    def __init__(self, cost, position, name, color=None):
        self.position = position
        self.color = color
        self.name = name
        self.situation = "none"
        self.message = None
        self.holder_color = None
        self.cost = cost
        self.empty_price = 1000
    def buyed(self, holder_color):
        self.situation = "buyed"
        self.holder_color = holder_color

    def di_ya(self):
        self.situation = "di_ya"

country_dir = {}
# 城市初始化，放在一个country_dir字典里面。
country_dir['1'] = Country(cost=3500, position=1, name="美国")
country_dir['3'] = Country(cost=3500, position=3, name="加拿大")
country_dir['5'] = Country(cost=2000, position=5, name="纽约火车站")
country_dir['6'] = Country(cost=1000, position=6, name="阿根廷")
country_dir['8'] = Country(cost=1000, position=8, name="墨西哥")
country_dir['9'] = Country(cost=3000, position=9, name="古巴")

country_dir['11'] = Country(cost=3000, position=11, name="法国")
country_dir['12'] = Country(cost=1500, position=12, name="电力公司")
country_dir['13'] = Country(cost=2400, position=13, name="德国")
country_dir['14'] = Country(cost=1400, position=14, name="意大利")
country_dir['15'] = Country(cost=2000, position=15, name="巴黎火车站")
country_dir['16'] = Country(cost=1400, position=16, name="西班牙")
country_dir['18'] = Country(cost=1600, position=18, name="希腊")
country_dir['19'] = Country(cost=2400, position=19, name="荷兰")

country_dir['21'] = Country(cost=2200, position=21, name="英国")
country_dir['23'] = Country(cost=1000, position=23, name="俄罗斯")
country_dir['24'] = Country(cost=1800, position=24, name="泰国")
country_dir['25'] = Country(cost=2000, position=25, name="东京火车站")
country_dir['26'] = Country(cost=3500, position=26, name="土耳其")
country_dir['27'] = Country(cost=3200, position=27, name="澳大利亚")
country_dir['28'] = Country(cost=1500, position=28, name="自来水厂")
country_dir['29'] = Country(cost=3000, position=29, name="新加坡")

country_dir['31'] = Country(cost=1000, position=31, name="韩国")
country_dir['32'] = Country(cost=4000, position=32, name="中国")
country_dir['34'] = Country(cost=2800, position=34, name="中国香港")
country_dir['35'] = Country(cost=2000, position=35, name="北京火车站")
country_dir['37'] = Country(cost=1000, position=37, name="日本")
country_dir['39'] = Country(cost=1800, position=39, name="巴西")


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

map_item_num = 40
map_type_list = [
    # 1-10
    'start',
    'place',
    'destiny',
    'place',
    'cost',
    'place',
    'place',
    'chance',
    'place',
    'place',
    # 10-20
    'lao',
    'place',
    'place',
    'place',
    'place',
    'place',
    'place',
    'destiny',
    'place',
    'place',
    # 20-30
    'stop',
    'place',
    'chance',
    'place',
    'place',
    'place',
    'place',
    'place',
    'place',
    'place',
    # 30-40
    'enter_lao',
    'place',
    'place',
    'destiny',
    'place',
    'place',
    'chance',
    'place',
    'cost',
    'place'
]
map_name_list = [
    # 1-10
    '起点',
    '美国',
    '命运',
    '加拿大',
    '所得税',
    '纽约火车站',
    '阿根廷',
    '机会',
    '墨西哥',
    '古巴',
    # 10-20
    '坐牢',
    '法国',
    '电力公司',
    '德国',
    '意大利',
    '巴黎火车站',
    '西班牙',
    '命运',
    '希腊',
    '荷兰',
    # 20-30
    '免费停车场',
    '英国',
    '机会',
    '俄罗斯',
    '泰国',
    '东京火车站',
    '土耳其',
    '澳大利亚',
    '自来水厂',
    '新加坡',
    # 30-40
    '进牢',
    '韩国',
    '中国',
    '命运',
    '中国香港',
    '北京火车站',
    '机会',
    '日本',
    '财产税',
    '巴西'
]
map_cost_list = [
    # 1-10
    None,
    3500,
    None,
    3500,
    2000,
    2000,
    1000,
    None,
    1000,
    3000,
    # 10-20
    None,
    3000,
    1500,
    2400,
    1400,
    2000,
    1400,
    None,
    1600,
    2400,
    # 20-30
    None,
    2200,
    None,
    1000,
    1800,
    2000,
    3500,
    3200,
    1500,
    3000,
    # 30-40
    None,
    1000,
    4000,
    None,
    2800,
    2000,
    None,
    1000,
    1000,
    1800
]
map_item_list = []
for i in range(map_item_num):
    map_item_type = map_type_list[i]
    map_item_name = map_name_list[i]
    map_item_cost = map_cost_list[i]
    map_item_list.append(MapItem(item_type=map_item_type,
                                 position=i,
                                 cost=map_item_cost,
                                 name=map_item_name))

class Player():
    def __init__(self, color, money):
        self.money = money
        self.color = color
        self.position = 0
        self.lao = False
        self.country_index_list = []

    def tou_shai_zi(self, start_num=1, end_num=24):
        step = random.randint(start_num, end_num)

        self.position += step
        if self.position >= map_item_num:
            circle_num = self.position // map_item_num
            self.position = self.position % map_item_num
            self.money += 2000 * circle_num
            print(f"你完成了一圈,你的钱增加2000,你现在的钱是{self.money}")
        print(f'{self.color}投到了{step},现在你在第{self.position}个格子。')
        print(f'{self.color}走到了{map_item_list[self.position].name}。')
        return self.position

    def auto_action(self):
        your_position_map_item = map_item_list[self.position]

        if your_position_map_item.item_type == 'cost':
            if self.money >= your_position_map_item.cost:
                self.money -= your_position_map_item.cost
                print(f'你被罚了{your_position_map_item.cost}钱,你还剩下{self.money}')
            else:
                print(f"穷逼,你的钱不够,你只有{self.money}")
                print(f'罚款要交{your_position_map_item.cost}')
                self.money -= your_position_map_item.cost

        if your_position_map_item.item_type == 'enter_lao':
            self.position = 10
            self.lao = True

        if your_position_map_item.item_type == 'chance':
            self.money += 200
        if your_position_map_item.item_type == 'destiny':
            self.money += 200

        if your_position_map_item.item_type == 'place':
            if country_dir[str(self.position)].situation == 'buyed':
                if country_dir[str(self.position)].holder_color != self.color:
                    print(f"你踩到了别人的地,该给{country_dir[str(self.position)].empty_price}")
                    self.money -= country_dir[str(self.position)].empty_price
                    player_dir[country_dir[str(self.position)].holder_color].money += country_dir[str(self.position)].empty_price
                    print(f'你还剩下{self.money}')
                elif country_dir[str(self.position)].holder_color == self.color:
                    print(f"你踩到了自己的{your_position_map_item.name}")
                    print("你是不是要盖房子")
                    print("这个功能还不想写。")
            elif country_dir[str(self.position)].situation == 'none':
                print(f"这{country_dir[str(self.position)].name}还没有人买啊.")
                buy_country_choose = int(input(f"输入1买{country_dir[str(self.position)].name}:"))
                if buy_country_choose == 1:
                    self.buy_country()


    def cost(self, cost_fee):
        self.money -= cost_fee
        print(f"你被罚款了{cost_fee}元，你现在还剩{self.money}元。")
        return self.money


    def judge_if_can_buy(self):
        ret = True

        if map_item_list[self.position].item_type == "place":
            print(f'这块地名字是{country_dir[str(self.position)].name}')
            print(f'这块地价格是{country_dir[str(self.position)].cost}')
            if country_dir[str(self.position)].situation == "none":
                if self.money > country_dir[str(self.position)].cost:
                    print(f"你的钱有{self.money},你可以买")
                    ret = True
                else:
                    print(f"穷逼,你才有{self.money}元,你买不起!!!")
                    ret = False
            else:
                print("这地被人买过了。")
                ret = False
        else:
            ret = False
            print("这tm就不是地。")
        return ret


    def buy_country(self):
        if self.judge_if_can_buy():
            self.money -= country_dir[str(self.position)].cost
            print(f'{country_dir[str(self.position)].name}被你买了,你还剩下{self.money}。')
            country_dir[str(self.position)].buyed(self.color)
            self.country_index_list.append(str(self.position))
    def show_message(self):
        print('----------------------')
        print(f'你的颜色是{self.color}')
        print(f'你的钱有{self.money}')
        print(f'你在序号{self.position}的格子上')
        print(f'格子的名字是{map_item_list[self.position].name}')
        country_name_list = []
        for country_index in self.country_index_list:
            country_name_list.append(country_dir[country_index].name)
        print('你的房子列表：', country_name_list)
        print('----------------------')

    def in_another_country(self, another_color):
        pass



player_dir = {}
player_dir['red'] = Player(color="red", money=2500)
player_dir['blue'] = Player(color="blue", money=2500)
red = player_dir['red']
blue = player_dir['blue']
cnt = 0
while 1:
    print(f'------第{cnt}轮--------')
    if red.lao == False:
        red.tou_shai_zi()
        red.auto_action()
        red.show_message()
    if blue.lao == False:
        blue.tou_shai_zi()
        blue.auto_action()
        blue.show_message()
    print("------------------------")
    cnt += 1
    input('输入任意键开启下一轮')










