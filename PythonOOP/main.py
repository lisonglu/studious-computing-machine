from phone import Phone
from item import Item
from keyboard import Keyboard

item1 = Item("MyItem", 750)


item1.read_only_name = "OtherItem"
print(item1.read_only_name)

item1.apply_discount()
item1.apply_increment(0.2)
print(item1.read_only_price)

item3 = Phone("Myphone", 1000, 3)
item3.send_email()
item3.apply_increment(0.2)
print(item3.read_only_price)
item3.apply_discount()
print(item3.read_only_price)

item4 = Keyboard("jsckeyboard", 1000, 3)
item4.apply_discount()
print(item4.read_only_price)
