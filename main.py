import random
import time
import class_lib as C

# 1、免费停车场功能 finished
# 2、把玩家回合写到类里面
# 3、飞机场功能 finished
# 4、电力公司、自来水厂功能 finished
# 5、命运、机会功能
# 6、经过起点本身仍然给钱的bug finished
# 7、赎回自己被抵押的土地 finished

country_dir = {}
# 城市初始化，放在一个country_dir字典里面。
country_dir['1'] = C.Country(cost=3500, position=1, name="美国")
country_dir['1'].set_price(350, 1750, 5000, 11000, 13000, 15000, 2000)

country_dir['3'] = C.Country(cost=3500, position=3, name="加拿大")
country_dir['3'].set_price(350, 1750, 5000, 11000, 13000, 15000, 2000)

country_dir['5'] = C.Country(cost=2000, position=5, name="纽约火车站")
country_dir['5'].set_special('station')

country_dir['6'] = C.Country(cost=1000, position=6, name="阿根廷")
country_dir['6'].set_price(60,300,900,2700,4000,550,500)

country_dir['8'] = C.Country(cost=1000, position=8, name="墨西哥")
country_dir['8'].set_price(60,300,900,2700,4000,550,500)

country_dir['9'] = C.Country(cost=3000, position=9, name="古巴")
country_dir['9'].set_price(260, 1300, 3900, 9000, 11000, 12750, 500)

country_dir['11'] = C.Country(cost=3000, position=11, name="法国")
country_dir['11'].set_price(260, 1300, 3900, 9000, 11000, 12750, 2000)

country_dir['12'] = C.Country(cost=1500, position=12, name="电力公司")
country_dir['12'].set_special('company')
country_dir['13'] = C.Country(cost=2400, position=13, name="德国")
country_dir['13'].set_price(200, 1000, 3000, 7500, 9250, 11000,1500)
country_dir['14'] = C.Country(cost=1400, position=14, name="意大利")
country_dir['14'].set_price(100, 500, 1500, 4500, 6250, 7500, 1000)

country_dir['15'] = C.Country(cost=2000, position=15, name="巴黎火车站")
country_dir['15'].set_special('station')

country_dir['16'] = C.Country(cost=1400, position=16, name="西班牙")
country_dir['16'].set_price(100, 500, 1500, 4500, 6250, 7500, 1000)


country_dir['18'] = C.Country(cost=1600, position=18, name="希腊")
country_dir['18'].set_price(120,600,1800,5000,7000,9000,1000)
country_dir['19'] = C.Country(cost=2400, position=19, name="荷兰")
country_dir['19'].set_price(200,1000,3000,7500,9250,11000,1500)


country_dir['21'] = C.Country(cost=2200, position=21, name="英国")
country_dir['21'].set_price(180, 900, 2500, 7000, 8750, 10500, 1500)

country_dir['23'] = C.Country(cost=1000, position=23, name="俄罗斯")
country_dir['23'].set_price(60, 300, 900, 2700, 4000, 5500, 500)

country_dir['24'] = C.Country(cost=1800, position=24, name="泰国")
country_dir['24'].set_price(140, 700, 2000, 5500, 7500, 9500, 1000)

country_dir['25'] = C.Country(cost=2000, position=25, name="东京火车站")
country_dir['25'].set_special('station')

country_dir['26'] = C.Country(cost=3500, position=26, name="土耳其")
country_dir['26'].set_price(350, 1750, 5000, 11000, 13000, 15000, 2000)
country_dir['27'] = C.Country(cost=3200, position=27, name="澳大利亚")
country_dir['27'].set_price(280, 1750, 5000, 11000, 13000, 15000,2000)

country_dir['28'] = C.Country(cost=1500, position=28, name="自来水厂")
country_dir['28'].set_special('company')

