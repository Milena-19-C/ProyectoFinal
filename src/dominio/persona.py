class Persona:
    def __init__(self, id=None, usuario='', clave=''):
        self._id = id
        self._usuario = usuario
        self._clave = clave

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    def __str__(self):
        return f'Persona: {self.__dict__}'

if __name__ == '__main__':
    p = Persona(id='1', usuario='Fernando', clave='123456')
    print(p)

