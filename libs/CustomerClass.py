import os
import sys
import json
import time
import configparser
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
from conf import settings


class Customer(object):
    """
    用户类
    """

    def __init__(self, name):
        self.name = name
        self._history_list = []
        self._history_file = '{}/{}_history.txt'.format(settings.history_dir, self.name)
        self._account_file = '{}/{}.db'.format(settings.account_dir, self.name)
        self._get_account_balance()
        self._get_account_password()

    def __str__(self):
        return self.name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, user_salary):
        self._balance = user_salary

    @property
    def get_balance(self):
        print('您的余额为：\033[32m{}\033[0m'.format(self._balance))
        return None

    @property
    def history(self):
        if os.path.exists(self._history_file):
            self._history_list = json.load(open(self._history_file))
        if self._history_list:
            for buy_time, goods_name, goods_num, goods_price, user_balance in self._history_list:
                print(
                    "{} 商品名称：{}  单位:{}  总价:{} 余额:{}".format(buy_time, goods_name, goods_num, goods_price, user_balance)
                )
        else:
            print('您的购物车为空！')
        return None

    @history.setter
    def history(self, data):
        """
        持久化保存用户的购买记录
        :param data: 购买信息的列表 buy_time, goods_name, goods_num, goods_price, self._balance
        :return: None
        """
        self._history_list.append(data)
        json.dump(self._history_list, open(self._history_file, 'w'))

    def buy(self, goods_name, goods_price, goods_num):
        """
        用户买东西
        :param goods_name: 商品名称
        :param goods_price: 商品价格
        :param goods_num: 商品数量
        :return: 购买结果
        """
        buy_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if self._balance < goods_price:
            return False
        else:
            self._balance -= int(goods_price)
            self.history = [buy_time, goods_name, goods_num, goods_price, self._balance]
            return True

    def _get_account_password(self):
        cp = configparser.ConfigParser(allow_no_value=True)
        cp.read(self._account_file)
        self._password = cp['account_info'].get('password')
        return self._password

    def _get_account_balance(self):
        cp = configparser.ConfigParser(allow_no_value=True)
        cp.read(self._account_file)
        self._cp = cp
        self._balance = cp['account_info'].get('balance')
        if self._balance.isdigit():
            self._balance = int(self._balance)
        return self._balance

    def auth(self, account_password):
        """
        用户登录验证
        :param account_password: 加密后的密码
        :return: 验证结果
        """
        password = self._get_account_password()
        if password == account_password:
            return True
        return False

    def save_balance(self):
        """
        退出时保存用户余额
        :return: None
        """
        with open(self._account_file, 'w') as f:
            self._cp.set('account_info', 'balance', str(self._balance))
            self._cp.write(f)

    __repr__ = __str__

