import os
import sys
import json
import time
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]))
from conf import settings


def menu():
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
        {"name": "咖啡", "price": 32},
        {"name": "口香糖", "price": 1.5},
        {"name": "苹果", "price": 3},
    ]
    return json.load(open(settings.goods_file))

print(menu())
#
# for menu_dic in menu():
#     print(menu_dic)
