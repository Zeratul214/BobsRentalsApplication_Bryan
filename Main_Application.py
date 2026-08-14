from rental_equipment import Ski as Ski, Snowboard as Snowboard
from customer import Customer as Customer
from rental import Rental as Rental
from rental_shop import RentalShop as RentalShop

def main():
    i = 1
    customer = []
    while True:
        name = input("Please enter customer name: ")
        customer_id = f"Customer{i}"
        customer.append(customer_id)
        customer_id = Customer(i, name)
        coupon_code = input("Please enter coupon here: ")

        print("Current rental periods-")
        print("Hourly")
        print("Daily")
        print("Weekly")

        rental_period = input("Please enter rental period: ")
        quantity = input("Please enter length of time: ")
        ski_daily = 0
        snowboard_daily = 0
        profit = 0

        rental = Rental(customer_id, rental_period, coupon_code)
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
                        ski_qty = int(input("Please enter total ski rentals: "))
                        if isinstance(ski_qty, int) and ski_qty > 0:
                            shop.rent_equipment("ski", ski_qty)
                        else:
                            print("Please enter a whole number above 0")
                    elif option == "2":
                        snowboard_qty = input("Please enter total snowboard rentals: ")
                        snowboard_qty = int(snowboard_qty)
                        if isinstance(snowboard_qty, int) and ski_qty > 0:
                            ski_qty = int(snowboard_qty)
                            shop.rent_equipment("snowboard", snowboard_qty)
                        else:
                            print("Please enter a whole number above 0")
                    elif option == "3":
                        for ski_num in ski_qty:
                            rental.add_equipment(Ski(f"SKI-{ski_num}"))
                        for snow_num in snowboard_qty:
                            rental.add_equipment(Snowboard(f"SKI-{snow_num}"))
                        subtotal = rental.calculate_subtotal(quantity)
                        equipment_total = ski_num + snow_num
                        print(f"Subtotal for {quantity} {rental_period}, {equipment_total} items: ${subtotal:.2f}")
                        print(f"Qualifies for family discount: {rental.qualifies_for_family_discount()}")
                        print(f"Qualifies for coupon discount: {rental.qualifies_for_coupon_discount()}")
                        estimate = rental.calculate_estimate(quantity)
                        print(f"Estimate with both discounts applied: ${estimate:.2f}")
                        shop.record_rental(ski_count=ski_qty, snowboard_count=snowboard_qty, amount_charged=0)
                        ski_daily += ski_qty
                        snowboard_daily += snowboard_qty
                        print("Back to main menu!")
                        exit_1 = True
                    else:
                        print("Invalid selection. Please try again!")


            elif choice == '2':
                print("You selected Return.")
                # Add functionality for Return here
                exit_2 = False
                while exit_2 == False:
                    print("Return Options: ")
                    print("1. Return rental")
                    print("2. Exit")

                    selection = input("Please select an option: ")

                    if selection == "1":
                        ski_returns = int(input("Please enter number of returned ski's: "))
                        snowboard_returns = int(input("Please enter number of returned snowboards: "))
                        shop.return_equipment("ski", ski_returns)
                        shop.return_equipment("snowboard", snowboard_returns)
                        actual_quantity=int(input("Please enter rental time: "))
                        final_bill = rental.calculate_final_bill(actual_quantity)
                        shop.record_rental(ski_count=ski_returns, snowboard_count=snowboard_returns, amount_charged=final_bill)
                        print(f"Final bill: ${final_bill:.2f}")
                        profit += final_bill
                    elif selection == "2":
                        print("Exit return menu.")
                        exit_2 = True
                    else:
                        print("Invalid selection, please try again.")

            elif choice == '3':
                print("Exiting to customer menu!")
                exit_0 == True
            else:
                print("Invalid selection. Please try again.")
        print("1. New Customer")
        print("2. Daily Totals")
        print("3. Exit")
        new_customer = input("Please select an option:")
        if new_customer == "1":
            i += 1
        elif new_customer == "2":
            print(f"Skis rented today: {shop.skis_rented_today}")
            print(f"Snowboards rented today: {shop.snowboards_rented_today}")
            print(f"Daily revenue: ${shop.daily_revenue:.2f}")
        elif new_customer == "3":
            print("Exiting application")
            break

if __name__ == "__main__":
    main()