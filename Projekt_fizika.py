file_path = 'fizikusok.txt'

def display_menu(selected_option):
    print("\nMenü:")
    options = ["Évszámok, listázása", "Legnagyobb, legkisebb, átlagos év kiírása", "Fizikus keresése", "Kilépés"]
    
    for i, option in enumerate(options):
        if i + 1 == selected_option:
            print(f">{option}<")
        else:
            print(f" {option} ")

def list_dates(lines):
    print("\nDates:")
    for line in lines:
        year, scientist, concept = int(line[2]), line[0], line[1]
        print(f"Évszám: {year}  Fizikusok: {scientist}  Találmányok: {concept}")

def calculate_statistics(years, scientists, concepts):
    largest_index = years.index(max(years))
    smallest_index = years.index(min(years))

    largest_year = years[largest_index]
    smallest_year = years[smallest_index]

    largest_scientist = scientists[largest_index]
    smallest_scientist = scientists[smallest_index]

    largest_concept = concepts[largest_index]
    smallest_concept = concepts[smallest_index]

    average_year = sum(years) / len(years)

    print(f"\nLegnagyobb: Év: {largest_year}, Fizikus: {largest_scientist}, Találmánya: {largest_concept}")
    print(f"Legkisebb: Év: {smallest_year}, Fizikus: {smallest_scientist}, Találmánya: {smallest_concept}")
    print(f"Átlagos: {average_year:.0f}")

def search_physics_name(years, scientists, concepts):
    user_input = input("\nAdj meg egy nevet! ").strip()

    while not user_input:
        print("Adj meg egy nevet! ")
        user_input = input().strip()

    if user_input:
        matching_indices = [i for i, name in enumerate(scientists) if name == user_input]

        if matching_indices:
            for index in matching_indices:
                user_year = years[index]
                user_concept = concepts[index]
                print(f"\nÉv: {user_year}, Fizikus: {user_input}, Találmánya: {user_concept}")
        else:
            print(f"\nA megadott név ({user_input}) nem található az adatok között.")

def main():
    repeat_program = 'igen'

    while repeat_program.lower() == 'igen':
        display_menu(0)

        user_input = input("Írj be egy számot, a feladat elvégezésére (1-3), Kilépés: 0: ").strip().lower()

        if user_input == '0':
            print("Program vége...")
            break

        try:
            option = int(user_input)
            if 1 <= option <= 3:
                if option == 1:
                    list_dates(lines)
                elif option == 2:
                    calculate_statistics([int(line[2]) for line in lines], [line[0] for line in lines], [line[1] for line in lines])
                elif option == 3:
                    search_physics_name([int(line[2]) for line in lines], [line[0] for line in lines], [line[1] for line in lines])
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

        repeat_program = input("\nAkarsz még Valamit? (igen/nem)): ").strip().lower()

if __name__ == "__main__":
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip().split(';') for line in file]

            if not lines:
                print("No data found in the file.")
            else:
                main()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError:
        print("Invalid year data in the file. Make sure the year is a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
