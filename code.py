
class Bicycle():
    """
    Bicycle instances define information about a bicycle model.
    """
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __repr__(self):
        """Return string representation of Bicycle object.
        Includes the name of the class (Bicycle), the model, the weight, and the cost
        """
        return "%s(model=%r, weight=%r, cost=%r)" % (self.__class__.__name__, self.model, self.weight, self.cost)        
        
class BikeShop():
    """
    BikeShop instances define information about individual bike shop.
    """
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.markup = 0.2
        self.store_profit = 0
        
    def set_inventory(self, bike_name):
        self.inventory.append(bike_name)

    def show_inventory(self):
        return self.inventory

    def calc_profit(self, selected_bike):
        self.sel_bike = self.inventory[selected_bike]
        self.store_profit += self.sel_bike.cost * self.markup
        return self.store_profit

    def sell_bike(self, choice):
        self.selection = self.inventory.pop(choice)
        return self.selection        

class Customer():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bike_list = []

    def bikes_avail(self, bike):
        if bike.cost <= self.money:
            self.bike_list.append(bike.model)

    def show_bikes_avail(self):
        return self.bike_list

    def purchase(self):
        self.bike_choice = input("Which would you like to purchase? ")
        if self.bike_choice == "Corvair":
            self.selected_bike = 0
        elif self.bike_choice == "Airstream":
            self.selected_bike = 1
        elif self.bike_choice == "Slipstream":
            self.selected_bike = 2
        elif self.bike_choice == "Monty":
            self.selected_bike = 3
        elif self.bike_choice == "Zuul":
            self.selected_bike = 4
        elif self.bike_choice == "Ratman":
            self.selected_bike = 5
        else:
            print ("You gave an invalid selection")
            
        shop.calc_profit(self.selected_bike)

        self.sold_bike = shop.sell_bike(self.selected_bike)
        print(self.sold_bike)
        print("Money left in pocket: $" + str(self.money - self.sold_bike.cost))
        
if __name__ == "__main__":
    dan = Customer("dan", 200)
    jessie = Customer("jessie", 500)
    brock = Customer("brock", 1000)

    shop = BikeShop("Blannigan's Bikes")

    bike1 = Bicycle("Corvair", 20, 150)
    bike2 = Bicycle("Airstream", 18, 200)
    bike3 = Bicycle("Slipstream", 25, 100)
    bike4 = Bicycle("Monty", 16, 400)
    bike5 = Bicycle("Zuul", 10, 800)
    bike6 = Bicycle("Ratman", 13, 650)

    shop.set_inventory(bike1)
    shop.set_inventory(bike2)
    shop.set_inventory(bike3)
    shop.set_inventory(bike4)
    shop.set_inventory(bike5)
    shop.set_inventory(bike6)

    print(shop.name)
    print(shop.show_inventory())

    print("Dan's budget = $%f" % dan.money)
    for bike in shop.show_inventory():
        dan.bikes_avail(bike)
    print(dan.show_bikes_avail())
    dan.purchase()
    print(shop.show_inventory())
    print(shop.store_profit)

    print("Jessie's budget = $%f" % jessie.money)
    for bike in shop.show_inventory():
        jessie.bikes_avail(bike)
    print(jessie.show_bikes_avail())
    jessie.purchase()
    print(shop.show_inventory())
    print(shop.store_profit)
    
    print("Brock's budget = $%f" % brock.money)
    for bike in shop.show_inventory():
        brock.bikes_avail(bike)
    print(brock.show_bikes_avail())
    brock.purchase()
    print(shop.show_inventory())
    print(shop.store_profit)        