# -----------------------------------------------------------------
# Assignment Name:  Final Part 1
# Name:             William Schoenling
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# Description
# -----------------------------------------------------------------
This repository contains the reusable business classes for Bob's Ski &
Snowboard Rentals. User menus, workflows, and reports are not included.

# -----------------------------------------------------------------
# Classes
# -----------------------------------------------------------------
### `RentalEquipment`
Abstract base class for all rental equipment. Provides shared behavior
and requires subclasses to define their rates and equipment type.

### `Ski`
Represents a ski rental item.

### `Snowboard`
Represents a snowboard rental item.

### `Customer`
Stores customer information.

### `Rental`
Manages a customer's rental, including equipment, pricing, discounts,
estimates, and final billing.

### `RentalShop`
Manages inventory, equipment rentals/returns, and daily rental statistics.

# -----------------------------------------------------------------
# Key Properties and Methods
# -----------------------------------------------------------------
- `calculate_best_price()` – Returns the lowest valid rental price.
- `add_equipment()` – Adds equipment to a rental.
- `calculate_estimate()` – Calculates the estimated rental cost.
- `calculate_final_bill()` – Calculates the final rental cost.
- `qualifies_for_family_discount()` – Checks family discount eligibility.
- `qualifies_for_coupon_discount()` – Checks coupon eligibility.
- `set_starting_inventory()` – Sets initial inventory.
- `is_available()` – Checks equipment availability.
- `rent_equipment()` / `return_equipment()` – Updates inventory.
- `record_rental()` – Records rental totals.

# -----------------------------------------------------------------
# Object-Oriented Design
# -----------------------------------------------------------------
- **Encapsulation:** Uses private attributes and properties to protect object data.
- **Inheritance:** `Ski` and `Snowboard` inherit from `RentalEquipment`.
- **Polymorphism:** Shared methods behave according to the equipment subclass.
- **Abstraction:** `RentalEquipment` is an abstract base class that defines the required interface for rental equipment.

# -----------------------------------------------------------------
# Running the Tests
# -----------------------------------------------------------------
To run the tests, use `python test_classes.py`.

It will print the results of tests covering object creation, pricing,
inventory management, discounts, billing, and daily rental totals.