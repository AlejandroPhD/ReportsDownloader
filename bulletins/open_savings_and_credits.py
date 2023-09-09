from bulletins.bulletin import Bulletin


class OpenSavingsAndCreditCooperatives(
    Bulletin
):  # Cooperativas de Ahorro y Crédito Abiertas
    def __init__(self):
        estadosFinancierosList = [
            ("COO", "EstadosFinancieros"),
        ]

        indicadoresFinancierosList = [
            ("COO", "CalificacionCartera"),
            ("COO", "IndicadoresFinancieros"),
            ("COO", "PonderacionActivos"),
        ]

        captacionesList = [
            ("TOT", "DepositosPorMonedaYSubsistema"),
            ("SNB", "EncajeLegal"),
            ("COO", "EstratificacionDepositos"),
            ("TOT", "NroCtasDeDepositosPorSubsistemaDepto"),
            ("COO", "ObligCarteraContingente"),
            ("SIS2", "RankingDepositos"),
        ]

        colocacionesList = [
            ("TOT", "ClasifCarPorDeptoSubsistema"),
            ("TOT", "ClasifCarPorEstadoSubsistema"),
            ("COO", "ClasifCarteraActividadEconomica"),
            ("COO", "ClasifCarteraDestinoCredito"),
            ("COO", "ClasifCarteraTipoGarantia"),
            ("COO", "ClasifCarteraTipoGarantia"),
            ("TOT", "CarteraPorMonedaYSubsistema"),
            ("COO", "EstratifCarteraMontoNumeroPrestatarios"),
            ("TOT", "NroPrestatariosPorSubsistema"),
            ("SIS2", "RankingColocaciones"),
        ]

        operacionesInterbancariasList = [
            ("SIS2", "OperacionesInterbancarias"),
        ]

        estadosFinancierosEvolutivosList = [
            ("COO", "EstadosFinancieros_Evolutivo"),
        ]

        indicadoresEvolutivosList = [
            ("COO", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("COO", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = [
            ("COO", "PAFs_x_Depto"),
            ("MCO", "SucrAgenEmpl"),
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
