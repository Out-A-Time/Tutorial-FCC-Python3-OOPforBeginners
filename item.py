import csv
import re

# PARENT CLASS


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than 0'
        assert quantity >= 0, f'Quantity {quantity} is not greater than 0'

        # Assign to self object
        self.__name = name  # __ means private, _ means visible in other files
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute encapsulation
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Helps display and identify all intances print(Item.all)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smpt_server):  # SIMULATION of Abstracion Principle
        pass

    def __prepare_body(self):  # SIMULATION  of Abstracion Principle
        return f"""
        Hello Stranger.
        we have {self.name} {self.quantity} times.
         """

    def __send(self):  # SIMULATION  of Abstracion Principle
        pass

    def send_email(self):  # SIMULATION  of Abstracion Principle
        self.__connect('')
        self.__prepare_body()
        self.__send()


Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.0))
