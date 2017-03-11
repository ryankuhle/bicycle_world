
class Bicycle(object):
    """
    Bicycle instances define information about a bicycle model.
    """
    def __init__(self, model_name="", weight=0, production_cost=0):
        self.model_name = model_name
        self.weight = weight
        self.production_cost = production_cost
        
class BikeShop(object): # 1 bike shop with 6 bike models
    """
    BikeShop instances define information about individual bike shop.
    """
    def __init__(self, name="", model_types=0, markup=0, profit=0):
        self.name = name
        self.model_types = model_types
        self.markup = markup
        self.profit = profit

class Customer(object): # name, budget, whether or not they are allowed to purchase
    """
    Customer instances define information about an individual customer.
    """
    def __init__(self, name="", budget=0, status=True):
        self.name = name
        self.budget = budget
        self.status = status
        
        
# fire one instance of bike shops with 6 different models in stock, price should be 20% above  production cost

"""
# BIKESHOP INSTANCES
bikeshop1 = BikeShop()
bikeshop1.name = "Excite Bike"
bikeshop1.model_types = 6
bikeshop1.markup = 20 # Percentage based, markup on bike models production cost

# CUSTOMER INSTANCES
customer1 = Customer()
customer1.name = "Bobby"
customer1.budget = 200

customer2 = Customer()
customer2.name = "Reggie"
customer2.budget = 500

customer3 = Customer()
customer3.name = "Charlie"
customer3.budget = 1000
"""

if __name__ == "__main__":
    customer1 = Customer("Bobby", 200, True)
    print(customer1)

    
# Print the initial inventory of the bike shop for each bike it carries.
# Print the name of each customer, and a list of the bikes offered by the bike
# shop that they can afford given their budget. Make sure you price the bikes
# in such a way that each customer can afford at least one.

# Have each of the three customers purchase a bike then print the name of the
# bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.

# After each customer has purchased their bike, the script should print out
# the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
