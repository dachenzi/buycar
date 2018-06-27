import os
import sys
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
from conf import settings
from libs import menus
from libs import CustomerClass
from libs import tools


def get_user_list():
    """
    获取系统用户列表
    :return:  返回用户列表
    """
    user_list = []
    with open(settings.account_list_file) as f:
        for line in f:
            user_list.append(line.strip())
    return user_list


def super_market(customer_obj):
    """
    购物超市
    :param customer_obj: 用户
    :return:
    """
    flag = True
    while flag:
        result = menus.goods_menu()
        if isinstance(result, dict):
            if customer_obj.buy(result['name'], int(result['price']), 1):
                print('购买 [ \033[36m{}\033[0m ] 成功，您的可用余额为：[ \033[35m{}\033[0m ]'.format(result['name'], customer.balance))
            else:
                print('余额不足，请尽快充值')
        elif result == 'quit':
            break


if __name__ == '__main__':
    while True:
        user_name, user_pass = menus.login_menu()
        if user_name in get_user_list():
            customer = CustomerClass.Customer(user_name)
            customer_password = tools.get_password_md5(user_pass)
            if customer.auth(customer_password):
                while True:
                    if customer.balance == 'None':
                        user_salary = input('\033[31m请输入您的工资：\033[0m')
                        if user_salary.isdigit():
                            customer.balance = int(user_salary)
                        else:
                            print('\033[31m请输入数字,谢谢\033[0m')
                    choice_func = menus.main_menu(customer.name)
                    if choice_func == 'quit':
                        customer.save_balance()
                        sys.exit('欢迎下次光临')
                    elif choice_func == 'goods_menu':
                        super_market(customer)
                    else:
                        getattr(customer, choice_func)
            else:
                print('\033[31m密码错误，请重新输入\033[0m')
        else:
            print('账户 [ \033[31m{}\033[0m ] 不存在，请重新输入'.format(user_name))
