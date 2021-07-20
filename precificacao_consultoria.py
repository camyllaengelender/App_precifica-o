# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'precificacao_consultoria.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import pandas as pd

font= QFont("Arial",10)
font1= QFont("Arial",10)
font1.setBold(True)
font2= QFont("Arial",14)
font2.setBold(True)
font3= QFont("Arial",12)
font3.setBold(True)


class Ui_Consultoria (object):
       
    def setupUi(self, PrecificacaodeConsultoria):
        PrecificacaodeConsultoria.setObjectName("PrecificacaodeConsultoria")
        PrecificacaodeConsultoria.resize(849, 555)
        
        
       # PrecificacaodeConsultoria.setObjectName("C:\icon/ajf.png")
        
        self.image = QtWidgets.QLabel(None, PrecificacaodeConsultoria)
        self.image.setPixmap(QPixmap("C:\icon/Logotipo1.png"))
        self.image.move(720,500)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../../icon/ajf.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        PrecificacaodeConsultoria.setWindowIcon(icon)
        
        
        
        
        
        '''
        self.icon = QtWidgets.QLabel(None, PrecificacaodeConsultoria)
        self.icon.setPixmap(QPixmap("C:\icon/ajf.png"))
        '''
        
        
        
        '''
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\icon/ajf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ObjectIcon(None,icon)
        '''
        
        
        
        
        PrecificacaodeConsultoria.setStyleSheet("QDialog{\n"
"background-color:green\n"
"}")
    
        '''
        self.textEdit = QtWidgets.QTextEdit(PrecificacaodeConsultoria)
        self.textEdit.setGeometry(QtCore.QRect(370, 10, 211, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Descricao da Consultoria")
        '''
        self.lineEdit_3 = QtWidgets.QLineEdit(PrecificacaodeConsultoria)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 10, 211, 101))
        self.lineEdit_3.setObjectName("lineEdit")
        self.lineEdit_3.setPlaceholderText("Descricao da Consultoria")
        
        self.lineEdit = QtWidgets.QLineEdit(PrecificacaodeConsultoria)
        self.lineEdit.setGeometry(QtCore.QRect(190, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Nome do contratante")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(PrecificacaodeConsultoria)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 50, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Nome do membro reponsavel")
        
        self.dateEdit = QtWidgets.QDateEdit(PrecificacaodeConsultoria)
        self.dateEdit.setGeometry(QtCore.QRect(190, 80, 141, 21))
        self.dateEdit.setObjectName("dateEdit")
        
        self.groupBox = QtWidgets.QGroupBox(PrecificacaodeConsultoria)
        self.groupBox.setGeometry(QtCore.QRect(30, 130, 241, 231))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet("color: white")
        
        self.tamanho_da_area = QtWidgets.QLabel(self.groupBox)
        self.tamanho_da_area.setGeometry(QtCore.QRect(20, 30, 901, 16))
        self.tamanho_da_area.setObjectName("label")
        self.tamanho_da_area.setFont(font)
                
      #  self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
       # self.layoutWidget1.setGeometry(QtCore.QRect(15, 40, 253, 27))
        #self.layoutWidget1.setObjectName("layoutWidget1")
        
       # self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
       # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
       # self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.radioButton.setObjectName("radioButton")
      #  self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton.setFont(font)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 50, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setFont(font)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 70, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setFont(font)
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(150, 90, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setFont(font)
         
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 151, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
         
        
        self.consultores_custo_consultoria = QtWidgets.QSpinBox(self.groupBox)
        self.consultores_custo_consultoria.setGeometry(QtCore.QRect(170, 140, 42, 22))
        self.consultores_custo_consultoria.setObjectName("spinBox")
        self.consultores_custo_consultoria.setFont(font1)
        self.consultores_custo_consultoria.setStyleSheet("color: black")
        
        
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 470, 13))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet("color: white")
      #  self.label_6.move(100,460)
        self.label_6.setObjectName("label_6")
             
        self.groupBox_2 = QtWidgets.QGroupBox(PrecificacaodeConsultoria)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 130, 241, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet("color: white")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        
        self.consultores_alimentacao = QtWidgets.QSpinBox(self.groupBox_2)
        self.consultores_alimentacao.setGeometry(QtCore.QRect(180, 30, 42, 22))
        self.consultores_alimentacao.setObjectName("spinBox_2")
        self.consultores_alimentacao.setFont(font1)
        self.consultores_alimentacao.setStyleSheet("color: black")
        
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 120, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("color: black")
        self.lineEdit_3.setPlaceholderText('R$ 25.00')
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        
        self.refeicoes_dia = QtWidgets.QSpinBox(self.groupBox_2)
        self.refeicoes_dia.setGeometry(QtCore.QRect(180, 80, 42, 22))
        self.refeicoes_dia.setObjectName("spinBox_3")
        self.refeicoes_dia.setFont(font1)
        self.refeicoes_dia.setStyleSheet("color: black")
        
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 501, 21))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font1)
        
        self.groupBox_3 = QtWidgets.QGroupBox(PrecificacaodeConsultoria)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 130, 261, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet("color: white")
        
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font)
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 30, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("color: black")
           
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font)
                
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 60, 61, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setStyleSheet("color: black")
        self.lineEdit_5.setPlaceholderText('R$ 0.95')
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 90, 61, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setStyleSheet("color: black")
        self.lineEdit_6.setPlaceholderText('R$ 35.00')        
        
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 130, 16))
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font)
        
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 131, 21))
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(font)
        
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 120, 61, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setStyleSheet("color: black")
        self.lineEdit_7.setPlaceholderText('0.00 Km')
        
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 130, 13))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(font1)
    
        self.calcular_1 = QtWidgets.QPushButton(PrecificacaodeConsultoria)
        self.calcular_1.setGeometry(QtCore.QRect(29, 365, 75, 23))
        self.calcular_1.setObjectName("calcular_1")
        self.calcular_1.clicked.connect(self.calc_1)
        
        self.calcular_2 = QtWidgets.QPushButton(PrecificacaodeConsultoria)
        self.calcular_2.setGeometry(QtCore.QRect(290, 365, 75, 23))
        self.calcular_2.setObjectName("calcular_2")
        self.calcular_2.clicked.connect(self.calc_2)
        
        self.calcular_3 = QtWidgets.QPushButton(PrecificacaodeConsultoria)
        self.calcular_3.setGeometry(QtCore.QRect(570, 365, 75, 23))
        self.calcular_3.setObjectName("calcular_3")
        self.calcular_3.clicked.connect(self.calc_3)
        
        self.calcular = QtWidgets.QPushButton(PrecificacaodeConsultoria)
        self.calcular.setGeometry(QtCore.QRect(190, 500, 75, 23))
    #    self.calcular.setMinimumSize(QtCore.QSize(0, 50))
     #   self.calcular.setMaximumSize(QtCore.QSize(16777215, 50))
        self.calcular.setObjectName("calcular")
       # self.resp_calcular = QtWidgets.QLabel(self.groupBox)
        self.calcular.clicked.connect(self.calc)
        
        self.salvar = QtWidgets.QPushButton(PrecificacaodeConsultoria)
        self.salvar.setGeometry(QtCore.QRect(275, 500, 75, 23))
        self.salvar.setObjectName("salvar")
        self.salvar.clicked.connect(self.save)
        
        self.label_13 = QtWidgets.QLabel(PrecificacaodeConsultoria)
        self.label_13.setGeometry(QtCore.QRect(430, 410, 470, 103))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet("color: white")
        
        
        self.label_20 = QtWidgets.QLabel(PrecificacaodeConsultoria)
        self.label_20.setGeometry(QtCore.QRect(680, 20, 130, 22))
        self.label_20.setObjectName("label_20")
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet("color: orange")
        
        self.label_21 = QtWidgets.QLabel(PrecificacaodeConsultoria)
        self.label_21.setGeometry(QtCore.QRect(660, 40, 180, 22))
        self.label_21.setObjectName("label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet("color: white")
        
        self.label_22 = QtWidgets.QLabel(PrecificacaodeConsultoria)
        self.label_22.setGeometry(QtCore.QRect(670, 60, 180, 22))
        self.label_22.setObjectName("label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet("color: white")

        a = 50000

        self.retranslateUi(PrecificacaodeConsultoria)
        QtCore.QMetaObject.connectSlotsByName(PrecificacaodeConsultoria)

    def retranslateUi(self,PrecificacaodeConsultoria):
        
        _translate = QtCore.QCoreApplication.translate
        PrecificacaodeConsultoria.setWindowTitle(_translate("PrecificacaodeConsultoria", "Precificacao de Consultoria"))
        '''
        self.colorLabel=QLabel(self)
        self.colorLabel.resize(1400,800)
        self.colorLabel.setStyleSheet("background-color: green")
        '''
        self.groupBox.setTitle(_translate("PrecificacaodeConsultoria", "Custo da Consultoria"))
        self.tamanho_da_area.setText(_translate("PrecificacaodeConsultoria", "Tamanho da area:"))
        self.radioButton.setText(_translate("PrecificacaodeConsultoria", "< 1ha"))
        self.radioButton_2.setText(_translate("PrecificacaodeConsultoria", "1 a 5ha"))
        self.radioButton_3.setText(_translate("PrecificacaodeConsultoria", "5 a 30ha"))
        self.radioButton_4.setText(_translate("PrecificacaodeConsultoria", "> 30ha"))
        self.label_2.setText(_translate("PrecificacaodeConsultoria", "Numero de consultores:"))
        self.label_6.setText(_translate("PrecificacaodeConsultoria", "Subtotal:"))
        self.calcular_1.setText(_translate("PrecificacaodeConsultoria", "Calcular"))
                
        
        self.groupBox_2.setTitle(_translate("PrecificacaodeConsultoria", "Alimentacao"))
        self.label_3.setText(_translate("PrecificacaodeConsultoria", "Numero de consultores:"))
        self.label_4.setText(_translate("PrecificacaodeConsultoria", "Valor medio da refeicao:"))
        self.label_5.setText(_translate("PrecificacaodeConsultoria", "Numero de refeicoes/dia:"))
        self.label_7.setText(_translate("PrecificacaodeConsultoria", "Subtotal:"))
        self.calcular_2.setText(_translate("PrecificacaodeConsultoria", "Calcular"))
        
        self.groupBox_3.setTitle(_translate("PrecificacaodeConsultoria", "Transporte"))
        self.label_8.setText(_translate("PrecificacaodeConsultoria", "Aluguel do carro:"))
        self.label_9.setText(_translate("PrecificacaodeConsultoria", "Combustivel + depreciacao:"))
        self.label_10.setText(_translate("PrecificacaodeConsultoria", "Limpeza do carro:"))
        self.label_11.setText(_translate("PrecificacaodeConsultoria", "Distancia do local: "))
        self.label_12.setText(_translate("PrecificacaodeConsultoria", "Subtotal:"))
        self.calcular_3.setText(_translate("PrecificacaodeConsultoria", "Calcular"))
        
        self.calcular.setText(_translate("PrecificacaodeConsultoria", "Calcular"))
        self.salvar.setText(_translate("PrecificacaodeConsultoria", "Salvar"))
        self.label_13.setText(_translate("PrecificacaodeConsultoria", "Total:"))
        
        self.label_20.setText(_translate("PrecificacaodeConsultoria", "Cuidado!!!"))
        self.label_21.setText(_translate("PrecificacaodeConsultoria", "nao utilize virgula(0,5)"))
        self.label_22.setText(_translate("PrecificacaodeConsultoria", "somente ponto(0.5)"))
        
   
    
    def calc_1 (self, PrecificacaodeConsultoria):
        global c, area, consultores
        
        consultores = self.consultores_custo_consultoria.value()
        c = float(consultores)
           
        
        test=''
        
        
        if self.radioButton.isChecked():
            area=3
            textarea = '1ha'
        elif self.radioButton_2.isChecked():
            area=5
            textarea = '1 a 5ha'
        elif self.radioButton_3.isChecked():
            area=7
            textarea = '5 a 30ha'
        elif self.radioButton_4.isChecked():
            area=9
            textarea = '> 30ha'
        else:
            self.label_6.setText('Selecione o tamanho da area')
            self.label_6.setStyleSheet("color: yellow")
            self.label_6.setFont(font3)
            self.label_6.move(10,200)
            self.label_6.resize(300,20)
            
               
        if consultores == test:
            pass
        else:
            resultado = (area*30)
            self.label_6.setText('Subtotal: R$' + str(resultado))
            self.label_6.setStyleSheet("color: white")
            self.label_6.setFont(font1)
            self.label_6.resize(300,20)
            #self.label_6.move(200,400)
        
        print(resultado)
        
        
    def calc_2 (self, PrecificacaodeConsultoria): 
        global a, b, c, d
        '''
        aluguel = self.lineEdit_4.text()
        a = str(aluguel)
        
        combust = self.lineEdit_5.text()
        b = str(combust)
        
        limpeza = self.lineEdit_6.text()
        c = str(limpeza)
        
        distancia = self.lineEdit_7.text()
        d = str(distancia)
        
        b * d + c + a
        combust * distancia + limpeza + aluguel
        '''
        
        a = float(self.lineEdit_4.text())
        b = float(self.lineEdit_5.text())
        c = float(self.lineEdit_6.text())
        d = float(self.lineEdit_7.text())
        
        b * d + c + a
        
        print(b * d + c + a)
        
        test = " "
        
        if a == test:
            self.label_12.setText('Indique o valor do aluguel')
            self.label_12.setStyleSheet("color: yellow")
            self.label_12.setFont(font1)
            self.label_12.resize(300,20)
            
     
            
            
        else:
            resultado = b * d + c + a
            self.label_12.setText('Subtotal: R$' + str(resultado))
            self.label_12.setStyleSheet("color: white")
            self.label_12.setFont(font1)
            self.label_12.resize(300,20)
            
            
        
        
    def calc_3 (self, PrecificacaodeConsultoria):
        global e, f, g
        
        consult = self.consultores_alimentacao.value()
        e = float(consult)
        
        refeicoesdia = self.refeicoes_dia.value()
        f = float(refeicoesdia)
        
        g = float(self.lineEdit_3.text())
        
        e * f * g
        
        print(e * f * g)
        
        test=''
        
        if e == test:
            pass
        else:
            resultado = e * f * g
            self.label_7.setText('Subtotal: R$' + str(resultado))
            self.label_7.setStyleSheet("color: white")
            self.label_7.setFont(font1)
            self.label_7.resize(300,20)
        
    def calc (self, PrecificacaodeConsultoria):
         (area*30)+(b * d + c + a) + (e * f * g)
         
         print((area*30)+(b * d + c + a) + (e * f * g))
         
         
         test=''
         
         if e == test:
            pass
         else:
            resultado = (area*30) + (b * d + c + a) + (e * f * g)
            self.label_13.setText('Total: R$' + str(resultado))
            self.label_13.setStyleSheet("color: white")
            self.label_13.setFont(font2)
           # self.label_13.resize(300,20)

    def save (self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        # descricao = self.textEdit.setPlaceholderText()
        
       #A descricao = self.lineEdit.text()
        data=self.dateEdit.text()
            #editor=self.editor.textedit()
          
        dados = [[name],[surname],[data],[area],[consultores],[a],[b],[c],[d],[e],[f],[g]]
        colunas  = ['Dados']
        index =['Contratante', 'Membro Preci.','Data','Tamanho da Area','Membros Participando','Aluguel do carro', 'Combustivel+Depreciacao', 'Limpeza','Distancia','Valor da Refeicao','M. Trabalhando','Refeicoes/dia',]
        df = pd.DataFrame(data=dados, columns=colunas, index=index)
        print(df)
        name = QFileDialog.getSaveFileName(None, 'Save File')
        df.to_csv(name[0]+'.csv')
            
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrecificacaodeConsultoria = QtWidgets.QDialog()
    ui = Ui_Consultoria()
    ui.setupUi(PrecificacaodeConsultoria)
    PrecificacaodeConsultoria.show()
    sys.exit(app.exec_())
    

