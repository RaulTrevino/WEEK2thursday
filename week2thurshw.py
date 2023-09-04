class ShoppingList:

    def __init__(self):
        self.grocery_list = {}

    def choices(self):
        while True:
            self.user_input = input(f"Do you want to [a]dd, [v]iew, [r]emove, or [q]uit? ")
            if self.user_input == 'a':
                item = input('What do you want to add? ')
                quantity = int(input('How Many? '))
                self.grocery_list[item] = quantity
            elif self.user_input == "r":
                del_item = input("Enter item name to delete: ")
                del self.grocery_list[del_item]
            elif self.user_input == "v":
                print(self.grocery_list)

            else:
                self.user_input == "q"
                print('Goodbye')
                if self.user_input.lower() == "quit":
                    break



shopping_list = ShoppingList()


shopping_list.choices()
