def get_string(m):
    """Request a string from the user."""
    my_string = input(m)
    return my_string


def get_integer(m):
    """Request an integer from the user."""
    my_integer = int(input(m))
    return my_integer


def get_integer_limits(message, a, b):
    """Get an integer from the user with a limit."""
    # must be between a and b
    while True:
        try:
            my_integer = int(input(message))
        except:
            print("Invalid entry")
            continue
        if my_integer < a or my_integer > b:
            print()
            print("Not in correct range")
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
    pasta_index = get_integer_limits("Choose the index number of the pasta you would like to order", 1, len(m))
    pasta_index -= 1
    print()
    old_amount = 0
    number = get_integer("How many would would you like to add? (please use numbers):")
    print()
    new_amount = old_amount + number
    output_message = "You now have {} {}s in your basket.".format(new_amount, m[pasta_index][0])
    print(output_message)
    temp = [m[pasta_index][0], m[pasta_index][1], new_amount]
    c.append(temp)


def review_order(c):
    """ Review the user's order."""
    for i in range(0, len(c)):
        if len(c[i]) != 3:
            print("Sublist is not the correct length")
            return None
        output = "{} {}'s at ${} each".format(c[i][2], c[i][0], c[i][1])
        print(output)


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
        ["V", "View the pasta menu"],
        ["A", "Add a pasta to your order"],
        ["R", "Review your order"],
        ["Q", "Quit"]
    ]

    run = True
    while run is True:
        print("La migliore Pastaria")
        print("." * 100)
        print_list(my_menu)
        choice = get_string("Please select your option: ->").upper()
        print("." * 100)
        if choice == "V":
            print("PASTA MENU:")
            print("." * 100)
            print_list_with_indexes(pasta_menu)
            print("." * 100)
        elif choice == "A":
            order_pasta(pasta_menu, customer_order)
            print("." * 100)
        elif choice == "R":
            review_order(customer_order)
            print("." * 100)
        elif choice == "Q":
            print("Thank you for visiting La migliore Pastaria")
            print("." * 100)
            run = False
        else:
            print("Input was not recognised, please try again")
            print("." * 100)


main_menu()
