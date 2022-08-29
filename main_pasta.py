"""This file is a program for a pasta restaurant's phone ordering service."""


def get_string(m):
    """Request string from user.

    :param m: string
    :return: string
    """
    my_string = input(m)
    return my_string


def get_integer(m):
    """Request integer from user.

    :param m: string
    :return: integer
    """
    while True:
        try:
            my_integer = int(input(m))
            return my_integer
        except ValueError:
            print("Oops, invalid entry, please try again")


def get_yes_no(m):
    """Get Y or N from user.

    :param m: string
    :return: integer
    """
    run = True
    while run is True:
        my_string = input(m).upper()
        if my_string == "Y":
            return my_string
        elif my_string == "N":
            return my_string
        else:
            print("Oops, invalid entry, please try again")


def validate_integer(message, a, b):
    """Request limited integer from user.

    :param message: string
    :param a: integer
    :param b: integer
    :return: integer
    """
    # must be between a and b
    while True:
        try:
            my_integer = int(input(message))
        except ValueError:
            print("Oops, invalid entry, please try again")
            continue
        if my_integer < a:
            print("This number is too small, please try again")
        elif my_integer > b:
            print("This number is too large, please try again")
        else:
            return my_integer


def validate_string_len(message, a, b):
    """Request limited length string from user.

    :param message: string
    :param a: integer
    :param b: integer
    :return: integer
    """
    # must be between a and b
    run = True
    while run is True:
        m = get_string(message)
        m_len = len(str(m))
        if m_len < a:
            print("This entry is too short, please try again")
        elif m_len > b:
            print("This entry is too large, please try again")
        else:
            return m


def get_letter(c):
    """Request letter from a list from user.

    :param c: list
    :return: None
    """
    run = True
    while run is True:
        user_choice = input("Please choose an option:").upper().strip()
        for i in range(0, len(c)):
            if user_choice == c[i][0]:
                return user_choice
        print("Oops, invalid entry, please try again")


def print_list(m):
    """Print list with two sets of values.

    :param m: list
    :return: None
    """
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:2} : {:<3}".format(m[i][0], m[i][1])
        print(output)


def print_menu(m):
    """Print menu with descriptions.

    :param m: list
    :return: None
    """
    for i in range(0, len(m)):
        if len(m[i]) != 3:
            print("Sublist is not the correct length")
            return None
        output = "{:2} : ${:<3} \n {}".format(m[i][0], m[i][1], m[i][2])
        print(output)


def print_list_triple(m):
    """Print list with three sets of values.

    :param m: list
    :return: None
    """
    for i in range(0, len(m)):
        if len(m[i]) != 3:
            print("Sublist is not the correct length")
            return None
        output = "{}\n{}\n{}".format(m[i][0], m[i][1], m[i][2])
        print(output)


def print_list_indexes(m):
    """Print list with indexes.

    :param m: list
    :return: None
    """
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:3} : ${:<3}".format(i + 1, m[i][0], m[i][1])
        print(output)


def find_name_index(c, n):
    """Find name of item from on index number.
    :param c: list
    :param n: string
    :return: integer
    """
    i = 0
    for x in c:
        if x[0] == n:
            return i
        i += 1
    return -1


def order_pasta(m, c):
    """Add an item to order.

    :param m: list
    :param c: list
    :return: None
    """
    print_list_indexes(m)
    pasta_index = validate_integer("Choose index number "
                                   "of pasta to order:", 1, len(m))
    pasta_index -= 1
    name = m[pasta_index][0]
    index = find_name_index(c, name)
    if index != -1:
        output = ("You currently have {} {} in the basket, you can order up "
                  "to {} more".format(c[index][2], name, 5 - c[index][2]))
        print(output)
        old_amount = c[index][2]
        number = validate_integer("How many more would would you like to add?:",
                                  0, 5 - c[index][2])
        print()
        c[index][2] = old_amount + number
        output_message = "You now have {} {}s in your basket." \
            .format(c[index][2], c[index][0])
        print(output_message)
    else:
        old_amount = 0
        number = validate_integer("How many would you like to add? "
                                  "(max 5):", 0, 5)
        print()
        new_amount = old_amount + number
        output_message = "You added {} {}s to your basket." \
            .format(new_amount, m[pasta_index][0])
        print(output_message)
        temp = [m[pasta_index][0], m[pasta_index][1], new_amount]
        if new_amount != 0:
            c.append(temp)


