

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'money': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_rem(self):
        print("""
The coffee machine has: 
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{cups} disposable cups
${money} of money""".format(water=self.water, milk=self.milk, beans=self.beans, cups=self.cups, money=self.money))

    def capacity(self, coffee):
        flag = True
        if self.cups < 1:
            print("Not enough cups")
            flag = False
        if self.water < coffee.get("water"):
            print("Not enough water")
            flag = False
        if self.milk < coffee.get("milk"):
            print("Not enough milk")
            flag = False
        if self.beans < coffee.get("beans"):
            print("Not enough beans")
            flag = False
        return flag

    def buy(self):
        slection = input("""\n
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n""")

        if slection == "1":
            if self.capacity(espresso):
                self.serve(espresso)
        elif slection == "2":
            if self.capacity(latte):
                self.serve(latte)
        elif slection == "3":
            if self.capacity(cappuccino):
                self.serve(cappuccino)
        elif slection == "back":
            print("Going back to main menu")
        else:
            print("Wrong selection, Try again!")

    def serve(self, coffee):
        print("""
            Starting to make a coffee
            Grinding coffee beans
            Boiling water
            Mixing boiled water with crushed coffee beans
            Pouring coffee into the cup
            Pouring some milk into the cup
            Coffee is ready!
            """)

        self.cups = self.cups - 1
        self.money = self.money + coffee.get("money")
        self.water = self.water - coffee.get("water")
        self.milk = self.milk - coffee.get("milk")
        self.beans = self.beans - coffee.get("beans")

    def fill(self):
        water_added = int(input("Write how many ml of water you want to add: "))
        milk_added = int(input("Write how many ml of milk you want to add: "))
        beans_added = int(input("Write how many grams of coffee beans you want to add: "))
        cups_added = int(input("Write how many disposable cups you want to add: "))

        self.cups += cups_added
        self.water += water_added
        self.milk += milk_added
        self.beans += beans_added

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


def machine():
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    action = input("Write action (buy, fill, take, remaining, exit): \n")

    while action != "exit":
        if action == "buy":
            coffee_machine.buy()

        elif action == "fill":
            coffee_machine.fill()

        elif action == "take":
            coffee_machine.take()

        elif action == "remaining":
            coffee_machine.print_rem()
        else:
            print("Incorrect statement")

        action = input("\nWrite action (buy, fill, take, remaining, exit): \n")


machine()
