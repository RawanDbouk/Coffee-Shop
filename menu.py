def display_menu():
    print("\nWelcome to Our Coffee Shop!")
    print("Menu:")
    print("1. Espresso - $2.50")
    print("2. Latte - $3.00")
    print("3. Cappuccino - $3.00")
    print("4. Americano - $2.75")
    print("5. Quit")

def order_espresso():
    print("You ordered an Espresso. That will be $2.50.")

def order_latte():
    print("You ordered a Latte. That will be $3.00.")

def order_cappuccino():
    print("You ordered a Cappuccino. That will be $3.00.")

def order_americano():
    print("You ordered an Americano. That will be $2.75.")

def main():
    while True:
        display_menu()
        choice = input("Please enter the number of your choice (1-5): ")

        if choice == '1':
            order_espresso()
        elif choice == '2':
            order_latte()
        elif choice == '3':
            order_cappuccino()
        elif choice == '4':
            order_americano()
