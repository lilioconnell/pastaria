"""This file is a program for a pasta restaurant's phone ordering service."""


def get_string(m):
    """Request a string from the user."""
    my_string = input(m)
    return my_string


def get_integer(m):
    """Request an integer from the user."""
    while True:
        try:
            my_integer = int(input(m))
            return my_integer
        except:
            print("Invalid entry")


def validate_integer(message, a, b):
    """Get an integer from the user with a limit."""
    # must be between a and b
    while True:
        try:
            my_integer = int(input(message))
        except:
            print("Invalid entry")
            continue
        if my_integer < a:
            print("This number is too small, please try again")
        elif my_integer > b:
            print("This number is too large, please try again")
        else:
            return my_integer


def get_letter(option_set):
    """Get an letter from the user from a set list."""
    run = True
    while run is True:
        user_choice = input("Please choose an option:").upper()
        for i in range(0, len(option_set)):
            if user_choice == option_set[i][0]:
                return user_choice
        print("Invalid entry, please try again")


def print_list(m):
    """Print the list."""
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:2} : {:<3}".format(m[i][0], m[i][1])
        print(output)


def print_list_triple(m):
    """Print the list."""
    for i in range(0, len(m)):
        if len(m[i]) != 3:
            print("Sublist is not the correct length")
            return None
        output = "{:2} : {:<3}: {:<3}".format(m[i][0], m[i][1], m[i][2])
        print(output)


def print_list_with_indexes(m):
    """Print the list with indexes."""
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:3} : ${:<3}".format(i + 1, m[i][0], m[i][1])
        print(output)


def find_name_index(c, n):
    """Find the name of a pasta based on index number."""
    i = 0
    for x in c:
        if x[0] == n:
            return i
        i += 1
    return -1


def order_pasta(m, c):
    """Add a pizza to the order."""
    print_list_with_indexes(m)
    pasta_index = validate_integer("Choose index number of the pasta you would like to order", 1, len(m))
    pasta_index -= 1
    name = m[pasta_index][0]
    index = find_name_index(c, name)
    if index != -1:
        output = ("You currently have {} {} in the order, you can order up to {} more".format(c[index][2], name, 5 - c[index][2]))
        print(output)
        old_amount = c[index][2]
        number = validate_integer("How many would would you like to add?:", 0, 5 - c[index][2])
        print()
        c[index][2] = old_amount + number
        output_message = "You now have {} {}s in your basket.".format(c[index][2], m[index][0])
        print(output_message)
    else:
        old_amount = 0
        number = validate_integer("How many would you like to add? (you can order up to 5):", 0, 5)
        print()
        new_amount = old_amount + number
        output_message = "You now added {} {}s to your basket.".format(new_amount, m[pasta_index][0])
        print(output_message)
        temp = [m[pasta_index][0], m[pasta_index][1], new_amount]
        c.append(temp)


def remove_pasta(c):
    """Remove a pizza to the order."""
    if len(c) == 0:
        print("You haven't ordered any pastas yet, please try again later")
        return None
    print("In your current order you have:")
    review_order(c)
    pasta_index = validate_integer("Choose index number of pasta you would like to remove some of", 1, len(c))
    pasta_index -= 1
    print()
    number = validate_integer("How many would would you like to remove? (please use numbers):", 1, c[pasta_index][2])
    c[pasta_index][2] -= number
    if c[pasta_index][2] == 0:
        c.pop(pasta_index)
    print()
    output_message = "In your basket you now have:"
    print(output_message)
    review_order(c)


def review_order(c):
    """Review the user's order."""
    for i in range(0, len(c)):
        if len(c[i]) != 3:
            print("Sublist is not the correct length")
            return None
        output = "{}: {} {}'s at ${} each".format(i + 1, c[i][2], c[i][0], c[i][1])
        print(output)


def order_cost(c):
    """Calculate the total cost of the user's order."""
    grand_total = 0
    for i in range(0, len(c)):
        pasta_quantity = c[i][2]
        pasta_price = c[i][1]
        total = pasta_price * pasta_quantity
        grand_total += total
        output = "{} {} at ${} each: ${}".format(c[i][2], c[i][0], c[i][1], total)
        print(output)
    final_output = "The grand total of your order is ${}".format(grand_total)
    print(final_output)


def get_phone(m):
    """Ask for and confirm the user has input an acceptable phone number."""
    run = True
    while run is True:
        phone = get_string(m)
        phone_number = len(str(phone))
        if phone_number > 12:
            print("This number is too large, please try again")
        elif phone_number < 9:
            print("This number is too small, please try again")
        else:
            return phone


def get_name(m):
    """Ask for and confirm the user has input an acceptable name."""
    run = True
    while run is True:
        name = get_string(m)
        name_length = len(str(name))
        if name_length < 1:
            print("This number is too small, please try again")
        elif name_length > 100:
            print("This number is too large, please try again")
        else:
            return name


def get_address(m):
    """Ask for and confirm the user has input an acceptable address."""
    run = True
    while run is True:
        address = get_string(m)
        address_length = len(str(address))
        if address_length < 15:
            print("This number is too small, please try again")
        else:
            return address


