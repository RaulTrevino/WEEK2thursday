class String:

    def __init__(self,):
        self.name = ""

    def get_string(self):
        self.name = input('what is your name? ').lower

    def print_string(self):
        print(self.name).upper()


string = String()
string.get_string()
string.print_string()
