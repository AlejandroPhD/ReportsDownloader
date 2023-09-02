from utilities import *
import os


def main_menu():
    while True:
        print("\n Escoge una opcion de descarga:")
        print("(1) Anual")
        print("(2) Mensual")
        print("(3) Mas reciente")
        print("(4) Salir")

        opcion = input()

        match opcion:
            case "1":
                validator_of_year(download_multiple_months)
            case "2":
                validator_of_month_and_year(download_one_month)
            case "3":
                year = current_year
                month = int(current_month) - 1
                download_most_recent(year, month)
            case "4":
                break
            case _:
                print("--- Indica una opcion correcta (1, 2, 3 o 4) ---")


if __name__ == "__main__":
    if os.path.exists("tempCodeRunnerFile.py"):
        os.remove("tempCodeRunnerFile.py")
    main_menu()