def remove_pasta(c):
    """Remove an item from order.

    :param c: list
    :return: None
    """
    if len(c) == 0:
        print("You haven't ordered any pastas yet :(")
        return None
    print("In your current order you have:")
    review_order(c)
    pasta_index = validate_integer("Choose which pasta you would "
                                   "like to remove:", 1, len(c))
    pasta_index -= 1
    print()
    number = validate_integer("How many would would you like to remove? "
                              "(please use numbers):", 0, c[pasta_index][2])
    c[pasta_index][2] -= number
    if c[pasta_index][2] == 0:
        print()
        output = ("You have removed all {} from your basket".format(c[pasta_index][0]))
        print(output)
        print()
        c.pop(pasta_index)
        if len(c) == 0:
            print("Your basket is now empty")
        else:
            print("In your order you now have:")
            review_order(c)
    elif c[pasta_index][2] != 0:
        print()
        output_message = "In your basket you now have:"
        print(output_message)
        review_order(c)


def review_order(c):
    """Review customer order.

    :param c: list
    :return: None
    """
    grand_total = 0
    for i in range(0, len(c)):
        if len(c[i]) != 3:
            print("Sublist is not the correct length")
            return None
        if len(c) == 0:
            print("Your basket is currently empty")
        else:
            pasta_quantity = c[i][2]
            pasta_price = c[i][1]
            total = pasta_price * pasta_quantity
            grand_total += total
            output = "{}: {} {} at ${} each: ${}" \
                .format(i + 1, c[i][2], c[i][0], c[i][1], total)
            print(output)
    final_output = "The grand total of your order is ${}".format(grand_total)
    print(final_output)


def order_cost(c):
    """Calculate total cost of customer order.

    :param c: list
    :return: None
    """
    grand_total = 0
    for i in range(0, len(c)):
        pasta_quantity = c[i][2]
        pasta_price = c[i][1]
        total = pasta_price * pasta_quantity
        grand_total += total
        output = "{} {} at ${} each: ${}" \
            .format(c[i][2], c[i][0], c[i][1], total)
        print(output)
    final_output = "The grand total of your order is ${}".format(grand_total)
    print(final_output)


def get_phone():
    """Request the customer phone number.

    :return: string
    """
    run = True
    while run is True:
        phone = validate_string_len("Please enter your phone number:", 9, 12).strip().replace(" ", "")
        if phone.isdigit():
            return phone
        print("Oops, invalid entry, please try again")


def details_delivery(r):
    """Confirm the customer details for delivery.
    :param r: list
    :return: None
    """
    run = True
    while run is True:
        name = validate_string_len("Please enter your name:", 1, 100) \
            .capitalize()
        address = validate_string_len("Please enter your street address "
                                      "and suburb:", 15, 200)
        phone = get_phone()
        print("Your details are\n{}\n{}\n{}".format(name, address, phone))
        confirm = get_yes_no("Would you like to confirm your details? Y/N:")
        if confirm == "Y":
            temp = [name, address, phone]
            r.append(temp)
            return confirm
        elif confirm == "N":
            print("Details erased, please re-enter")
            second_choice = get_string("You chose not to confirm details,"
                                       " erase and return to main menu (M) or "
                                       "erase and re-enter (R)?:").upper()
            if second_choice == "M":
                return None
            if second_choice == "R":
                print("Details erased, please re-enter")
            else:
                print("Oops, invalid input, please try again")
        else:
            print("Oops, invalid input, please try again")


def details_pickup(p):
    """Confirm the customer details for pickup.

    :param p: list
    :return: None
    """
    run = True
    while run is True:
        name = validate_string_len("Please enter your name:", 1, 100) \
            .capitalize()
        phone = get_phone()
        print("Your details are\n{}\n{}".format(name, phone))
        confirm = get_yes_no("Would you like to confirm your details? Y/N:")
        if confirm == "Y":
            temp = [name, phone]
            p.append(temp)
            return confirm
        elif confirm == "N":
            second_choice = get_string("You chose not to confirm details,"
                                       " erase and return to main menu (M) or "
                                       "erase and re-enter (R)?:").upper()
            if second_choice == "M":
                return None
            if second_choice == "R":
                print("Details erased, please re-enter")
            else:
                print("Oops, invalid input, please try again")
        else:
            print("Oops, invalid input, please try again")


