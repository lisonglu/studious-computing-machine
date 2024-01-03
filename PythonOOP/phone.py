from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # use a super function to access attributes/methods from parent class it inherits from
        super().__init__(name, price, quantity)
        assert (
            broken_phones >= 0
        ), f"Broken_phones {broken_phones} is not greater or equal to zero!"

        # assign to self object
        self.broken_phones = (
            broken_phones,
            f"Broken Phones {broken_phones} is not greater or equal to zero!",
        )
