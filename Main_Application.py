from rental_equipment import Ski as Ski, Snowboard as Snowboard
from customer import Customer as Customer
from rental import Rental as Rental
from rental_shop import RentalShop as RentalShop

def main():
    i = 1
    while True:
        customer = []
        name = input("Please enter customer name: ")
        customer[i] = Customer(i, name)
        customer.append(customer[i])
        coupon_code = input("Please enter coupon here: ")

        print("Current rental periods-")
        print("Hourly")
        print("Daily")
        print("Weekly")

        rental_period = input("Please enter rental period: ")
        quantity = input("Please enter length of time: ")


        rental = Rental(customer[i], rental_period, coupon_code)
        exit_0 = False
        while exit_0 == False:
            shop = RentalShop()
            shop.set_starting_inventory(ski_count=30, snowboard_count=20)
            
            print("Welcome to the Main Menu!")
            print("1. Rental")
            print("2. Return")
            print("3. Exit")
            
            choice = input("Please select an option: ")
            
            if choice == '1':
                print("You selected Rental.")
                exit_1 = False
                # Add functionality for Rental here
                while exit_1 == False:
                    print("Please enter what you would like to rent.")
                    print("1. Ski")
                    print("2. Snowboard")
                    print("3. Exit")

                    option = input("Please select an option: ")

                    if option == "1":
                        ski_qty = input("Please enter total ski rentals: ")
                        shop.rent_equipment("ski", ski_qty)
                    elif option == "2":
                        snowboard_qty = input("Please enter total snowboard rentals: ")
                        shop.rent_equipment("snowboard", snowboard_qty)
                    elif option == "3":
                        for ski_num in ski_qty:
                            rental.add_equipment(Ski(f"SKI-{ski_num}"))
                        for snow_num in snowboard_qty:
                            rental.add_equipment(Snowboard(f"SKI-{snow_num}"))
                        subtotal = rental.calculate_subtotal(quantity)
                        print("Back to main menu!")
                        exit_1 = True
                    else:
                        print("Invalid selection. Please try again!")


            elif choice == '2':
                print("You selected Return.")
                # Add functionality for Return here
            elif choice == '3':
                print("Exiting to customer menu!")
                exit_0 == True
            else:
                print("Invalid selection. Please try again.")
        print("1. New Customer")
        print("2. Exit")
        new_customer = input("Please select an option:")
        if new_customer == "1":
            i += 1
        elif new_customer == "2":
            print("Exiting application")
            break
