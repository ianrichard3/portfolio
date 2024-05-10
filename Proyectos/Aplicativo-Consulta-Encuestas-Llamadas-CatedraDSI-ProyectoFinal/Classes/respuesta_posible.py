class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.__descripcion = descripcion
        self.__valor = valor

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter descripcion
    @property
    def descripcion(self):
        # Executes this code when object.att
        return self.__descripcion
    
    # Setter descripcion
    @descripcion.setter
    def descripcion(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__descripcion = value
    
    # Getter valor
    @property
    def valor(self):
        # Executes this code when object.att
        return self.__valor
    
    # Setter valor
    @valor.setter
    def valor(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__valor = value
