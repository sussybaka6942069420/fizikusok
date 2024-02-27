file_path = 'fizikusok.txt'

try:
    with open(file_path, 'r') as file:
        lines = [line.strip().split(';') for line in file]

        if not lines:
            print("No data found in the file.")
        else:
            years = [int(line[2]) for line in lines]
            scientists = [line[0] for line in lines]
            concepts = [line[1] for line in lines]

            print("Fizikusok és találmányaik:")
            for i in range(len(lines)):
                print(f"Év: {years[i]}, Fizikus: {scientists[i]}, Találmánya: {concepts[i]}")

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
            print(f"Átlagos: {average_year:.2f}")

            user_input = input("\nAdj meg egy nevet! ").strip()

            while not user_input:
                print("Adj meg egy nevet! ")
                user_input = input().strip()

            if user_input:
                user_index = scientists.index(user_input) if user_input in scientists else -1

                if user_index != -1:
                    user_year = years[user_index]
                    user_concept = concepts[user_index]
                    print(f"\nÉv: {user_year}, Fizikus: {user_input}, Találmánya: {user_concept}")
                else:
                    print(f"\nA megadott név ({user_input}) nem található az adatok között.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except ValueError:
    print("Invalid year data in the file. Make sure the year is a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")
