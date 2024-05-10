from datetime import date, datetime


def from_string_to_date(date_string: str, date_format: str = "%d/%m/%Y"):
    try:
        return datetime.strptime(date_string, date_format).date()
    except ValueError as error:
        print(error)
        return




def from_date_to_string(date_value: date, date_format: str = "%d/%m/%Y"):

    # return datetime.strftime(date_value , date_format)
    return date_value.strftime(date_format)


def from_call_dictionary_to_string(dictionary):
    operador = dictionary.get("operador")
    fecha = from_date_to_string(dictionary.get("fecha"))
    string = f"Operador: {operador}".ljust(30) + f"Fecha: {fecha}"
    return string


# def from_call_string_get_call_object(string, calls):
#     for c in calls:
#         dic = {"operador": c.descripcion_operador,
#          "fecha": c.get_fecha_inicio()}
#         if from_call_dictionary_to_string(dic) == string:
#             return c
#     return False
    








if __name__ == "__main__":
    d = {'operador': 'Operador2', 'fecha': date(2022, 5, 3)}
    print(from_call_dictionary_to_string(d))
# d1 = date(year=1999, month=2, day=23)
# d2 = date(year=2003, month=7, day=21)

# print(d2 - d1)

# formato_fecha = "%d/%m/%Y"

# fecha_1 = "20/03/2010"
# fecha_2 = "31/03/2017"


# fecha_a_buscar = "17/09/1008"


# date_fecha_1 = datetime.strptime(fecha_1, formato_fecha)
# date_fecha_2 = datetime.strptime(fecha_2, formato_fecha) 

# date_fecha_buscar = datetime.strptime(fecha_a_buscar, formato_fecha)


# print(date_fecha_1 < date_fecha_buscar < date_fecha_2)

