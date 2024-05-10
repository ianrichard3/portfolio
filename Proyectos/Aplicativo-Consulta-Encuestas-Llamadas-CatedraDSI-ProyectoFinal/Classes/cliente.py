class Cliente:
    def __init__(self, dni: str, nombre_completo: str, nro_celular: str):
        # atributos propios
        self.__dni = dni
        self.__nombre_completo = nombre_completo
        self.__nro_celular = nro_celular

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter dni
    @property
    def dni(self):
        # Executes this code when object.att
        return self.__dni 

    # Setter dni
    @dni.setter
    def dni(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__dni = value

    # Getter nombre_completo
    @property
    def nombre_completo(self):
        # Executes this code when object.att
        return self.__nombre_completo

    # Setter nombre_completo
    @nombre_completo.setter
    def nombre_completo(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__nombre_completo = value

    # Getter nro_celular
    @property
    def nro_celular(self):
        # Executes this code when object.att
        return self.__nro_celular

    # Setter nro_celular
    @nro_celular.setter
    def nro_celular(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__nro_celular = value

if __name__ == "__main__":
    pass