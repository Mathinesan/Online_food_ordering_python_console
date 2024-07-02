class Food:

    def user(self):
        self.name = input("Enter your name: ")
        while True:
            self.ph_num = input("Enter your mobile number: ")
            if len(self.ph_num) == 10 and self.ph_num.isdigit():
                break
            else:
                print("Invalid phone number. Please enter a 10-digit number.")

        print("User Details")
        print("Name:", self.name)
        print("Mobile Number:", self.ph_num)

    def city(self):
        self.cities = {
            '1': "Erode",
            '2': "Coimbatore",
            '3': "Salem",
            '4': "Namakkal"
        }
        print("Choose your city.")
        for key, value in self.cities.items():
            print(key + ": " + value)
        while True:
            self.chosen_city = input()
            if self.chosen_city in self.cities:
                print("Selected City:", self.cities[self.chosen_city])
                break
            else:
                print("Invalid input! Please choose a valid city.")

    def Restaurants(self):
        self.restaurants = {
            "Erode": ["1. Vadakku Restaurant", "2. Kongu Parotta", "3. Taj Hotels"],
            "Coimbatore": ["1. Dosa & Drama", "2. Arabian Cuisine", "3. McDonald's"],
            "Salem": ["1. H for Hitler", "2. Pizza Hut", "3. Steaks and Streaks"],
            "Namakkal": ["1. Oscar kudra trumpeh", "2. Burger King", "3. A2B"]
        }
        chosen_city_name = self.cities[self.chosen_city]
        print("Choose the restaurant you wish to order from below.")
        for res in self.restaurants[chosen_city_name]:
            print(res)
        while True:
            self.chosen_restaurant = input()
            if self.chosen_restaurant in ['1', '2', '3']:
                self.chosen_restaurant_name = \
                self.restaurants[chosen_city_name][int(self.chosen_restaurant) - 1].split('. ')[1]
                print(f"You've chosen {self.chosen_restaurant_name}")
                break
            else:
                print("Invalid input! Please choose a valid restaurant.")

    def Food_menu(self):
        menus = {
            "Vadakku Restaurant": {"Dosa": 50, "Idli": 30, "Vada": 20},
            "Kongu Parotta": {"Parotta": 60, "Chicken Curry": 120, "Mutton Curry": 150},
            "Taj Hotels": {"Biriyani": 150, "Paneer Butter Masala": 200, "Naan": 40},
            "Dosa & Drama": {"Dosa": 70, "Paneer Dosa": 90, "Masala Dosa": 80},
            "Arabian Cuisine": {"Shawarma": 100, "Grill Chicken": 250, "Falafel": 80},
            "McDonald's": {"Burger": 120, "Fries": 80, "Coke": 40},
            "H for Hitler": {"Pizza": 150, "Pasta": 100, "Garlic Bread": 50},
            "Pizza Hut": {"Cheese Pizza": 200, "Veggie Pizza": 180, "Chicken Pizza": 220},
            "Steaks and Streaks": {"Steak": 300, "Grilled Chicken": 250, "Fish Fillet": 200},
            "Oscar kudra trumpeh": {"Sandwich": 100, "Burger": 120, "Pasta": 150},
            "Burger King": {"Whopper": 200, "Veg Burger": 150, "Chicken Burger": 180},
            "A2B": {"Sambar Rice": 50, "Curd Rice": 40, "Rava Kesari": 30}
        }

        self.menu = menus[self.chosen_restaurant_name]
        print("Menu for", self.chosen_restaurant_name)
        for item, price in self.menu.items():
            print(f"{item}: Rs {price}")

        self.order = {}
        while True:
            item = input("Enter the item you want to order (type 'done' when finished): ")
            if item == "done":
                break
            elif item in self.menu:
                quantity = int(input(f"Enter the quantity for {item}: "))
                self.order[item] = self.order.get(item, 0) + quantity
            else:
                print("Invalid item! Please choose from the menu.")

    def OrderConfirmation(self):
        print("Order Confirmation")
        total = 0
        for item, quantity in self.order.items():
            price = self.menu[item] * quantity
            total += price
            print(f"{item} x {quantity}: Rs {price}")

        gst = total * 0.18
        total_with_gst = total + gst
        print(f"Total: Rs {total}")
        print(f"GST (18%): Rs {gst}")
        print(f"Total with GST: Rs {total_with_gst}")

        discount = 0
        coupon = input("Enter any coupon code/discount (if any): ")
        if coupon == "DISCOUNT10":
            discount = total_with_gst * 0.1
            total_with_gst -= discount
            print(f"Discount: Rs {discount}")
            print(f"Total after discount: Rs {total_with_gst}")

        self.final_amount = total_with_gst

    def Payment(self):
        print("Payment Method")
        print("1. UPI")
        print("2. Cash on Delivery")
        while True:
            payment_method = input("Choose your payment method: ")
            if payment_method == "1":
                print("You chose UPI. Please complete the payment via your UPI app.")
                break
            elif payment_method == "2":
                self.final_amount += 60
                print(f"You chose Cash on Delivery. An additional delivery fee of Rs 60 will be added.")
                print(f"Total amount to be paid: Rs {self.final_amount}")
                break
            else:
                print("Invalid input! Please choose a valid payment method.")

    def DeliveryPartnerDetails(self):
        delivery_partners = {
            "Erode": "John Doe - 9876543210",
            "Coimbatore": "Jane Smith - 8765432109",
            "Salem": "Bob Johnson - 7654321098",
            "Namakkal": "Alice Brown - 6543210987"
        }
        print("Delivery Partner Details")
        print(f"Delivery Partner: {delivery_partners[self.cities[self.chosen_city]]}")

        self.address = input("Enter your delivery address: ")
        self.estimated_time = "30-45 minutes"

        print(f"Delivery Address: {self.address}")
        print(f"Your order will reach you in {self.estimated_time}.")
        print("Thank you for ordering with us!")

        rating = input("Please rate our service (1-5): ")
        print(f"Thank you for your rating of {rating}!")


obj = Food()
obj.user()
obj.city()
obj.Restaurants()
obj.Food_menu()
obj.OrderConfirmation()
obj.Payment()
obj.DeliveryPartnerDetails()
