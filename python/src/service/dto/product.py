class Product():
    def __init__(self, model = None, grade = None, condition = None, storage = None, price = None, color = None):
        self.model = model
        self.grade = grade
        self.condition = condition
        self.storage = storage
        self.price = price
        self.color = color

    def __str__(self):
        return (f"Product(model={self.model!r}, "
                f"grade={self.grade!r}, condition={self.condition!r}, "
                f"storage={self.storage!r}, price={self.price!r}), color={self.color!r})")

    def __repr__(self):
        return self.__str__()