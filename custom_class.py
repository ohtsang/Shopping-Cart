'''
Owen Tsang
Assignment 10.1 Your Own Class
This code will involve me implementing my own class of a real world item
'''
class DrinksShoppingCart:
    #Sets base cart with 1 drink and flavor
    def __init__(self, drink, flavor):
        self.drink = drink
        self.flavor = flavor
        self.count = 2
        for x in range(0, 1):
            self.cart = {"Drink 1":self.drink, "Flavor for drink 1":self.flavor}

    #Returns current shopping cart
    def get_cart(self):
        return self.cart

    #Returns the flavor of the corresponding drink
    def get_flavor(self, flavor_num):
        flavor_num = str(flavor_num)
        placeholder = "Flavor for drink " + flavor_num
        return self.cart[placeholder]
    
    #Returns the drink of the corresponding drink number
    def get_drink(self, drink_num):
        drink_num = str(drink_num)
        placeholder = "Drink " + drink_num
        return self.cart[placeholder]

    #Changes drink and its flavor
    def change_drink_and_flavor(self, drink_num, new_drink,new_flavor):
        #Turns number into string 
        drink_num = str(drink_num)
        placeholder = "Drink " + drink_num
        #Changing drink
        self.cart[placeholder] = new_drink
        placeholder = "Flavor for drink " + drink_num
        #Changing flavor
        self.cart[placeholder] = new_flavor

    #Adds a new drink and flavor
    def add_drink_and_flavor(self, drink, flavor): 
        while True:
            self.count = str(self.count)
            #Adding a drink
            self.cart["Drink " + self.count] = drink
            self.count = int(self.count)
            self.count = str(self.count)
            #Adding a flavor
            self.cart["Flavor for drink " + self.count] = flavor
            self.count = int(self.count)
            #Counting the amount of drinks
            self.count += 1
            break

    #Removes an unwanted drink and its corresponding flavor
    def remove_drink(self, drink_num):
        drink_num = str(drink_num)
        del self.cart["Drink " + drink_num]
        del self.cart["Flavor for drink " + drink_num]

#DEMO PROGRAM
def main():
    #Sets the base shopping cart with one drink and a flavor
    print("Welcome to the shopping cart. Please add choose one drink and the flavor and put exit for both prompts if you are done.")
    while True:
        drink_command = input ("Please enter your drink here: ")
        flavor_command = input("Please enter the flavor of your drink here: ")
        if drink_command and flavor_command == "exit":
            print("Thanks for trying out my shopping cart!")
            break 
        else:
            cart = DrinksShoppingCart(drink_command, flavor_command)
            print("Below is what you currently have")
            print(cart.get_cart())
            break
    #Lets the user do whatever he/she wants
    print("Now you can do you following just type what is printed and follow the instructions: add to cart, change drink, check drink, check flavor, remove drink, exit")
    while True:
        command = input("What would you like to do? ")
        #Adding to cart
        if command == "add to cart":
            drink_command = input ("Please enter your drink here: ")
            flavor_command = input("Please enter the flavor of your drink here: ")
            cart.add_drink_and_flavor(drink_command, flavor_command)
            print(cart.get_cart())
        #Changing a drink
        if command == "change drink":
            print("Your current cart is below")
            print(cart.get_cart())
            drink_num_command = input("Which drink would you like to change(input drink number) ")
            drink_command = input("What drink would you like to replace it with? ")
            flavor_command = input("Which new flavor would you like with this drink? ")
            cart.change_drink_and_flavor(drink_num_command, drink_command, flavor_command)
            print("Your new cart is below")
            print(cart.get_cart())
        #Checking a drink
        if command == "check drink":
            drink_command = input("Which drink number would you like to check? ")
            print(cart.get_drink(drink_command))
        #Checking a flavor
        if command == "check flavor":
            flavor_command = input("Which flavor number would you like to check? ")
            print(cart.get_flavor(flavor_command))
        #Removing a drink
        if command == "remove drink":
            print("Your current cart is below")
            print(cart.get_cart())
            drink_command = input("Which drink would you like to remove?(Please input the drink number) ")
            cart.remove_drink(drink_command)
            print("Your new cart is below")
            print(cart.get_cart())
        #Exit
        if command == "exit":
            print("Thanks for using my shopping cart!")
            break

if __name__ == "__main__":
    main()
