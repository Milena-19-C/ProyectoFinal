# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##


## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(706, 567)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnNuevo = QPushButton(self.centralwidget)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(160, 320, 75, 28))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btnNuevo.setFont(font)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(490, 320, 75, 28))
        self.btnLimpiar.setFont(font)
        self.btnBorrarRegistro = QPushButton(self.centralwidget)
        self.btnBorrarRegistro.setObjectName(u"btnBorrarRegistro")
        self.btnBorrarRegistro.setGeometry(QRect(350, 320, 121, 28))
        self.btnBorrarRegistro.setFont(font)
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(250, 320, 78, 28))
        self.btnActualizar.setFont(font)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(110, 60, 358, 26))
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.lbBuscarUsuario = QLabel(self.splitter_3)
        self.lbBuscarUsuario.setObjectName(u"lbBuscarUsuario")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lbBuscarUsuario.setFont(font1)
        self.splitter_3.addWidget(self.lbBuscarUsuario)
        self.txtBuscarUsuario = QLineEdit(self.splitter_3)
        self.txtBuscarUsuario.setObjectName(u"txtBuscarUsuario")
        self.txtBuscarUsuario.setMaxLength(20)
        self.splitter_3.addWidget(self.txtBuscarUsuario)
        self.btnBuscarUsuario = QPushButton(self.splitter_3)
        self.btnBuscarUsuario.setObjectName(u"btnBuscarUsuario")
        self.btnBuscarUsuario.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btnBuscarUsuario.setIcon(icon)
        self.splitter_3.addWidget(self.btnBuscarUsuario)
        self.cbUsuario = QComboBox(self.centralwidget)
        self.cbUsuario.addItem("")
        self.cbUsuario.addItem("")
        self.cbUsuario.addItem("")
        self.cbUsuario.addItem("")
        self.cbUsuario.setObjectName(u"cbUsuario")
        self.cbUsuario.setGeometry(QRect(200, 210, 261, 22))
        self.lbUsuario = QLabel(self.centralwidget)
        self.lbUsuario.setObjectName(u"lbUsuario")
        self.lbUsuario.setGeometry(QRect(90, 204, 79, 22))
        self.lbUsuario.setFont(font1)
        self.lbClave = QLabel(self.centralwidget)
        self.lbClave.setObjectName(u"lbClave")
        self.lbClave.setGeometry(QRect(90, 177, 91, 22))
        self.lbClave.setFont(font1)
        self.lbUsuarioid = QLabel(self.centralwidget)
        self.lbUsuarioid.setObjectName(u"lbUsuarioid")
        self.lbUsuarioid.setGeometry(QRect(88, 150, 101, 22))
        self.lbUsuarioid.setFont(font1)
        self.txtUsuarioid = QLineEdit(self.centralwidget)
        self.txtUsuarioid.setObjectName(u"txtUsuarioid")
        self.txtUsuarioid.setGeometry(QRect(200, 150, 261, 21))
        self.txtUsuarioid.setMaxLength(10)
        self.txtClave = QLineEdit(self.centralwidget)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setGeometry(QRect(200, 180, 261, 21))
        self.txtClave.setMaxLength(50)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 706, 22))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gestion del Personal", None))
        self.btnNuevo.setText(QCoreApplication.translate("vtnPrincipal", u"Nuevo", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.btnBorrarRegistro.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar Registro", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtnPrincipal", u"Actualizar", None))
        self.lbBuscarUsuario.setText(QCoreApplication.translate("vtnPrincipal", u"Buscar por Usuario:", None))
        self.btnBuscarUsuario.setText("")
        self.cbUsuario.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbUsuario.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Administrador", None))
        self.cbUsuario.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Operador", None))
        self.cbUsuario.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Invitado", None))

        self.lbUsuario.setText(QCoreApplication.translate("vtnPrincipal", u"Usuario:", None))
        self.lbClave.setText(QCoreApplication.translate("vtnPrincipal", u"Clave:", None))
        self.lbUsuarioid.setText(QCoreApplication.translate("vtnPrincipal", u"UsuarioID:", None))
    # retranslateUi

