import requests
import os
import shutil
import datetime

from bulletins.bulletin import Bulletin
from bulletins.multiple import MultipleBanks
from bulletins.small_and_medium import SmallAndMediumBanks
from bulletins.financial_housing import FinancialHousingEntities
from bulletins.development_financial import DevelopmentFinancialInstitutions
from bulletins.open_savings_and_credits import OpenSavingsAndCreditCooperatives
from bulletins.productive_development import ProductiveDevelopmentBanks


initial_year = 1990
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

current_denominations: dict[str, Bulletin] = {
    "Bancos Multiples": MultipleBanks(),
    "Bancos PyME": SmallAndMediumBanks(),
    "Entidades Financieras de Vivienda": FinancialHousingEntities(),
    "Cooperativas de Ahorro y Credito Abiertas": OpenSavingsAndCreditCooperatives(),
    "Instituciones Financieras de Desarrollo": DevelopmentFinancialInstitutions(),
    "Bancos de Desarrollo Productivo": ProductiveDevelopmentBanks(),
}

denominations = [key for key in current_denominations.keys()]

reportsNamesList = [
    "Estados Financieros",
    "Indicadores Financieros",
    "Captaciones",
    "Colocaciones",
    "Operaciones interbancarias",
    "Estados Financieros Evolutivos",
    "Indicadores Evolutivos",
    "Estados Financieros Desagregados",
    "Agencias, Sucursales, Nro de Empleados",
]

reportsLists: list[Bulletin]
bulletin_type = ""


list_months = [
    ("01", "ENERO"),
    ("02", "FEBRERO"),
    ("03", "MARZO"),
    ("04", "ABRIL"),
    ("05", "MAYO"),
    ("06", "JUNIO"),
    ("07", "JULIO"),
    ("08", "AGOSTO"),
    ("09", "SEPTIEMBRE"),
    ("10", "OCTUBRE"),
    ("11", "NOVIEMBRE"),
    ("12", "DICIEMBRE"),
]


def set_denomination(denomination: str):
    assign_reports_list(denomination)
    assign_bulletins(denomination)


def assign_reports_list(denomination: str):
    global reportsLists
    reportsLists = current_denominations[denomination].reportsLists


def assign_bulletins(denomination: str):
    global bulletin_type
    bulletin_type = denomination


def create_folder_bulletin(_year: str):
    os.mkdir(f"boletines/boletines-{_year}/{bulletin_type}")


def download_reports(_month: tuple, _year: str):
    successRate = 0
    os.mkdir(f"boletines/boletines-{_year}/{bulletin_type}/{_month[1]}")
    for i, reportsList in enumerate(reportsLists):
        if reportsList != []:
            os.mkdir(f"boletines/boletines-{_year}/{bulletin_type}/{_month[1]}/{reportsNamesList[i]}")
            for report in reportsList:
                durl = f"https://appweb.asfi.gob.bo/boletines_if/{_year}/{_month[0]}/{report[0]}_{report[1]}.zip"
                r = requests.get(durl, allow_redirects=True)
                if r.ok:
                    open(
                        f"boletines/boletines-{_year}/{bulletin_type}/{_month[1]}/{reportsNamesList[i]}/{report[1]}.zip",
                        "wb",
                    ).write(r.content)
                    successRate += 1
    return successRate


def getDate(_value: str, _example: str, _validation: tuple):
    print(
        f"Introduce un {_value} para obtener los boletines correspondientes, e.g. {_example}"
    )
    inputValue = input()
    if int(inputValue) >= _validation[0] and int(inputValue) <= _validation[1]:
        return inputValue
    return 0


def create_initial_folders(_year: str):
    if os.path.exists("boletines"):
        shutil.rmtree("boletines")
    os.mkdir(f"boletines")
    os.mkdir(f"boletines/boletines-{_year}")


def validator_of_year(_else_fn):
    year = getDate("año", "2023", (initial_year, current_year))
    if not year:
        print(f"ERROR: Por favor ingresa un año valido ({initial_year}-{current_year})")
    else:
        create_initial_folders(year)
        _else_fn(year)


def validator_of_month_and_year(_else_fn):
    month = getDate("mes", "8", (1, 12))
    if not month:
        print(f"ERROR: Por favor ingresa un mes valido (1-12)")
    else:
        month = int(month) - 1
        validator_of_year(_else_fn)


def error_no_data():
    print("ERROR: No se encontro data del mes y año especificados")

def download_multiple_bulletins(_year):
    for deno in denominations:
        set_denomination(deno)
        download_multiple_months(_year)

def download_multiple_months(_year):
    create_folder_bulletin(_year)
    for m in list_months:
        if not download_reports(m, _year):
            error_no_data()


def download_one_month(_year, _month):
    if not download_reports(list_months[_month], _year):
        error_no_data()


def download_most_recent(_year, _month):
    month = _month
    year = _year
    print(f"Buscando data de {list_months[month][1]} de {year}...")
    create_initial_folders(year)
    if not download_reports(list_months[month], year):
        print(
            f"ALERTA: Aun no hay data disponible para el mes de {list_months[month][1]} de {year}"
        )
        if os.path.exists(f"boletines/boletines-{year}/{list_months[month][1]}"):
            shutil.rmtree(f"boletines/boletines-{year}/{list_months[month][1]}")
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            print(f"¿Desea obtener data del mes anterior? (SI/NO)")
            respuesta = input()
            if respuesta == "SI":
                download_most_recent(year, month)
