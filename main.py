from item import Item
from phone import Phone


Item.instantiate_from_csv()


item1 = Item('MyItem', 750)
print(Item.all)

# Setting an Attribute
item1.name = "Other Item"  # overwriting
item1.apply_increment(0.2)

# Getting an Attribute
print(item1.name)
print(item1.price)

item1.co
