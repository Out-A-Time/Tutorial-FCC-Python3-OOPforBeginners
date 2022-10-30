from item import Item


# CHILD CLASS - Inheritance
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        assert broken_phones >= 0, f'Broken phones {quantity} is not greater than 0'

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Item('Motorola Z8', 500, 5)
print(phone1.calculate_total_price())
print(Phone.all)
