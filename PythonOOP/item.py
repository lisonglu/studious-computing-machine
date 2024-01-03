import csv


# create a class:
class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # self is a keyword that’s used to access an instance method, which retrieves all the attributes of a class.
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # assign to self object
        self.__name = name  # private attribute
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    @property
    def read_only_price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def read_only_name(self):
        return self.__name

    @read_only_name.setter
    def read_only_name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    # classmethod are used to manipulate different structures of data to instantiate objects,
    # pass the object reference as the first argument in the background
    def instantiate_from_csv(cls):
        # cls is a keyword that’s used to access a class method, which is a code template for creating objects
        with open("PythonLib/PythonOOP/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    # this should do something that has a relationship with the class, but not something that must be unique per instance
    # never send the object as the first argument, it is like a regular function that just receives parameters like isolated functions
    def is_integer(num):
        # count out the floats that are point zero, for i,e: 5.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # create magic method to represent these object
    def __repr__(self):
        # {self.__class__.__name__} is to call the class 'Item' generically
        return f"{self.__class__.__name__}('{self.read_only_name}','{self.__price}','{self.quantity}')"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""Hello xxx. We have {self.read_only_name} {self.quantity} times."""

    def __send(self):
        pass

    def send_email(self):
        self.__connect(" ")
        self.__prepare_body()
        self.__send()
