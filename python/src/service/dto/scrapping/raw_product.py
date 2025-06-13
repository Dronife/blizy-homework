class RawProduct:
    def __init__(self, headline_string = None, price_string = None):
        self.headline_string = headline_string
        self.price_string = price_string

    def __str__(self):
        return f"Product(headline_string={self.headline_string!r}, price_string={self.price_string!r}"

    def __repr__(self):
        return self.__str__()