#  A hotel has N number of rooms. Create a list of rooms in the hotel such that
#  Each room in your rooms list needs to contain at least 5 items and the relative dollar value of each item.
#  It should provide us with an interactive command prompt based shell with the following menu.
#  1. Add a hotel
#  2. Add a room to the hotel with any of the 5 items.
#  3. Print out each room along with the individual items and values. This needs to be properly formatted.
#  4. Accept a budget from the user in $ and list only those rooms which will cost less than or equal to his budget.

class room:
    def __init__(self, name, item_list):
        self.name = name
        self.item_list = item_list
        self.ac = 10
        self.fridge = 10
        self.bed = 5
        self.fan = 2
        self.geyser = 5
        self.sofa = 10
        self.tv = 10
        self.light = 2
        self.total = 0
        self.amount = 0

    def calculate_amount(self, item_list=None):
        if item_list == None:
            item_list = self.item_list
        for i in item_list:
            if i == 'ac':
                self.total = self.total + self.ac
            if i == 'fridge':
                self.total = self.total + self.fridge
            if i == 'bed':
                self.total = self.total + self.bed
            if i == 'fan':
                self.total = self.total + self.fan
            if i == 'geyser':
                self.total = self.total + self.geyser
            if i == 'sofa':
                self.total = self.total + self.sofa
            if i == 'tv':
                self.total = self.total + self.tv
            if i == 'light':
                self.total = self.total + self.light
        return self.total

    def print_room(self):
        self.amount = self.calculate_amount()
        print('The amount for the ' + str(self.name) + ' room you have opted is $' + str(
            self.amount) + ' with the following items ' + str(self.item_list))


class hotel(room):
    def __init__(self):
        self.name = input("Enter a hotel name: ")
        print()
        self.room_count = 0
        self.rooms = []
        while True:
            if self.room_count > 0:
                add_more_room = input("Do you want to add one more room? yes/no: ")
                lower_add_room = add_more_room.lower()
                while True:
                    if lower_add_room == 'yes':
                        break
                    elif lower_add_room == 'no':
                        break
                    else:
                        lower_add_room = input("enter a valid answer: ")
                if lower_add_room == 'no':
                    break
            room_name = input('Enter a room name under \"' + self.name.capitalize() + '\" hotel: ')
            print()
            print('You can select ' + str(room_name.capitalize()) + ' with any of the items below (5 or more items)')
            print("AC - $10, Fridge - $10, Bed - $5, Fan - $2, Geyser - $5, Sofa - $10, TV - $10, Light -$2 ")
            print("<---- You can type only the name of the items with spaces in between and can add same item multiple times ---->")
            print()
            input_string = input()
            item_list = input_string.split()
            while True:
                if len(item_list) >= 5:
                    break
                again_input = input("Please add at least " + str(5 - len(item_list)) + " more items: ")
                input_string = input_string + ' ' + again_input
                item_list = input_string.split()
            lower_item_list = []
            for i in item_list:
                item = i.lower()
                lower_item_list.append(item)
            self.rooms.append(room(room_name, lower_item_list))
            self.room_count += 1
        for i in range(self.room_count):
            self.rooms[i].print_room()
        print()
        need_budget = input("Do you need budget help from our side? yes/no: ")
        lower_need_budget = need_budget.lower()
        while True:
            if lower_need_budget == 'yes':
                break
            elif lower_need_budget == 'no':
                break
            else:
                lower_need_budget = input("enter a valid answer: ")
        if lower_need_budget == 'yes':
            budget = int(input("Enter the budget of your choice: "))
            budget_rooms = False
            print('-----------------------------------------------------------------------------')
            between = " " * 10
            print('{between}Rooms under your budget{between}Price in ${between}'.format(between=between))
            for i in range(self.room_count):
                if self.rooms[i].amount <= budget:
                    budget_rooms = True
                    print('{between}{room:<{room_width}}{between}{price:>{price_width}}{between}'.format(
                        room=self.rooms[i].name.capitalize(), room_width=len('Rooms under your budget'),
                        between=between, price=self.rooms[i].amount, price_width=len('Price in $')))
            print('-----------------------------------------------------------------------------')
            if budget_rooms is False:
                print("Sorry you didn't add rooms in your budget! Thanks for choosing " + str(self.name.capitalize()))
            if budget_rooms is True:
                print("You can select any of the rooms listed above, Thank you for selecting " + str(
                    self.name.capitalize()))
        if lower_need_budget == 'no':
            print(
                "You can select any of the rooms listed above, Thank you for selecting " + str(self.name.capitalize()))


hotel_1 = hotel()
input("Press enter to exit ")
