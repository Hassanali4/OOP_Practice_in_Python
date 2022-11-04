import csv


class Item:
    # This is a class level attribute
    pay_rate = 0.8  # discount rate payable at 20% discount
    all = []

    def __init__(self, name, price, quantity=0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} should be equal to or greater then zero!"
        assert quantity >= 0, f"Quantity {quantity} should be equal to or greater then zero!"

        # Assigning to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_Discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_Increment(self,Increment_value):
        self.__price = self.__price + self.__price * Increment_value

    @property
    #property Decorator = Read-Only Attribute
    def name(self):
        #print("Your trying to get the value of name variable")
        return self.__name

    @name.setter
    def name(self,value):
        #print("Your trying to set the value of name variable")
        if len(value) > 10:
            raise Exception("The name of characters should not be longer them 10 characters")
        else:
            self.__name = value

    def calculate_the_total(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
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
            # We will count out the floats that are point zero
            # i.e 5.0 , 10.0
            return num.is_integer()
        elif isinstance(num, float):
            return True
        else:
            return False

    def __repr__(self):
        # return "Item"
        return f"{self.__class__.__name__}',('{self.name}','{self.__price}','{self.quantity}')"
