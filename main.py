print ("Welcome to the lift!")

current_floor = 0

while True:
    floor = input(f"please enter the floor you want to go to: (G - 10)").upper()

    if floor == "G":
        selected_floor = 0

    elif floor .isdigit() and 1 <= int(floor) <= 10:
        selected_floor = int(floor)

    else:
        print("Invalid input. Please enter a valid floor number (G - 10).")
        continue

    if selected_floor > current_floor:
        print("Going up...")

    elif selected_floor < current_floor:
        print("Going down...")

    else:
        print("You are already on this floor.")

    current_floor = selected_floor

    if current_floor == 0:
        print("Ground floor, Have a nice day!")

    else:
        print(f"{current_floor} floor, Have a nice day!")

    exit_choice = input("Do you want to exit the lift? (yes/no)").lower()

    if exit_choice == "yes" or exit_choice == "y":
        print("Exiting the lift. Have a great day!")
        break

    elif exit_choice == "no" or exit_choice == "n":
        continue

    else:
        print("Invalid choice. Continuing...")
    
