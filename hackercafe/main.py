#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Made by HackerEarth with <3
"""

import sys
import uuid


DEFAULT_MSG_TEMPLATE = """
No Options Given
Use the following options:
    1. order - To order an item in the menu
    2. menu  - To list the menu
"""


INCORRECT_MSG_TEMPLATE = """
Incorrect Option Given
Use the following options:
    1. order - To order an item in the menu
    2. menu  - To list the menu
"""

INCORRECT_ITEM_TEMPLATE = """
Incorrect Item Given
Following products are available in HackerCafe:
    Item Code - Item Name
    -----------------------
    1. HBC  - Bit Coffee
    2. HBYC - Byte Coffee
    3. HDS  - Dijkstra Sandwich
    4. HBP  - Babbage Pasta
    5. HTC  - Time Capsule
    6. HJSN - XML Salad
    7. HCB  - Chill Bill
    8. HZB  - Zuck-Burg
    9. HAJ  - Aj-eggs
"""

NO_ITEMS_TEMPLATE = """
No Item Given
Following products are available in HackerCafe:
    Item Code - Item Name
    -----------------------
    1. HBC  - Bit Coffee
    2. HBYC - Byte Coffee
    3. HDS  - Dijkstra Sandwich
    4. HBP  - Babbage Pasta
    5. HTC  - Time Capsule
    6. HJSN - XML Salad
    7. HCB  - Chill Bill
    8. HZB  - Zuck-Burg
    9. HAJ  - Aj-eggs
"""

AVAILABLE_CODES = [
    "HBC",
    "HBYC",
    "HDS",
    "HZB",
    "HBP",
    "HTC",
    "HAJ",
    "HZB",
    "HCB",
]

HELP_TEMPLATE = """
HackerCafe is a place for hackers, by hackers, from HackerEarth Inc.

Hackers want easy access to the internet and an environment they love.
They want food which allows them to be awake at night and helps code
better and faster. The food at HackerCafe is low-carb, high on protein
with right amount of Aspartic & Glutamic acid. It is the result of 3 years
of research by the best nutritionists in the world.

Available Commands:
    1. menu - List the menu and item codes to order.
    2. order - To order the item and send it to our servers

Available Foods:
    Item Name - Item Code
    ----------------------
    1. Bit Coffee (8 beans of pure, intense coffee flavour)          - HBC
    2. Byte Coffee (16 beans with steamed milk & deep layer of foam) - HBYC
    3. Dijkstra Sandwich (Shortest sandwich)                         - HDS
    4. Babbage Pasta (Father of the pasta)                           - HBP
    5. Time capsule (Keeps you awake till whenever you want)         - HTC
    6. XML Salad (Messed-up salad)                                   - HJSN
    7. Aj-eggs (The refreshing omlette)                              - HAJ
    8. Chill Bill (Opens your mind windows)                          - HCB
    9. Zuck-Burg (The social burger)                                 - HZB
"""


class HackerCafe(object):
    ITEMS = [
        ("Bit Coffee", "HBC"),
        ("Byte Coffee", "HBYC"),
        ("Djikstra Sandwich", "HDS"),
        ("Babbage Pasta", "HBP"),
        ("Time Capsule", "HTC"),
        ("XML Salad", "HJSN"),
        ("Aj-eggs", "HAJ"),
        ("Chill Bill", "HCB"),
        ("Zuck-Burg", "HZB"),
    ]

    @classmethod
    def list_orders(cls):
        print "Following Products are available to order \n"
        for item, item_code in cls.ITEMS:
            print """
            {item} - {item_code}
            """.format(item=item, item_code=item_code).strip()
        print "\n\nPlease Order any of these"
        return

    @classmethod
    def order_item(cls, user_code):
        item_codes = map(lambda d: d[1], cls.ITEMS)
        if user_code.upper() not in item_codes:
            print "Please order what we are offering"
            return
        msg = """
        Order is in pipeline. Consumers allocated. ORDER ID: {o_id}.
        """
        print msg.format(o_id=cls.generate_hex_id()).strip()
        print "Estimated Delivery Time is - log2(2016)."
        print "-----------------------------------------\n"
        print "Remote Orders are not accepted. Your order will be delivered only if you are in HackerCafe."

    @staticmethod
    def generate_hex_id():
        uid = uuid.uuid4()
        uid = uid.get_hex()[:5]
        return "0x"+uid

AVAILABLE_CMDS = {
    "order": HackerCafe.order_item,
    "menu": HackerCafe.list_orders,
    "help": "",
}


def main():
    args = sys.argv
    if len(args) < 2:
        print HELP_TEMPLATE.strip()
        return
    cmd = args[1]
    cmd = cmd.lower()
    if cmd not in AVAILABLE_CMDS.keys():
        print INCORRECT_MSG_TEMPLATE.strip()
        return
    if cmd == 'order':
        if len(args) < 3:
            print NO_ITEMS_TEMPLATE.strip()
            return
        item = args[2]
        if item.upper() not in AVAILABLE_CODES:
            print INCORRECT_ITEM_TEMPLATE.strip()
            return
        func = AVAILABLE_CMDS[cmd]
        func(item)
    elif cmd == 'menu':
        func = AVAILABLE_CMDS[cmd]
        func()
    elif cmd == 'help':
        print HELP_TEMPLATE.strip()
        return


if __name__ == '__main__':
    main()
