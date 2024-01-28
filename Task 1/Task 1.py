def calculate_price(is_tuesday: bool, num_pizzas: int, is_delivery: bool, is_ordered_via_app: bool) -> float:
    pizza_price = 12
    delivery_cost = 2.5 if is_delivery and num_pizzas < 5 else 0

    total_pizza_price = num_pizzas * pizza_price

    if is_tuesday:
        total_pizza_price *= 0.5

    if is_ordered_via_app:
        total_pizza_price *= 0.75

    total_price = total_pizza_price + delivery_cost
    return total_price

def get_yes_no_input(prompt: str) -> bool:
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response == "y" or response == "n":
            return response == "y"
        else:
            print('Please answer "y" or "n".')

print("BPP Pizza Price Calculator")
print("==========================")

# Gather order information
is_tuesday = get_yes_no_input("Is it Tuesday?")
num_pizzas = int(input("How many pizzas would you like to order? "))
is_delivery = get_yes_no_input("Would you like delivery?")
is_ordered_via_app = get_yes_no_input("Did you order via the BPP app?")

# Calculate and display the total price
total_price = calculate_price(is_tuesday, num_pizzas, is_delivery, is_ordered_via_app)
print(f"Total price: £{total_price:.2f}")
