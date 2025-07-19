from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.UI.vtnPrincipal import Ui_vtnPrincipal
from src.datos.personaDao import PersonaDao
from src.dominio.persona import Persona
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()

        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)

        # Conexión de botones
        self.ui.btnNuevo.clicked.connect(self.nuevo)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscarUsuario.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnBorrarRegistro.clicked.connect(self.borrar_registro)

        # Validaciones para campos exactamente de 10 caracteres alfanuméricos
        regex_9_10 = QRegularExpression("^[a-zA-Z0-9]{9,10}$")  # entre 9 y 10 caracteres alfanuméricos
        validador_flexible = QRegularExpressionValidator(regex_9_10)

        self.ui.txtUsuarioid.setValidator(validador_flexible)
        self.ui.txtBuscarUsuario.setValidator(validador_flexible)

    def nuevo(self):
        usuarioid = self.ui.txtUsuarioid.text()
        usuario = self.ui.cbUsuario.currentText()
        clave = self.ui.txtClave.text()

        if not usuarioid or not usuario or not clave:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese todos los datos.')
            return

        if len(usuarioid) != 10:
            QMessageBox.warning(self, 'Advertencia', 'UsuarioID debe tener exactamente 10 caracteres alfanuméricos.')
            return

        persona = Persona(
            id=usuarioid,
            usuario=usuario,
            clave=clave
        )

        if PersonaDao.insertar_persona(persona) == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo guardar el usuario.')
        else:
            self.ui.statusbar.showMessage('Usuario guardado correctamente.', 3000)
            self.limpiar()

    def buscar(self):
        usuarioid = self.ui.txtBuscarUsuario.text().strip()

        if not usuarioid:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el ID de usuario a buscar.')
            return

        if len(usuarioid) < 9 or len(usuarioid) > 10:
            QMessageBox.warning(self, 'Advertencia', 'El ID debe tener entre 9 y 10 caracteres alfanuméricos.')
            return

        persona = PersonaDao.seleccionar_persona_por_id(usuarioid)
        if persona:
            self.ui.cbUsuario.setCurrentText(persona.usuario)
            self.ui.txtClave.setText(persona.clave)
            self.ui.txtUsuarioid.setText(str(persona.id))
        else:
            QMessageBox.information(self, 'Información', 'Usuario no encontrado.')

    def actualizar(self):
        if QMessageBox.question(self, 'Confirmación', '¿Desea actualizar el registro?') == QMessageBox.Yes:
            usuarioid = self.ui.txtUsuarioid.text().strip()
            usuario = self.ui.cbUsuario.currentText()
            clave = self.ui.txtClave.text()

            if not usuarioid or not usuario or not clave:
                QMessageBox.warning(self, 'Advertencia', 'Complete todos los campos.')
                return

            if len(usuarioid) < 9 or len(usuarioid) > 10:
                QMessageBox.warning(self, 'Advertencia', 'UsuarioID debe tener entre 9 y 10 caracteres alfanuméricos.')
                return

            persona = Persona(
                id=usuarioid,
                usuario=usuario,
                clave=clave
            )

            if PersonaDao.actualizar_persona(persona) == -1:
                QMessageBox.critical(self, 'Error', 'No se pudo actualizar.')
            else:
                self.ui.statusbar.showMessage('Usuario actualizado correctamente.', 3000)
                self.limpiar()

    def borrar_registro(self):
        usuarioid = self.ui.txtUsuarioid.text().strip()

        if not usuarioid:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el ID del usuario.')
            return

        if len(usuarioid) < 9 or len(usuarioid) > 10:
            QMessageBox.warning(self, 'Advertencia', 'UsuarioID debe tener entre 9 y 10 caracteres alfanuméricos.')
            return

        confirmacion = QMessageBox.question(
            self,
            'Confirmación',
            f'¿Está seguro de eliminar el usuario con ID: {usuarioid}?',
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.Yes:
            resultado = PersonaDao.eliminar_persona_por_id(usuarioid)
            if resultado == -1:
                QMessageBox.critical(self, 'Error', 'No se pudo eliminar el usuario.')
            else:
                self.ui.statusbar.showMessage('Usuario eliminado correctamente.', 3000)
                self.limpiar()


    def limpiar(self):
        self.ui.txtUsuarioid.clear()
        self.ui.cbUsuario.setCurrentIndex(-1)  # O 0 si tienes un valor por defecto
        self.ui.txtClave.clear()
        self.ui.txtBuscarUsuario.clear()

