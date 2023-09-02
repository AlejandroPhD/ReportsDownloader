import requests
import os
import shutil
import datetime

initial_year = 1990
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

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

estadosFinancierosList = [
    ("BMU", "EstadosFinancieros"),
    ("BMU", "EstadosFinancierosMoneda"),
]

indicadoresFinancierosList = [
    ("BMU", "CalificacionCartera"),
    ("BMU", "IndicadoresFinancieros"),
    ("BMU", "PonderacionActivos"),
]

captacionesList = [
    ("TOT2", "DepositosPorMonedaYSubsistema"),
    ("BMU", "RankingDepositosPublico"),
    ("BMU", "EncajeLegal"),
    ("BMU", "EstratificacionDepositos"),
    ("BMU", "EvolucionCaptaciones"),
    ("TOT2", "NroCtasDeDepositosPorSubsistemaDepto"),
    ("BMU", "ObligCarteraContingente"),
    ("SIS2", "RankingDepositos"),
]

colocacionesList = [
    ("TOT2", "ClasifCarPorDeptoSubsistema"),
    ("TOT2", "ClasifCarPorEstadoSubsistema"),
    ("BMU", "ClasifCarteraActividadEconomica"),
    ("BMU", "ClasifCarteraDestinoCredito"),
    ("BMU", "ClasifCarteraTipoCredito"),
    ("BMU", "ClasifCarContDeptoEstadoDestino"),
    ("BMU", "ClasifCarContDeptoPlazoDestino"),
    ("BMU", "ClasifCarContEntidadEstadoDestino"),
    ("BMU", "ClasifCarContEntidadEstadoTipo"),
    ("BMU", "ClasifCarContEntidadPlazoDestino"),
    ("BMU", "ClasifCarContTipoGarantia"),
    ("BMU", "ClasifCarContTipoObjCredito"),
    ("BMU", "ClasifContingActividadEconomica"),
    ("BMU", "ClasifContingDestinoCredito"),
    ("BMU", "ClasifContingTipoCredito"),
    ("TOT2", "CarteraPorMonedaYSubsistema"),
    ("BMU", "EstratifCarContEntidadEstado"),
    ("BMU", "EstratifCarContMontoNumeroPrestatarios"),
    ("BMU", "EvolucionCartera"),
    ("BMU", "FinanciamientosExternos"),
    ("TOT2", "NroPrestatariosPorSubsistema"),
    ("SIS2", "RankingColocaciones"),
    ("BMU", "RankingContingente"),
]

operacionesInterbancariasList = [
    ("SIS2", "OperacionesInterbancarias"),
    ("BMU", "EstadosFinancieros_Evolutivo"),
    ("BMU", "IndicadoresFinancieros_Evolutivo"),
    ("BMU", "EstadosFinancierosDesagregados"),
    ("BMU", "PAFs_x_Depto"),
    ("BMU", "SucrAgenEmpl"),
]

reportsLists = [
    estadosFinancierosList,
    indicadoresFinancierosList,
    captacionesList,
    colocacionesList,
    operacionesInterbancariasList,
]


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


def download_reports(_month: tuple, _year: str):
    successRate = 0
    os.mkdir(f"reportes/reportes-{_year}/{_month[1]}")
    for i, reportsList in enumerate(reportsLists):
        os.mkdir(
            f"reportes/reportes-{_year}/{_month[1]}/{reportsNamesList[i]}")
        for report in reportsList:
            durl = f"https://appweb.asfi.gob.bo/boletines_if/{_year}/{_month[0]}/{report[0]}_{report[1]}.zip"
            r = requests.get(durl, allow_redirects=True)
            if r.ok:
                open(
                    f"reportes/reportes-{_year}/{_month[1]}/{reportsNamesList[i]}/{report[1]}.zip",
                    "wb",
                ).write(r.content)
                successRate += 1
    return successRate


def getDate(_value: str, _example: str, _validation: tuple):
    print(
        f"Introduce un {_value} para obtener los reportes correspondientes, e.g. {_example}")
    inputValue = input()
    if int(inputValue) >= _validation[0] and int(inputValue) <= _validation[1]:
        return inputValue
    return 0


def create_initial_folders(_year: str):
    if os.path.exists("reportes"):
        shutil.rmtree("reportes")
    os.mkdir(f"reportes")
    os.mkdir(f"reportes/reportes-{_year}")


def validator_of_year(_else_fn):
    year = getDate("año", "2023", (initial_year, current_year))
    if not year:
        print(
            f"ERROR: Por favor ingresa un año valido ({initial_year}-{current_year})")
    else:
        create_initial_folders(year)
        _else_fn(year)

def validator_of_month_and_year(_else_fn):
    month = getDate("mes", "8", (1, 12))
    if not month:
        print(f"ERROR: Por favor ingresa un mes valido (1-12)")
    else:
        month = int(month) - 1
        validator_of_year(_else_fn, month)


def error_no_data():
    print("ERROR: No se encontro data del mes y año especificados")


def download_multiple_months(_year):
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
            f"ALERTA: Aun no hay data disponible para el mes de {list_months[month][1]} de {year}")
        if os.path.exists(f"reportes/reportes-{year}/{list_months[month][1]}"):
            shutil.rmtree(f"reportes/reportes-{year}/{list_months[month][1]}")
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            print(f"¿Desea obtener data del mes anterior? (SI/NO)")
            respuesta = input()
            if respuesta == "SI":
                download_most_recent(year, month)