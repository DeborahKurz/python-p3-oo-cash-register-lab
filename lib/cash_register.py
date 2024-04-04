#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.quantity = 0
    self.last_item = ""
    self.last_price = 0
    self.last_quantity = 0

  def add_item(self, item, price, quantity = 1):
    for an_item in range(quantity):
      self.items.append(item)
      self.last_item = item
      self.last_price = price
      self.last_quantity = quantity
    self.total += quantity * price
    return self.items

  def apply_discount(self):
    if self.discount >= 1:
      percent = 100 - self.discount
      opposite_percent = percent * .01
      self.total = opposite_percent * self.total
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - (self.last_price * self.last_quantity)
    self.items.pop(-self.last_quantity)
    if len(self.items) == 0:
      self.total = 0.0
    else:
      return self.total