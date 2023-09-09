from bulletins.bulletin import Bulletin


class ProductiveDevelopmentBanks(Bulletin):  # Bancos de Desarrollo Productivo
    def __init__(self):
        estadosFinancierosList = [
            ("BDR", "EstadosFinancieros"),
            ("BDR", "EstadosFinancierosMoneda"),
        ]

        indicadoresFinancierosList = [
            ("BDR", "CalificacionCartera"),
            ("BDR", "IndicadoresFinancieros"),
            ("BDR", "PonderacionActivos"),
        ]

        captacionesList = [
            ("TOT2", "DepositosPorMonedaYSubsistema"),
            ("BDR", "EstratificacionDepositos"),
            ("BDR", "EstratificacionDepositosTrimestral"),
            ("TOT2", "NroCtasDeDepositosPorSubsistemaDepto"),
            ("BDR", "ObligCarteraContingente"),
            ("SIS2", "RankingDepositos"),
        ]

        colocacionesList = [
            ("TOT2", "ClasifCarPorDeptoSubsistema"),
            ("TOT2", "ClasifCarPorEstadoSubsistema"),
            ("BDR", "ClasifCarteraActividadEconomica"),
            ("BDR", "ClasifCarteraDestinoCredito"),
            ("BDR", "ClasifCarteraTipoCredito"),
            ("BDR", "ClasifCarContDeptoEstadoDestino"),
            ("BDR", "ClasifCarContDeptoPlazoDestino"),
            ("BDR", "ClasifCarContEntidadEstadoDestino"),
            ("BDR", "ClasifCarContEntidadEstadoTipo"),
            ("BDR", "ClasifCarContTipoGarantia"),
            ("BDR", "ClasifCarContTipoObjCredito"),
            ("BDR", "ClasifContingActividadEconomica"),
            ("BDR", "ClasifContingDestinoCredito"),
            ("BDR", "ClasifContingDestinoCredito"),
            ("TOT2", "CarteraPorMonedaYSubsistema"),
            ("BDR", "EstratifCarContEntidadEstado"),
            ("BDR", "EstratifCarContMontoNumeroPrestatarios"),
            ("TOT2", "NroPrestatariosPorSubsistema"),
            ("SIS2", "RankingColocaciones"),
        ]

        operacionesInterbancariasList = [
            ("SIS2", "OperacionesInterbancarias"),
        ]

        estadosFinancierosEvolutivosList = []

        indicadoresEvolutivosList = [
            ("BDR", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("BDR", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = [
            ("BDR", "PAFs_x_Depto"),
            ("BDR", "SucrAgenEmpl"),
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
