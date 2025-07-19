from src.datos.conexion import Conexion
from src.dominio.persona import Persona

class PersonaDao:
    _ERROR = -1
    _INSERT = "INSERT INTO Persona(usuarioid, usuario, clave) VALUES (?, ?, ?)"
    _SELECT = "SELECT id, usuario, clave FROM Persona WHERE id = ?"
    _UPDATE = "UPDATE Persona SET usuario = ?, clave = ? WHERE id = ?"
    _DELETE = "DELETE FROM Persona WHERE UsuarioID = ?"

    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.id, persona.usuario, persona.clave)
                registros = cursor.execute(cls._INSERT, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al insertar persona: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_persona_por_id(cls, usuario_id):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (usuario_id,)
                registro = cursor.execute("SELECT UsuarioID, usuario, clave FROM Persona WHERE UsuarioID = ?",
                                          datos).fetchone()
                print(registro)  # ← para ver si llega algo

                if registro:
                    persona = Persona(
                        id=registro[0],
                        usuario=registro[1],
                        clave=registro[2]
                    )
                    return persona
                else:
                    return None
        except Exception as e:
            print(f"Error al consultar persona: {e}")
            return None

    @classmethod
    def actualizar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.usuario, persona.clave, persona.id)
                registros = cursor.execute(
                    "UPDATE Persona SET usuario = ?, clave = ? WHERE UsuarioID = ?",
                    datos
                )
                return registros.rowcount
        except Exception as e:
            print(f"Error al actualizar persona: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def eliminar_persona_por_id(cls, usuario_id):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (usuario_id,)
                registros = cursor.execute(cls._DELETE, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al eliminar persona: {e}")
            cursor.rollback()
            return cls._ERROR

# Solo para prueba
if __name__ == '__main__':
    p = Persona(id='1', usuario='FerchoAdmin', clave='123456')
    r = PersonaDao.actualizar_persona(p)
    print(r)
