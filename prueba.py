import requests
import os
import shutil

if os.path.exists("reportes"):
    shutil.rmtree("reportes")

if os.path.exists("tempCodeRunnerFile.py"):
    os.remove("tempCodeRunnerFile.py")

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

print("Introduce un anio para obtener los reportes correspondientes, e.g. 2023")
year = input()

os.mkdir(f"reportes")
os.mkdir(f"reportes/reportes-{year}")


for month in list_months:
    os.mkdir(f"reportes/reportes-{year}/{month[1]}")
    for i, reportsList in enumerate(reportsLists):
        os.mkdir(f"reportes/reportes-{year}/{month[1]}/{reportsNamesList[i]}")
        for report in reportsList:
            durl = f"https://appweb.asfi.gob.bo/boletines_if/{year}/{month[0]}/{report[0]}_{report[1]}.zip"
            r = requests.get(durl, allow_redirects=True)
            if r.ok:
                open(
                    f"reportes/reportes-{year}/{month[1]}/{reportsNamesList[i]}/{report[1]}.zip",
                    "wb",
                ).write(r.content)
