class Bulletin:
    def __init__(
        self,
        estadosFinancierosList,
        indicadoresFinancierosList,
        captacionesList,
        colocacionesList,
        operacionesInterbancariasList,
        estadosFinancierosEvolutivosList,
        indicadoresEvolutivosList,
        estadosFinancierosDesagregadosList,
        agenciasSucursalesNroEmpleadosList,
    ):
        self.reportsLists = [
            estadosFinancierosList,
            indicadoresFinancierosList,
            captacionesList,
            colocacionesList,
            operacionesInterbancariasList,
            estadosFinancierosEvolutivosList,
            indicadoresEvolutivosList,
            estadosFinancierosDesagregadosList,
            agenciasSucursalesNroEmpleadosList,
        ]
    
