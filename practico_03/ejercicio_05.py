# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from ejercicio_01 import reset_tabla, check_exists, execute_query
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    
    if not check_exists(id_persona):
        return False
    
    update_query = """
    UPDATE Persona
    SET id = ?, name = ?, birth_date = ?, DNI = ?, altura = ?
    WHERE id = ?;
    """

    parameters = (id_persona, 
                  nombre, 
                  datetime.datetime.strftime(nacimiento, '%Y-%m-%d'),
                  dni, 
                  altura, 
                  id_persona)

    return execute_query(update_query, parameters)


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
