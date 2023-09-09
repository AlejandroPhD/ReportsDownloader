from bulletins.bulletin import Bulletin


class FinancialHousingEntities(Bulletin):  # Entidades Financieras de Vivienda
    def __init__(self):
        estadosFinancierosList = [
            ("EFV", "EstadosFinancieros"),
        ]

        indicadoresFinancierosList = [
            ("EFV", "CalificacionCartera"),
            ("EFV", "IndicadoresFinancieros"),
            ("EFV", "PonderacionActivos"),
        ]

        captacionesList = [
            ("TOT", "DepositosPorMonedaYSubsistema"),
            ("SNB", "EncajeLegal"),
            ("EFV", "EstratificacionDepositos"),
            ("TOT", "NroCtasDeDepositosPorSubsistemaDepto"),
            ("EFV", "ObligCarteraContingente"),
            ("SIS2", "RankingDepositos"),
        ]

        colocacionesList = [
            ("TOT", "ClasifCarPorDeptoSubsistema"),
            ("TOT", "ClasifCarPorEstadoSubsistema"),
            ("EFV", "ClasifCarteraActividadEconomica"),
            ("EFV", "ClasifCarteraDestinoCredito"),
            ("EFV", "CarteraTipoGarantia"),
            ("EFV", "ClasifCarteraTipoCredito"),
            ("TOT", "CarteraPorMonedaYSubsistema"),
            ("EFV", "EstratifCarteraMontoNumeroPrestatarios"),
            ("TOT", "NroPrestatariosPorSubsistema"),
            ("SIS2", "RankingColocaciones"),
        ]

        operacionesInterbancariasList = [
            ("SIS2", "OperacionesInterbancarias"),
        ]

        estadosFinancierosEvolutivosList = [
            ("EFV", "EstadosFinancieros_Evolutivo"),
        ]

        indicadoresEvolutivosList = [
            ("EFV", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("EFV", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = []

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
