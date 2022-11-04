from Item import Item


class Phone(Item):
    all = []
    def __init__(self, name, price, quantity=0,broken_phones=0):
        # Call to super function to access all the attributes / methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to the recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} should be equal to or greater then zero!"

        # Assigning to self object
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)
