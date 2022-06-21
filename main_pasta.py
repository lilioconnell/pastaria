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
            print()
            print("The number you have entered is too small, please try again")
            print()
        elif my_integer > b:
            print()
            print("The number you have entered is too large, please try again")
            print()
        else:
            return my_integer


def print_list(m):
    """Print the list."""
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:2} : {:<3}".format(m[i][0], m[i][1])
        print(output)


def print_list_with_indexes(m):
    """Print the list with indexes."""
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:3} : ${:<3}".format(i + 1, m[i][0], m[i][1])
        print(output)


def order_pasta(m, c):
    """Add a pizza to the order."""
    print_list_with_indexes(m)
    pasta_index = validate_integer("Choose the index number of the pasta you would like to order", 1, len(m))
    pasta_index -= 1
    print()
    old_amount = 0
    number = validate_integer("How many would would you like to add? (you can order up to 5):", 0, 5)
    print()
    new_amount = old_amount + number
    output_message = "You now have {} {}s in your basket.".format(new_amount, m[pasta_index][0])
    print(output_message)
    temp = [m[pasta_index][0], m[pasta_index][1], new_amount]
    c.append(temp)


def remove_pasta(m, c):
    """Remove a pizza to the order."""
    print("In your current order you have:")
    review_order(c)
    pasta_index = validate_integer("Choose the index number of the pasta you would like to remove", 1, len(c))
    pasta_index -= 1
    print()
    old_amount = c[pasta_index][2]
    number = validate_integer("How many would would you like to remove? (please use numbers):", 1, c[pasta_index][2])
    c[pasta_index][2] -= number
    print()
    output_message = "In your basket you now have:"
    print(output_message)
    review_order(c)


def review_order(c):
    """ Review the user's order."""
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
    final_output = "The grand total cost of your order is ${}".format(grand_total)
    print(final_output)


def main_menu():
    """Main function call other functions."""

    customer_order = []

    pasta_menu = [
        ["Linguine Gamberi ", 23],
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
        ["E", "Calculate the total cost of your order"],
        ["Q", "Quit"]
    ]

    run = True
    while run is True:
        print("La migliore Pastaria")
        print("." * 100)
        print_list(my_menu)
        choice = get_string("Please select your option: ->").upper()
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
            remove_pasta(pasta_menu, customer_order)
            print("." * 100)
        elif choice == "E":
            order_cost(customer_order)
            print("." * 100)
        elif choice == "Q":
            print("Thank you for visiting La migliore Pastaria")
            print("." * 100)
            run = False
        else:
            print("Input was not recognised, please try again")
            print("." * 100)


main_menu()
