#!/usr/bin/env python3

# class CashRegister:
#   pass

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []


def add_item(self, title, price, quantity=1):
    item = {'title': title, 'price': price, 'quantity': quantity}
    self.items.append(item)
    self.total += price * quantity


def apply_discount(self):
    if self.discount > 0:
        self.total -= self.total * self.discount / 100
        return f'After the discount, the total comes to ${self.total:.2f}.'
    else:
        return 'There is no discount to apply.'


def item_names(self):
    return [item['title'] for item in self.items]


def void_last_transaction(self):
    if self.items:
        last_item = self.items.pop()
        self.total -= last_item['price'] * last_item['quantity']





