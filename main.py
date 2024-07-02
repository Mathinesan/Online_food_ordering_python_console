class Food:

    def user(self, name, ph_num):
        name = input("Enter your name: ")
        while True:
            ph_num = input("Enter your mobile number: ")
            if len(ph_num) == 10 and ph_num.isdigit():
                break
            else:
                print("Invalid phone number. Please enter a 10-digit number.")

        print("User Details")
        print("Name:", name)
        print("Mobile Number:", ph_num)

    def city(self,citi):
        citi = {
            1 : "Erode",
            2 : "Coimbatore",
            3 : "Salem",
            4 : "Namakkal"
        }
        print("Choose your city.")
        print(citi)
        chosen_citi = int(input())
        if chosen_citi == 1:
            print(citi[1])
        elif chosen_citi == 2:
            print(citi[2])
        elif chosen_citi == 3:
            print(citi[3])
        elif chosen_citi == 4:
            print(citi[4])
        else:
            print("Invalid input!")


    def Restaurants(self):
        hotel = {
            "Erode" : ["Vadakku Restaurant", "Kongu Parotta", "Taj Hotels"],
            "Coimbatore" : ["Dosa & Drama", "Arabian cuisine", "Mc Donald's"]
            "Salem" : ["H for Hitler", "Pizza Hut", "Steaks and Streaks"]
            "Namakkal" : ["Oscar kudra trumpeh", "Burger King", "A2B"]
        }
        print("Choose the restaurant you wish to order.")
        print(hotel)
        chosen = int(input())
        if
        print("You've chosen ",end='')
        if chosen_hotel == 1:
            print(hotel[chosen])
        elif chosen_hotel == 2:
            print(hotel[chosen])
        elif chosen_hotel == 3:
            print(hotel[chosen])
        elif chosen_hotel == 4:
            print(hotel[chosen])
        else:
            print("an unavailable restaurant mf!")

    def Food_menu(self):

        pass

    def OrderConfirmation(self):

        pass

    def Payment(self):

        pass

    def DeliveryPartnerDetails(self):

        pass


obj = Food()
obj.user("", "")