import sys
from PySide6.QtWidgets import QApplication
from src.servicio.persona import PersonaServicio

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vtn_principal = PersonaServicio()
    vtn_principal.show()
    sys.exit(app.exec())


