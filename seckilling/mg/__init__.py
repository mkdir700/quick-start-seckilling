# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 14:03
# @Author  : CRJ
# @File    : __init__.py
# @Software: PyCharm
# @Python3.6
import threading

from .order_consume import start_order_consume
from .overtime_consume import start_overtime_consume
from .paid_consume import start_paid_consume


def start_consume(goods_id):
    t1 = threading.Thread(target=start_order_consume, args=(goods_id,), daemon=True)
    t2 = threading.Thread(target=start_overtime_consume, daemon=True)
    t3 = threading.Thread(target=start_paid_consume, args=(goods_id,), daemon=True)
    t1.start()
    t2.start()
    t3.start()
