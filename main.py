def main():
    option = 0

    while True:
        display_menu(option)

        user_input = input("Press 'Enter' to navigate the menu: ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == '1':
            list_dates(lines)
        elif user_input.lower() == '2':
            calculate_statistics([int(line[2]) for line in lines], [line[0] for line in lines], [line[1] for line in lines])
        elif user_input.lower() == '3':
            search_physics_name([int(line[2]) for line in lines], [line[0] for line in lines], [line[1] for line in lines])