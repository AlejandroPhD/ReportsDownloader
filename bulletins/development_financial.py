from bulletins.bulletin import Bulletin


class DevelopmentFinancialInstitutions(
    Bulletin
):  # Instituciones Financieras de Desarrollo
    def __init__(self):
        estadosFinancierosList = [
            ("IFD", "EstadosFinancieros"),
            ("IFD", "EstadosFinancierosMoneda"),
        ]

        indicadoresFinancierosList = [
            ("IFD", "CalificacionCartera"),
            ("IFD", "CalificacionCartera"),
            ("IFD", "PonderacionActivos"),
        ]

        captacionesList = [
            ("TOT2", "DepositosPorMonedaYSubsistema"),
            ("IFD", "EstratificacionDepositos"),
            ("TOT2", "NroCtasDeDepositosPorSubsistemaDepto"),
            ("IFD", "ObligCarteraContingente"),
            ("SIS2", "RankingDepositos"),
        ]

        colocacionesList = [
            ("TOT2", "ClasifCarPorDeptoSubsistema"),
            ("TOT2", "ClasifCarPorEstadoSubsistema"),
            ("IFD", "ClasifCarteraActividadEconomica"),
            ("IFD", "ClasifCarteraTipoCredito"),
            ("IFD", "ClasifCarContDeptoEstadoDestino"),
            ("IFD", "ClasifCarContDeptoPlazoDestino"),
            ("IFD", "ClasifCarContEntidadEstadoDestino"),
            ("IFD", "ClasifCarContEntidadEstadoTipo"),
            ("IFD", "ClasifCarContTipoGarantia"),
            ("IFD", "ClasifCarContTipoObjCredito"),
            ("IFD", "ClasifContingActividadEconomica"),
            ("TOT2", "CarteraPorMonedaYSubsistema"),
            ("IFD", "EstratifCarContEntidadEstado"),
            ("IFD", "EstratifCarContMontoNumeroPrestatarios"),
            ("TOT2", "NroPrestatariosPorSubsistema"),
            ("SIS2", "RankingColocaciones"),
        ]

        operacionesInterbancariasList = [
            ("SIS2", "OperacionesInterbancarias"),
        ]

        estadosFinancierosEvolutivosList = [
            ("IFD", "EstadosFinancieros_Evolutivo"),
        ]

        indicadoresEvolutivosList = [
            ("IFD", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("IFD", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = [
            ("IFD", "PAFs_x_Depto"),
            ("IFD", "SucrAgenEmpl"),
        ]

        super().__init__(
            estadosFinancierosList,
            indicadoresFinancierosList,
            captacionesList,
            colocacionesList,
            operacionesInterbancariasList,
            estadosFinancierosEvolutivosList,
            indicadoresEvolutivosList,
            estadosFinancierosDesagregadosList,
            agenciasSucursalesNroEmpleadosList,
        )
