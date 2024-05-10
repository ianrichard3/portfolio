class Estado:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    # Getter nombre
    @property
    def nombre(self):
        # Executes this code when object.att
        return self.__nombre 

    # Setter nombre
    @nombre.setter
    def nombre(self, value):
        # Executes this code when object.att = value
        self.__nombre = value



if __name__ == "__main__":
    pass