import time

order_food = [
    {"Pizza": 10}, {"Burger": 8}, {"Sushi": 15}, {"Pasta": 12},
    {"Salad": 7}, {"Tacos": 9}, {"Ice Cream": 5}, {"Steak": 20},
    {"Sandwich": 6}, {"Soup": 4}, {"Fries": 3}, {"Curry": 11}
]

class InstaMart:
    def __init__(self):
        self.payment_success = False
        self.selected_item = None
        self.bill = 0
        self.delivery_charge = 2

        print("Welcome to InstaMart!")
        print("Here is our menu:")
        for index, item in enumerate(order_food, start=1):
            name = list(item.keys())[0]
            price = list(item.values())[0]
            print(f"{index}. {name} - ${price}")
            

    def place_order(self):
        x = input("Enter the item number you want to order: ")
      
        try:
            item_number = int(x)
            if 1 <= item_number <= len(order_food):
                self.selected_item = order_food[item_number - 1]
                name = list(self.selected_item.keys())[0]
                self.bill = list(self.selected_item.values())[0]

                total_bill = self.bill + self.delivery_charge # including delivery charge

                print(f"You have ordered: {name}")
                print(f"your order value: ${self.bill}")
                time.sleep(2)
                print(f"Total bill (including delivery): ${total_bill}")
                
                time.sleep(2)
                return True
            else:
                print("Invalid item number.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False

    def payment(self):
        print("Processing your payment...")
        time.sleep(2)
        total_bill = self.bill + self.delivery_charge  # including delivery charge

        print(f"Your total bill is: ${total_bill}")
        user_payment = input("Enter payment amount: $")

        if user_payment != str(total_bill):
            print("Payment failed. Amount mismatch.")
            return

        while True:
            pay = input("Confirm payment? (y/n): ").lower()

            if pay == 'y':
                print("Payment successful! Thank you for shopping with InstaMart")
                self.payment_success = True
                break

            elif pay == 'n':
                print("Payment cancelled.")
                break

            else:
                print("Please enter valid option (y or n)")

    def deliver_order(self):
        if not self.payment_success:
            print("Cannot deliver order without successful payment.")
            return

        print("-------------------We received your order-----------------(wait).", end="", flush=True)
        time.sleep(10)
        print("\r------------------Preparing your order-------------", end="", flush=True)
        time.sleep(10)
        print("\r------------------Your order is out for delivery!------------------", end="", flush=True)
        time.sleep(10)
        print("\rYour order has been delivered. Enjoy your meal 🍽️")

    def rating(self):
        rating = input("Please rate your experience from 1 to 5: ")
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                print(f"Thank you for rating us {rating} stars ⭐")
            else:
                print("Invalid rating. Please give 1 to 5.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    mart = InstaMart()
    if mart.place_order():
        mart.payment()
        mart.deliver_order()
        mart.rating()
