class MenuItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        self.total_price = self.calculate_total_price()
        

    def calculate_total_price(self):
        return self.price


class Beverage(MenuItem):
    def __init__(self, name: str, price: int, alcohol: bool):
        super().__init__(name, price,)
        self.alcohol = alcohol
        


class Appetizer(MenuItem):
    def __init__(self, name: str, price: int,origin: str):
        super().__init__(name, price,)
        self.origin = origin
        


class MainCourse(MenuItem):
    def __init__(self, name: str, price: int, vegan: bool):
        super().__init__(name, price,)
        self.vegan = vegan
        


class Dessert(MenuItem):
    def __init__(self, name: str, price: int, kind: str):
        super().__init__(name, price,)
        self.kind = kind
        



class Order:
    def __init__(self, Menu_items:list):
        self.Menu_items = Menu_items


    def add_items(self, new_food:list):
        self.new_food = new_food
        for i in self.new_food:
            self.Menu_items.append(i)


        

    def calculate_total_bill(self):
        total_money = []
        for i in self.Menu_items:
            total_money.append(i.total_price)
        return sum(total_money)


    def calculate_discounts(self):
        self.total_discount = self.calculate_total_bill()
        if len(self.Menu_items) > 5:
            return (self.total_discount - self.total_discount*0.05)
        else:
            return (self.total_discount)



if __name__ == "__main__":
    

    lemonade = Beverage(name="Lemonade", price=2000, alcohol=False)
    beer = Beverage(name="Beer", price=3000, alcohol=False)
    water = Beverage(name="Water", price=1000, alcohol=False)


    empanada = Appetizer(name="Lemonade", price=1500, origin="Colombia")
    arepa = Appetizer(name="Lemonade", price=2200, origin="Venezuela")
    


    chinese_rise = MainCourse(name="Chinese rise", price=20000, vegan=False)
    hamburger = MainCourse(name="Hamburger", price=25000, vegan=False)
    vegan_hamburger = MainCourse(name="Vegan_hambuerger", price=30000, vegan=True)



    ice_cream = Dessert(name="orange ice cream", price=3000, kind="Ice Cream")
    candys = Dessert(name="sweet mind", price=500, kind="Candy")
    cake = Dessert(name="Banana Cake", price=4500, kind="Cake")

    print("Menu")
    print("lemonade, water, beer, empanada, arepa, chinese rise, hamburger, vegan hamburger, Banana Cake, sweet mind, orange ice cream")

    print("So, you want a cake, a empanada, a water and a hamburger")

    First_order: Order = Order([cake, empanada, water, hamburger])

    start = True
    new_food = []
    while start or mores_food:
        start = False
        more_food: str = input("Would you like more food, yes or no?\n" )
        if more_food == "yes":
            mores_food = True
            food = input("Which one?: ")
            match food:
                case "lemonade": 
                    wished_food = lemonade
                case "beer":
                    wished_food = beer
                case "water":
                    wished_food= water
                case "arepa": 
                    wished_food = arepa
                case "empanada":
                    wished_food = empanada
                case "chinise rise":
                    wished_food= chinese_rise
                case "hamburger": 
                    wished_food = hamburger
                case "vegan hamburger":
                    wished_food = vegan_hamburger
                case "orange ice cream":
                    wished_food= ice_cream
                case "Banana Cake":
                    wished_food = cake
                case "sweet mind":
                    wished_food= candys
            new_food.append(wished_food)
        else:
            mores_food = False
        

    First_order.add_items(new_food=new_food)
        



    print("Your bill without discount is: ",First_order.calculate_total_bill())
    print("your bill with discounts is: ", First_order.calculate_discounts())








