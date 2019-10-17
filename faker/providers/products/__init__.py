from __future__ import unicode_literals

from .. import BaseProvider

class Provider(BaseProvider):

    material = (
        "Asbestos",
        "Aluminum",
        "Bronze",
        "Brass",
        "Steel", 
        "Wooden", 
        "Concrete", 
        "Plastic", 
        "Cotton", 
        "Granite", 
        "Rubber", 
        "Leather", 
        "Silk", 
        "Wool", 
        "Linen", 
        "Marble", 
        "Iron", 
        "Bronze", 
        "Copper", 
        "Aluminum", 
        "Paper"
    )

    adjective = (
        "Small"
        "Ergonomic"
        "Rustic"
        "Intelligent"
        "Gorgeous"
        "Incredible"
        "Fantastic"
        "Practical"
        "Sleek"
        "Awesome"
        "Enormous"
        "Mediocre"
        "Synergistic"
        "Heavy Duty"
        "Lightweight"
        "Aerodynamic"
        "Durable"
    )

    product = (
        "Chair"
        "Car"
        "Computer"
        "Gloves"
        "Pants"
        "Shirt"
        "Table"
        "Shoes"
        "Hat"
        "Plate"
        "Knife"
        "Bottle"
        "Coat"
        "Lamp"
        "Keyboard"
        "Bag"
        "Bench"
        "Clock"
        "Watch"
        "Wallet"
    )

    def product(self):
       """
       :example 'Simple Bronze Computer'
       """
       self.name = str(self.random_element(self.adjective)) + " " + str(self.random_element(self.material)) + " " + str(self.random_element(self.product))
       return self.name()
