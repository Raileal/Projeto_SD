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
        self.ano = QtWidgets.QLineEdit(Form)
        self.ano.setGeometry(QtCore.QRect(300, 240, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.ano.setFont(font)
        self.ano.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.ano.setText("")
        self.ano.setObjectName("ano")
        self.autor = QtWidgets.QLineEdit(Form)
        self.autor.setGeometry(QtCore.QRect(300, 100, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.autor.setFont(font)
        self.autor.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.autor.setText("")
        self.autor.setObjectName("autor")
        self.Titulo = QtWidgets.QLineEdit(Form)
        self.Titulo.setGeometry(QtCore.QRect(300, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.Titulo.setText("")
        self.Titulo.setObjectName("Titulo")
        self.paginas = QtWidgets.QLineEdit(Form)
        self.paginas.setGeometry(QtCore.QRect(300, 170, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.paginas.setFont(font)
        self.paginas.setStyleSheet("background-color: lightblue; /* Azul claro */\n"
"")
        self.paginas.setText("")
        self.paginas.setObjectName("paginas")
        self.confirm_5 = QtWidgets.QPushButton(Form)
        self.confirm_5.setGeometry(QtCore.QRect(300, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_5.setFont(font)
        self.confirm_5.setStyleSheet("QPushButton {\n"
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
        self.confirm_5.setObjectName("confirm_5")
        self.confirm_6 = QtWidgets.QPushButton(Form)
        self.confirm_6.setGeometry(QtCore.QRect(540, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_6.setFont(font)
        self.confirm_6.setStyleSheet("QPushButton {\n"
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
        self.confirm_6.setObjectName("confirm_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Livros"))
        self.confirm_4.setText(_translate("Form", "Voltar"))
        self.confirm_5.setText(_translate("Form", "Concluir"))
        self.confirm_6.setText(_translate("Form", "Excluir"))
