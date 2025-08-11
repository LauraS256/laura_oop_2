# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self,price):
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker

    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
class Bond(Asset):
    def __init__(self, price, description, duration, interest):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.interest = interest

    def get_description(self):
        return f"{self.bondname}: {self.duration} : ${self.price} : {self.interest}% "

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())