def confirm_details_delivery(r):
    """Confirm the user's details."""
    run = True
    while run is True:
        name = get_name("Please enter your name:")
        address = get_address("Please enter your address in form STREET ADDRESS, CITY, POST CODE:")
        phone = get_phone("Please enter your phone number:")
        confirm = get_string(
            "Your details are {}: {}: {}, please press Y/N to confirm:".format(name, address, phone)).upper()
        if confirm == "Y":
            temp = [name, address, phone]
            r.append(temp)
            return confirm
        elif confirm == "N":
            print("Details erased, please re-enter")
        else:
            print("Invalid input, please try again")


def confirm_details_pickup(p):
    """Confirm the user's details."""
    run = True
    while run is True:
        name = get_name("Please enter your name:")
        phone = get_phone("Please enter your phone number:")
        confirm = get_string("Your details are {}: {}, please press Y/N to confirm:".format(name, phone)).upper()
        if confirm == "Y":
            temp = [name, phone]
            p.append(temp)
            return confirm
        elif confirm == "N":
            print("Details erased, please re-enter")
        else:
            print("Invalid input, please try again")


def customer_details(c, r, p):
    """Confirm the user's order."""
    if len(r) != 0 or len(p) != 0:
        print("You have already entered your details")
        choice = get_string("Would you like to erase and renter? Y/N:").upper()
        if choice == "Y":
            print()
            r.clear()
            p.clear()
        elif choice == "N":
            print("Returning to main menu...")
            return None
    grand_total = 0
    for i in range(0, len(c)):
        total = c[i][1] * c[i][2]
        grand_total += total

    run = True
    while run is True:
        receive = get_string("Would you like to have your order delivered (D) or pick up (P):").upper()
        if receive == "D":
            print("This will add an automatic $3 surcharge, your total cost is now ${}"
                  .format(grand_total + 3))
            confirm_details_delivery(r)
            return None
        elif receive == "P":
            confirm_details_pickup(p)
            return None
        else:
            print("This is not a valid input, please try again")


def complete_order(c, p, d):
    """Complete the customer order."""
    grand_total = 0
    if len(c) == 0:
        print("You have not ordered any pastas yet, please do so first")
        return None
    elif len(d) == 0 and len(p) == 0:
        print("You have not entered customer details yet, please do so first")
        return None
    elif len(p) != 0:
        print("You are going to pick up your order")
        print_list(p)
    elif len(d) != 0:
        grand_total+=3
        print("Your order is going to be delivered (note $3 surcharge) to:")
        print_list_triple(d)
    for i in range(0, len(c)):
        total = c[i][1] * c[i][2]
        grand_total += total
        output = "{} {} at ${} each: ${}".format(c[i][2], c[i][0], c[i][1], total)
        print(output)
        final_output = "The grand total of your order is ${}".format(grand_total)
        print(final_output)
    run = True
    while run is True:
        choice = get_string("Above are the details of your order, would you like to confirm? Y/N:").upper()
        if choice == "Y":
            print("Thank you your order is complete")
            c.clear()
            p.clear()
            d.clear()
            return None
        elif choice == "N":
            print("Returning to main menu...")
            return None
        else:
            print("Invalid input, please try again")


def main_menu():
    """Main function call other functions."""

    customer_order = []

    customer_pickup_details = []

    customer_delivery_details = []

    pasta_menu = [
        ["Linguine Gamberi", 23],
        ["Fusilli Pesto", 19],
        ["Conchilglie alla Bolognese", 22],
        ["Rigatoni alla Caponata", 21],
        ["Fettuccine Carbonara", 20],
        ["Spaghetti Pomodoro", 16],
        ["Pappardelle Ricci D’Angello", 26],
        ["Raviolo di Salsiccia", 22],
        ["Ravioli di Ricotta", 20]
    ]

    my_menu = [
        ["A", "View the pasta menu"],
        ["B", "Add a pasta to your order"],
        ["C", "Review your order"],
        ["D", "Remove a pasta from your order"],
        ["E", "Add customer details"],
        ["F", "Complete order placement"],
        ["Q", "Quit"]
    ]

    option_set = []

    for x in my_menu:
        option_set.append(x[0])

    run = True
    while run is True:
        print("La migliore Pastaria")
        print("." * 100)
        print_list(my_menu)
        choice = get_letter(option_set)
        print("." * 100)
        if choice == "A":
            print("PASTA MENU:")
            print("." * 100)
            print_list_with_indexes(pasta_menu)
            print("." * 100)
        elif choice == "B":
            order_pasta(pasta_menu, customer_order)
            print("." * 100)
        elif choice == "C":
            review_order(customer_order)
            print("." * 100)
        elif choice == "D":
            remove_pasta(customer_order)
            print("." * 100)
        elif choice == "E":
            customer_details(customer_order, customer_delivery_details, customer_pickup_details)
            print("." * 100)
        elif choice == "F":
            complete_order(customer_order, customer_pickup_details, customer_delivery_details)
            print("." * 100)
        elif choice == "Q":
            print("Thank you for visiting La migliore Pastaria")
            print("." * 100)
            run = False
        else:
            print("An error has occured, please try again")
            print("." * 100)


main_menu()