country_dir['29'] = C.Country(cost=3000, position=29, name="新加坡")
country_dir['29'].set_price(260,1300,3900,9000,11000,12750,2000)
country_dir['31'] = C.Country(cost=1000, position=31, name="韩国")
country_dir['31'].set_price(60,300,900,2700,4000,5500,500)
country_dir['32'] = C.Country(cost=4000, position=32, name="中国")
country_dir['32'].set_price(500,2000,6000,14000,17000,20000,2000)
country_dir['34'] = C.Country(cost=2800, position=34, name="中国香港")
country_dir['34'].set_price(220,1200,3600,8500,10250,12000,1500)

country_dir['35'] = C.Country(cost=2000, position=35, name="北京火车站")
country_dir['35'].set_special('station')

country_dir['37'] = C.Country(cost=1000, position=37, name="日本")
country_dir['37'].set_price(60, 300, 900, 2700, 4000, 5500,500)
country_dir['39'] = C.Country(cost=1800, position=39, name="巴西")
country_dir['39'].set_price(140,700,2000,5500,7500,9500,1000)




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
    'stop', # 这个是免费停车场
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
    map_item_list.append(C.MapItem(item_type=map_item_type,
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
        self.situation = 'live'
        self.stop = False
        self.step = None
    def tou_shai_zi(self, start_num=1, end_num=12):
        step = random.randint(start_num, end_num)
        self.step = step
        self.position += step
        if self.position >= map_item_num:
            circle_num = self.position // map_item_num
            self.position = self.position % map_item_num
            if self.position != 0:
                self.money += 2000 * circle_num
                print(f"{self.color}完成了一圈,钱增加2000,你现在的钱是{self.money}")
            elif self.position == 0:
                print(f"{self.color}完成了一圈，但是你走到了起点，你的钱是{self.money}")
        print(f'{self.color}投到了{step},现在你在第{self.position}个格子。')
        print(f'{self.color}走到了{map_item_list[self.position].name}。')
        return self.position

    def auto_action(self):
        your_position_map_item = map_item_list[self.position]

        # 1、罚款操作
        if your_position_map_item.item_type == 'cost':
            self.cost(your_position_map_item.cost)

        # 2、进牢操作
        if your_position_map_item.item_type == 'enter_lao':
            self.position = 10
            self.lao = True

        # 3、如果你踩到了机会或者命运
        if your_position_map_item.item_type == 'chance':
            self.go_to_chance()
        if your_position_map_item.item_type == 'destiny':
            self.go_to_destiny()

        # 4、如果你踩到了免费停车场
        if your_position_map_item.item_type == 'stop':
            self.stop = True

        # 5、如果你踩到了国家
        if your_position_map_item.item_type == 'place':
            your_position_country = country_dir[str(self.position)]
            # 5.2 如果国家被买过了,不是抵押状态
            if your_position_country.situation == 'buyed':
                # 5.2.1 这个国家还不是你的
                if your_position_country.holder_color != self.color:

                    # 5.2.1.1 这个国家对应的人还没有坐牢
                    if player_dir[your_position_country.holder_color].lao == False:
                        # 判断国家类型
                        # 正常国家
                        if your_position_country.special_type is None:
                            self.go_to_another_nomal_country()
                        # 公司
                        elif your_position_country.special_type == 'company':
                            self.go_to_another_company()
                        # 车站
                        elif your_position_country.special_type == 'station':
                            self.go_to_another_station()
                    else:
                        print(f"{player_dir[your_position_country.holder_color].color}坐牢了，你不用给钱了。")
                # 5.2.2 这个国家是你的
                elif your_position_country.holder_color == self.color:
                    # 判断国家是否有特殊类型
                    if your_position_country.special_type is None:
                        self.go_to_self_nomal_country()
                    else:
                        print("这是你的车站或者公司，无法进行操作。")
            elif your_position_country.situation == 'di_ya':
                print(f"{your_position_country.name}被抵押了。")

            # 5.1 如果国家没有被买过
            elif your_position_country.situation == 'none':
                self.go_to_none_country()

    def active_action(self):
        while 1:
            if_can_shuhui = True
            self.show_message()
            di_ya_index_list = []
            for country_index in self.country_index_list:
                your_country = country_dir[country_index]
                if your_country.situation == 'di_ya':
                    di_ya_index_list.append(country_index)
            print("这是你的回合,你可以进行抵押、赎回操作")
            print("输入1,进行进入赎回界面")
            print("输入2,进行进入抵押界面")
            print("输入其他，结束操作。")
            if not di_ya_index_list:
                if_can_shuhui = False
                print("但是你没有抵押的国家，不能执行赎回操作。")
            your_active_choose = input("请输入：")
            if your_active_choose == '1':
                if if_can_shuhui:
                    di_ya_name_list = []
                    for di_ya_country_index in di_ya_index_list:
                        di_ya_name_list.append(country_dir[di_ya_country_index].name)
                    print(di_ya_name_list)
                    shuhui_index_choose = int(input("请输入你想要赎回的序号"))
                    shuhui_index_choose -= 1
                    self.shuhui_self_country(di_ya_index_list[shuhui_index_choose])
            elif your_active_choose == '2':
                self.di_ya_get_money()
            else:
                print("主动选择结束。")
                break

    def shuhui_self_country(self, country_index):
        ret = False
        country_index = str(country_index)
        shuhui_country = country_dir[country_index]
        if shuhui_country.holder_color == self.color:
            if self.money >= (shuhui_country.cost / 2):
                self.money -= (shuhui_country.cost / 2)
                country_dir[country_index].situation = 'buyed'
                print("赎回成功！")
                ret = True
            else:
                print("你赎不起")
                di_ya_choose = input("如果你要抵押，请输入1，输入其他结束：")
                if di_ya_choose == '1':
                    self.di_ya_get_money()
                    ret = self.shuhui_self_country(country_index)
                else:
                    ret = False
        else:
            print("程序出现bug了，排查一下问题。")
        return ret

    def di_ya_get_money(self):
        print("你要抵押房子还是抵押国家")
        active_action_choose = input("抵押房子选择1，抵押国家选择2：")
        if active_action_choose == '1':
            self.di_ya_house()
        elif active_action_choose == '2':
            self.di_ya_country()

    def judge_money(self):
        if self.money < 0:
            while self.money < 0:
                self.di_ya_get_money()
                choose_dead = input("选择破产输入1,输入其他，继续抵押。")
                if choose_dead == '1':
                    self.do_dead()
                    break

    def do_dead(self):
        #你的国家变成无人购买状态
        if self.country_index_list:
            for your_country_index in self.country_index_list:
                country_dir[str(your_country_index)].situation = 'none'
                country_dir[str(your_country_index)].house_num = 0
                country_dir[str(your_country_index)].holder_color = None
        self.position = 0
        self.money = 0
        self.country_index_list = []
        self.situation = 'dead'

    def di_ya_house(self):
        if self.country_index_list:
            country_name_list = []
            house_num_list = []
            for your_country_index in self.country_index_list:
                house_num_list.append(country_dir[your_country_index].house_num)
                country_name_list.append(country_dir[your_country_index].name)
            print(f'你有的国家是{country_name_list}')
            print(f'你的国家有的房子数目列表是{house_num_list}')
            if sum(house_num_list):
                di_ya_index_choose = int(input("你要选择卖第几个国家的房子啊:"))
                di_ya_index_choose -= 1
                if house_num_list[di_ya_index_choose] > 0:
                    country_dir[str(self.country_index_list[di_ya_index_choose])].house_num -= 1
                    di_ya_money = int(country_dir[str(self.country_index_list[di_ya_index_choose])].house_cost)/2
                    self.money += di_ya_money
                    print(f"你抵押了{di_ya_money}元。")
                    print(f'你现在有{self.money}元。')
                else:
                    print("你选择的国家没有房子。")

    def di_ya_country(self):
        if self.country_index_list:
            country_name_list = []
            situation_list = []
            for your_country_index in self.country_index_list:
                situation_list.append(country_dir[your_country_index].situation)
                country_name_list.append(country_dir[your_country_index].name)
            print(f'你有的国家是{country_name_list}')
            print(f'你的国家状态是{situation_list}')
            if_can_diya = False
            for situation in situation_list:
                if situation == "buyed":
                    if_can_diya = True
            if if_can_diya:
                di_ya_country_choose = int(input("请选择你抵押国家的序号"))
                di_ya_country_choose -= 1
                your_choose_country = country_dir[str(self.country_index_list[di_ya_country_choose])]
                if your_choose_country.situation == 'buyed' and your_choose_country.house_num == 0:
                    your_choose_country.situation = 'di_ya'
                    self.money += your_choose_country.cost/2
                    print(f"{your_choose_country.name}抵押了")
                    print(f"你得到了{your_choose_country.cost/2}")
                    print(f'你现在有{self.money}')
                else:
                    print("国家已经被抵押或者国家上有房子。")

    def cost(self, cost_fee):
        self.money -= cost_fee
        print(f"你被罚款了{cost_fee}元，你现在还剩{self.money}元。")
        self.judge_money()

    def buy_country(self):
        your_position_country = country_dir[str(self.position)]
        if self.money >= your_position_country.cost:
            self.money -= your_position_country.cost
            print(f'{your_position_country.name}被你买了,你还剩下{self.money}。')
            your_position_country.buyed(self.color)
            self.country_index_list.append(str(self.position))
            ret = True
        else:
            self.show_message()
            if_di_ya_choose = input("你的钱不够,是否进行抵押操作,然后尝试购买,输入1，继续抵押：")
            if if_di_ya_choose == '1':
                self.di_ya_get_money()
                # 进行递归操作
                ret = self.buy_country()
            else:
                ret = False
        return ret

    def show_message(self):
        print('||----------------------')
        print(f'||你的颜色是{self.color}')
        print(f'||你的钱有{self.money}')
        print(f'||你在序号{self.position}的格子上')
        print(f'||格子的名字是{map_item_list[self.position].name}')
        country_name_list = []
        house_num_list = []
        country_situation_list = []
        country_cost_list = []
        for country_index in self.country_index_list:
            country_name_list.append(country_dir[country_index].name)
            house_num_list.append(country_dir[country_index].house_num)
            country_situation_list.append(country_dir[country_index].situation)
            country_cost_list.append(country_dir[country_index].cost)
        print('||你的国家列表：', country_name_list)
        print('||你的国家房子列表：', house_num_list)
        print('||你的国家状态列表：', country_situation_list)
        print('||你的国家价格列表：',country_cost_list)
        print('----------------------')

    def build_house(self, country_index):
        if self.money >= country_dir[country_index].house_cost:
            print(f'房子的价格是{country_dir[country_index].house_cost}')
            print(f'你的钱还有:{self.money}')
            self.money -= country_dir[country_index].house_cost
            print(f'买完房子,你还剩下{self.money}元')
            country_dir[country_index].house_num += 1
            ret = True
        else:
            print("穷鬼,你的钱不够买房子")
            self.show_message()
            if_di_ya_choose = int(input("你的钱不够,是否进行抵押操作,然后尝试购买,输入1，继续抵押："))
            if if_di_ya_choose == 1:
                self.di_ya_get_money()
                # 进行递归操作
                ret = self.build_house(country_index)
            else:
                ret = False
        return ret

    def go_to_another_station(self):
        another_station = country_dir[str(self.position)]
        another_player = player_dir[another_station.holder_color]
        print(f"你走到了{another_station.holder_color}的{another_station.name}上")
        another_station_num = 0
        for another_country_index in another_player.country_index_list:
            if another_country_index == '5' or another_country_index == '15' or another_country_index == '25' or another_country_index == '35':
                # 判断车站是不是没有抵押，来计算钱数
                if country_dir[another_country_index].situation == 'buyed':
                    another_station_num += 1
        give_money = another_station_num * 250
        self.money -= give_money
        another_player.money += give_money
        print(f'{another_player.color}有{another_station_num}个车站，你需要给{give_money}元.')
        print(f'你还剩下{self.money}元')
        print(f'{another_player.color}还有{another_player.money}元')
        self.judge_money()

    def go_to_another_company(self):
        another_company = country_dir[str(self.position)]
        another_player = player_dir[another_company.holder_color]
        another_company_num = 0
        print(f'你走到了{another_company.holder_color}的{another_company.name}上')
        for another_country_index in another_player.country_index_list:
            if another_country_index == '12' or another_country_index == '28':
                another_company_num += 1
        give_money = 0
        if another_company_num == 1:
            give_money = self.step * 10
        elif another_company_num == 2:
            give_money = self.step * 100
        self.money -= give_money
        another_player.money += give_money
        print(f'{another_player.color}有{another_company_num}个厂房，你需要给{give_money}元.')
        print(f'你还剩下{self.money}元')
        print(f'{another_player.color}还有{another_player.money}元')
        self.judge_money()

    def go_to_chance(self):
        random_get_loss_seed = random.random()
        if random_get_loss_seed > 0.5:
            print(f"是好机会，获得600元")
            self.money += 600
        elif random_get_loss_seed <= 0.5:
            print(f"是坏机会，失去600元")
            self.money -= 600
            self.judge_money()

    def go_to_destiny(self):
        random_get_loss_seed = random.random()
        if random_get_loss_seed > 0.5:
            print(f"是好命运，获得600元")
            self.money += 600
        elif random_get_loss_seed <= 0.5:
            print(f"是坏命运，失去600元")
            self.money -= 600
            self.judge_money()

    def go_to_another_nomal_country(self):
        your_position_country = country_dir[str(self.position)]
        give_price = your_position_country.get_give_price()
        print(f"你踩到了别人的地,该给{give_price}")
        self.money -= give_price
        player_dir[your_position_country.holder_color].money += give_price
        print(f'你还剩下{self.money}')
        self.judge_money()

    def go_to_self_nomal_country(self):
        your_position_country = country_dir[str(self.position)]
        print(f"你踩到了自己的{your_position_country.name}")
        choose_build_house = input("你是不是要买房子, 输入1买房子：")
        if your_position_country.house_num <= 4:
            if choose_build_house == '1':
                ret_build_house = self.build_house(str(self.position))
                if ret_build_house:
                    print('买房成功')
                else:
                    print("买房失败")
        else:
            print(f'{your_position_country.name}你都有五个房子了，别买了')
    def go_to_none_country(self):
        your_position_country = country_dir[str(self.position)]
        print(f"这{your_position_country.name}还没有人买啊.")
        print(f'这个国家{your_position_country.cost}元，而你有{self.money}元。')
        buy_country_choose = input(f"输入1买{country_dir[str(self.position)].name}:")
        if buy_country_choose == '1':
            build_country_ret = self.buy_country()
            if build_country_ret:
                print("购买国家成功。")
            else:
                print("购买国家失败。")

    def play(self, sleep_time):
        if self.situation == 'live':
            if self.lao == False:
                if self.stop == False:
                    print(f"\n这是{self.color}的回合\n")
                    self.tou_shai_zi()
                    time.sleep(sleep_time)
                    self.auto_action()
                    time.sleep(sleep_time)
                    self.active_action()
                    self.judge_money()
                    time.sleep(sleep_time)
                else:
                    print("你进停车场了老弟，停一回合吧，老弟。")
                    self.stop = False
            else:
                print("你进牢了，老弟，停一回合吧。")
                self.lao = False

player_dir = {}
player_dir['red'] = Player(color="red", money=2500)
player_dir['blue'] = Player(color="blue", money=2500)
red = player_dir['red']
blue = player_dir['blue']
cnt = 0
while 1:
    print(f'\n-------第{cnt+1}轮--------\n')
    red.play(1)
    blue.play(1)
    cnt += 1
    input('输入任意键开启下一轮')

