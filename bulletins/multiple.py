from bulletins.bulletin import Bulletin


class MultipleBanks(Bulletin): # Bancos Múltiples
    def __init__(self):
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
            ("BMU", "EstratificacionDepositosTrimestral"),
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
        ]

        estadosFinancierosEvolutivosList = [
            ("BMU", "EstadosFinancieros_Evolutivo"),
        ]

        indicadoresEvolutivosList = [
            ("BMU", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("BMU", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = [
            ("BMU", "PAFs_x_Depto"),
            ("BMU", "SucrAgenEmpl"),
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
