# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editar_livros.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class editar_livros(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(772, 650)
        self.lista = QtWidgets.QListWidget(Form)
        self.lista.setGeometry(QtCore.QRect(10, 30, 271, 521))
        self.lista.setObjectName("lista")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.informacoes = QtWidgets.QLabel(Form)
        self.informacoes.setGeometry(QtCore.QRect(300, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.informacoes.setFont(font)
        self.informacoes.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.informacoes.setObjectName("informacoes")
        self.confirm_4 = QtWidgets.QPushButton(Form)
        self.confirm_4.setGeometry(QtCore.QRect(0, 610, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_4.setFont(font)
        self.confirm_4.setStyleSheet("QPushButton {\n"
"    background-color:White;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: Gray;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:Gray;\n"
"    border: 2px solid yellow;\n"
"}")
        self.confirm_4.setObjectName("confirm_4")
        self.informacoes_2 = QtWidgets.QLabel(Form)
        self.informacoes_2.setGeometry(QtCore.QRect(300, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.informacoes_2.setFont(font)
        self.informacoes_2.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.informacoes_2.setObjectName("informacoes_2")
        self.informacoes_3 = QtWidgets.QLabel(Form)
        self.informacoes_3.setGeometry(QtCore.QRect(300, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.informacoes_3.setFont(font)
        self.informacoes_3.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.informacoes_3.setObjectName("informacoes_3")
        self.informacoes_4 = QtWidgets.QLabel(Form)
        self.informacoes_4.setGeometry(QtCore.QRect(300, 220, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.informacoes_4.setFont(font)
        self.informacoes_4.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.informacoes_4.setObjectName("informacoes_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Livros"))
        self.informacoes.setText(_translate("Form", "TextLabel"))
        self.confirm_4.setText(_translate("Form", "Voltar"))
        self.informacoes_2.setText(_translate("Form", "TextLabel"))
        self.informacoes_3.setText(_translate("Form", "TextLabel"))
        self.informacoes_4.setText(_translate("Form", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Cria a aplicação
    Form = QtWidgets.QWidget()  # Cria o widget principal
    ui = editar_livros()  # Instancia a classe gerada
    ui.setupUi(Form)  # Aplica o layout à janela
    Form.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém a aplicação rodando