def customer_details(c, r, p):
    """Confirm all customer details.

    :param c: list
    :param r: list
    :param p: list
    :return: None
    """
    if len(r) != 0 or len(p) != 0:
        print("You have already entered your details")
        choice = get_string("Would you like to erase "
                            "and re-enter? Y/N:").upper()
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
        receive = get_string("Would you like to have your order "
                             "delivered (D) or pick up (P):").upper()
        if receive == "D":
            choice = get_yes_no("This adds automatic $3 surcharge, total cost"
                                " is now ${}, would you like to continue? Y/N:"
                                .format(grand_total + 3)).upper()
            if choice == "Y":
                details_delivery(r)
                return None
            elif choice == "N":
                print()
        elif receive == "P":
            details_pickup(p)
            return None
        else:
            print("Oops, invalid entry, please try again")


def complete_order(c, p, d):
    """Complete order.

    :param c: list
    :param p: list
    :param d: list
    :return: None
    """
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
        grand_total += 3
        print("Your order is going to be delivered (note $3 surcharge) to:")
        print_list_triple(d)
    for i in range(0, len(c)):
        total = c[i][1] * c[i][2]
        grand_total += total
        output = "{} {} at ${} each: ${}"\
            .format(c[i][2], c[i][0], c[i][1], total)
        print(output)
    final_output = "The grand total of your order is ${}"\
        .format(grand_total)
    print(final_output)
    run = True
    while run is True:
        choice = get_string("Above are the details of your order, "
                            "would you like to confirm? Y/N:").upper()
        if choice == "Y":
            print("Thank you your order is confmired and now being prepared")
            c.clear()
            p.clear()
            d.clear()
            return None
        elif choice == "N":
            print("Returning to main menu...")
            return None
        else:
            print("Invalid entry, please try again")


def main_menu():
    """Call the other functions using a main function.

    :return: None
    """
    customer_order = []

    pickup_details = []

    delivery_details = []

    pasta_menu = [
        ["Linguine Gamberi", 23,
         "Long flat pasta.Tomato, garlic and chilli sauce, prawns, "
         "anchovies, capers, olives, parmesan."],
        ["Fusilli Pesto", 19,
         "Short, spiral pasta. Kale and cashew pesto and cream "
         "sauce, olives, parmesan."],
        ["Conchilglie alla Bolognese", 22,
         "Small, shell pasta. Northern italian beef and pork sauce, "
         "parmesan."],
        ["Rigatoni alla Caponata", 21,
         "Short, tube pasta. Agrodolce tomato sauce, "
         "eggplant, ricotta salata, pine nut."],
        ["Fettuccine Carbonara", 20,
         "Long, flat pasta. Creamy egg and pepper sauce, "
         "bacon, parmesan."],
        ["Spaghetti Pomodoro", 16,
         "Long, thin pasta. Classic tomato and basil sauce, parmesan."],
        ["Pappardelle Ricci D’Angello", 26,
         "Short, frizzy pasta. Slow cooked lamb ragu, "
         "rosemary, olives, sweet garlic, parmesan."],
        ["Raviolo di Salsiccia", 22,
         "Filled pasta. Red wine vinegar and tomato sauce, "
         "sausage, green capsicum, three cheese(filled) parmesan."],
        ["Ravioli di Ricotta", 20,
         "Spinach and ricotta(filled) pasta, brown butter sauce, "
         "sage, hazelnuts, parmesan."]]

    order_menu = [
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
        ["V", "View the pasta menu"],
        ["A", "Add a new pasta or more pasta to order"],
        ["R", "Remove a pasta or reduce pastas in order"],
        ["C", "Review customer's current order"],
        ["D", "Add customer details"],
        ["F", "Finish order placement"],
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
        if choice == "V":
            print("PASTA MENU:")
            print("." * 100)
            print_menu(pasta_menu)
            print("." * 100)
        elif choice == "A":
            order_pasta(order_menu, customer_order)
            print("." * 100)
        elif choice == "R":
            remove_pasta(customer_order)
            print("." * 100)
        elif choice == "C":
            review_order(customer_order)
            print("." * 100)
        elif choice == "D":
            customer_details(customer_order, delivery_details, pickup_details)
            print("." * 100)
        elif choice == "F":
            complete_order(customer_order, pickup_details, delivery_details)
            print("." * 100)
        elif choice == "Q":
            print("Thank you for visiting La migliore Pastaria")
            print("." * 100)
            run = False
        else:
            print("An error has occurred, please try again")
            print("." * 100)


main_menu()
