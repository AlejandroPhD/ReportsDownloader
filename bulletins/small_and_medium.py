from bulletins.bulletin import Bulletin


class SmallAndMediumBanks(Bulletin):  # Bancos pequeños y medianos
    def __init__(self):
        estadosFinancierosList = [
            ("BPY", "EstadosFinancieros"),
            ("BPY", "EstadosFinancierosMoneda"),
        ]

        indicadoresFinancierosList = [
            ("BPY", "CalificacionCartera"),
            ("BPY", "IndicadoresFinancieros"),
            ("BPY", "PonderacionActivos"),
        ]

        captacionesList = [
            ("TOT2", "DepositosPorMonedaYSubsistema"),
            ("BPY", "RankingDepositosPublico"),
            ("BPY", "EncajeLegal"),
            ("BPY", "EstratificacionDepositos"),
            ("BPY", "EstratificacionDepositosTrimestral"),
            ("BPY", "EvolucionCaptaciones"),
            ("TOT2", "NroCtasDeDepositosPorSubsistemaDepto"),
            ("BPY", "ObligCarteraContingente"),
            ("SIS2", "RankingDepositos"),
        ]

        colocacionesList = [
            ("TOT2", "ClasifCarPorDeptoSubsistema"),
            ("TOT2", "ClasifCarPorEstadoSubsistema"),
            ("BPY", "ClasifCarteraActividadEconomica"),
            ("BPY", "ClasifCarteraDestinoCredito"),
            ("BPY", "ClasifCarteraTipoCredito"),
            ("BPY", "ClasifCarContDeptoEstadoDestino"),
            ("BPY", "ClasifCarContDeptoPlazoDestino"),
            ("BPY", "ClasifCarContEntidadEstadoDestino"),
            ("BPY", "ClasifCarContEntidadEstadoTipo"),
            ("BPY", "ClasifCarContEntidadPlazoDestino"),
            ("BPY", "ClasifCarContTipoGarantia"),
            ("BPY", "ClasifCarContTipoObjCredito"),
            ("BPY", "ClasifContingActividadEconomica"),
            ("BPY", "ClasifContingDestinoCredito"),
            ("BPY", "ClasifContingTipoCredito"),
            ("TOT2", "CarteraPorMonedaYSubsistema"),
            ("BPY", "EstratifCarContEntidadEstado"),
            ("BPY", "EstratifCarContMontoNumeroPrestatarios"),
            ("BPY", "EvolucionCartera"),
            ("BPY", "FinanciamientosExternos"),
            ("TOT2", "NroPrestatariosPorSubsistema"),
            ("SIS2", "RankingColocaciones"),
            ("BPY", "RankingContingente"),
        ]

        operacionesInterbancariasList = [
            ("SIS2", "OperacionesInterbancarias"),
        ]

        estadosFinancierosEvolutivosList = [
            ("BPY", "EstadosFinancieros_Evolutivo"),
        ]

        indicadoresEvolutivosList = [
            ("BPY", "IndicadoresFinancieros_Evolutivo"),
        ]

        estadosFinancierosDesagregadosList = [
            ("BPY", "EstadosFinancierosDesagregados"),
        ]

        agenciasSucursalesNroEmpleadosList = [
            ("BPY", "PAFs_x_Depto"),
            ("BPY", "SucrAgenEmpl"),
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
