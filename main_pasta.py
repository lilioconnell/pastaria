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
            print("The number you have entered is too small, please try again")
        elif my_integer > b:
            print("The number you have entered is too large, please try again")
        else:
            return my_integer

def get_letter(option_set):
    run = True
    while run == True:
        user_choice = input("What option would you like to select?:").upper()
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


def print_list_with_indexes(m):
    """Print the list with indexes."""
    for i in range(0, len(m)):
        if len(m[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:3} : ${:<3}".format(i + 1, m[i][0], m[i][1])
        print(output)

def find_name_index(c, n):
    i=0
    for x in c:
        if x[0] == n:
            return i
        i += 1
    return -1


def order_pasta(m, c):
    """Add a pizza to the order."""
    print_list_with_indexes(m)
    pasta_index = validate_integer("Choose the index number of the pasta you would like to order", 1, len(m))
    print()
    pasta_index -= 1
    name = m[pasta_index][0]
    index = find_name_index(c, name)
    if index != -1:
        output = ("You currently have {} {} in your order, you can order up to {} more".format(c[index][2], name, 5-c[index][2]))
        print(output)
        old_amount = c[index][2]
        number = validate_integer("How many more would would you like to add?:", 0, 5-c[index][2])
        print()
        c[index][2] = old_amount + number
        output_message = "You now have {} {}s in your basket.".format(c[index][2], m[index][0])
        print(output_message)
    else:
        print("Not yet in order")
        old_amount = 0
        number = validate_integer("How many would would you like to add? (you can order up to 5):", 0, 5)
        print()
        new_amount = old_amount + number
        output_message = "You now have {} {}s in your basket.".format(new_amount, m[pasta_index][0])
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
    pasta_index = validate_integer("Choose the index number of the pasta you would like to remove some of", 1, len(c))
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

def get_phone(m):
    """ Ask for and confirm the user has input an acceptable phone number. """
    run = True
    while run == True:
        phone = get_string(m)
        phone_number = len(str(phone))
        if phone_number > 12:
            print("The number you have entered is too large, please try again")
        elif phone_number < 9:
            print("The number you have entered is too small, please try again")
        else:
            return phone

def get_name(m):
    """ Ask for and confirm the user has input an acceptable name. """
    run = True
    while run == True:
        name = get_string(m)
        name_length = len(str(name))
        if name_length < 1:
            print("The number you have entered is too small, please try again")
        elif name_length > 100 :
            print("The number you have entered is too large, please try again")
        else:
            return name

def get_address(m):
    """ Ask for and confirm the user has input an acceptable address. """
    run = True
    while run == True:
        address = get_string(m)
        address_length = len(str(address))
        if address_length < 15:
            print("The number you have entered is too small, please try again")
        else:
            return address

def confirm_order(c, m):
    """Confirm the user's order."""
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

    run = True
    while run == True:
        receive = get_string("Would you like to have your order delivered (D) or pick up (P):").upper()
        if receive == "D":
            print("This will add an automatic $3 surcharge, your total cost is now ${}".format(grand_total+3))
            name = get_name("Please enter your name:")
            address = get_address("Please enter your address in form STREET ADDRESS, PROVINCE, CITY, POST CODE:")
            phone = get_phone("Please enter your phone number:")
            confirm = ("Your details are {}: {}: {}".format(name, address, phone))
            print(confirm)
            temp = [name, phone, address]
            m.append(temp)
            return None

        elif receive == "P":
            name = get_name("Please enter your name:")
            phone = get_phone("Please enter your phone number:")
            confirm = ("Your details are {}: {}".format(name, phone))
            print(confirm)
            temp = [name, phone]
            m.append(temp)
            return None
        else:
            print("This is not a valid input, please try again")





def main_menu():
    """Main function call other functions."""

    customer_order = []

    customer_details = []

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
        ["E", "Calculate the total cost of your order"],
        ["F", "Confirm Order"],
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
            order_cost(customer_order)
            print("." * 100)
        elif choice == "F":
            confirm_order(customer_order, customer_details)
            print("." * 100)
        elif choice == "Q":
            print("Thank you for visiting La migliore Pastaria")
            print("." * 100)
            run = False
        else:
            print("An error has occured, please try again")
            print("." * 100)


main_menu()
