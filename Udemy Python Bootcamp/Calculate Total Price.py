available_parts = {
    1: "computer",
    2: "monitor",
    3: "keyboard",
    4: "mouse",
    5: "hdmi cable",
    6: "dvd drive"
}

price_quantity = {
    "computer": {"price": 500, "quantity": 10},
    "monitor": {"price": 200, "quantity": 8},
    "keyboard": {"price": 500, "quantity": 5},
    "mouse": {"price": 10, "quantity": 0},
    "hdmi cable": {"price": 20, "quantity": 7},
    "dvd drive": {"price": 50, "quantity": 5}
}

print("Please select an item from the list.")
for key, value in available_parts.items():
    print(f"{key} : {value}")
print("0 : to finish")

choice = None
total_price = 0


def check_stock(p_choice, p_total_price):
    item = available_parts[p_choice]

    if price_quantity[item]["quantity"] == 0:
        print(f"{available_parts[choice]} out of stock.")
    else:
        print(f"Adding {item} to your basket.")
        price_quantity[item]["quantity"] -= 1
        p_total_price += price_quantity[item]["price"]

    return p_total_price


while choice != 0:
    choice = int(input("> "))
    if choice in available_parts:
        total_price = check_stock(choice, total_price)
    elif choice == 0:
        break
    else:
        print("Invalid Selection. Try again.")

print(f"Total price: {total_price}")
