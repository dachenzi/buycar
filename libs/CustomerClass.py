import os
import sys
import json
import time
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
from conf import settings


class Customer(object):

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._history_list = []
        self._history_file = '{}/{}_history.txt'.format(settings.history_dir, self.name)

    def __str__(self):
        return self.name

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        if os.path.exists(self._history_file):
            self._history_list = json.load(open(self._history_file))
        return self._history_list

    @history.setter
    def history(self, data):
        self.history.append(data)
        json.dump(self._history_list, open(self._history_file, 'w'))

    def buy(self, goods_name, goods_price, goods_num):
        buy_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if self._balance < goods_price:
            return False
        else:
            self._balance -= int(goods_price)
            self.history = [buy_time, goods_name, goods_num, goods_price, self._balance]
            return True

    __repr__ = __str__

# a = Customer('daxin', 123)
# print(a.history)