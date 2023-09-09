from utilities import *
import os


def main_menu():
    while True:
        print("\nEscoge una opcion de boletin:")

        for i, op in enumerate(denominations):
            print(f"({i+1}) {op}")
        print(f"({len(denominations)+1}) Todo")
        print(f"({len(denominations)+2}) Salir")
        try:
            opcion = int(input())
            if 0 < opcion <= len(denominations):
                sub_time_options(denominations[opcion - 1])
            elif opcion == len(denominations) + 1:
                validator_of_year(download_multiple_bulletins)
            elif opcion == len(denominations) + 2:
                break
            else:
                print("--- Indica una opcion correcta (1 al 8) ---")
        except ValueError as e:
            print("--- Indica una opcion correcta (1 al 8) ---")


def sub_time_options(denomination: str):
    while True:
        print("\nEscoge una opcion de descarga:")
        print("(1) Anual")
        print("(2) Mensual (No disponible)")
        print("(3) Mas reciente (No disponible)")
        print("(4) Salir")

        opcion = input()

        match opcion:
            case "1":
                set_denomination(denomination)
                validator_of_year(download_multiple_months)
                break
            case "2":
                # validator_of_month_and_year(download_one_month)
                break
            case "3":
                # year = current_year
                # month = int(current_month) - 1
                # download_most_recent(year, month)
                break
            case "4":
                break
            case _:
                print("--- Indica una opcion correcta (1, 2, 3 o 4) ---")


if __name__ == "__main__":
    if os.path.exists("tempCodeRunnerFile.py"):
        os.remove("tempCodeRunnerFile.py")
    main_menu()
