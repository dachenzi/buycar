import os
import sys
import json
import time
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
from conf import settings


def login_menu():
    """
    login menu,Collect user input information
    :return:Username and Password
    """

    while True:
        print('--------> Login Page <---------')
        username = input('Username: ').strip()
        if not username:
            print('\033[31mError,You must input Username !\033[0m')
            time.sleep(1)
            continue
        password = input('Password: ').strip()
        if not password:
            print('\033[31mPassword not None !\033[0m')
            time.sleep(1)
            continue
        break
    return username, password


def goods_menu():
    goods_index = []
    goods_list = json.load(open(settings.goods_file))
    print('*'*10, '购物商城', '*'*10)
    for index, value in enumerate(goods_list):
        goods_index.append((index,value))
        print('商品编号:{} \t 商品名称:{} \t ￥{}'.format(index, value['name'], value['price']))
    user_choice = input('请输入要购买的序号 (按q推出) >>:')
    if user_choice.isdigit() and int(user_choice) <= len(goods_index) - 1:
        user_choice = int(user_choice)
        return goods_index[user_choice][-1]
    elif user_choice == 'q':
        return 'quit'
    else:
        print('\033[31m输入有误，请重新输入\033[0m')


def main_menu(username):
    user_func = {
        '1': 'history',
        '2': 'get_balance',
        '3': 'goods_menu',
        '4': 'quit'
    }
    while True:
        print('''
--------> [  \033[34m{}\033[0m  ] <--------
    1. 查看购物记录
    2. 查看账户余额
    3. 购物商城
    4. 退出
        '''.format(username))
        user_input = input('选择>>: ').strip()
        if user_input in user_func.keys():
            return user_func[user_input]
        else:
            print('\033[31m输入错误，请重新输入\033[0m')
