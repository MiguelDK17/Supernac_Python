from tkinter import Canvas, PhotoImage, Variable
from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas


app = QtWidgets.QApplication([])
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cadastro_pessoas"
)
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.comboBox.currentText()
    linha7 = formulario.lineEdit_7.text()
    linha8 = formulario.lineEdit_8.text()
    linha9 = formulario.lineEdit_9.text()

    print ("CPF-CNPJ:",linha1)
    print ("Nome:",linha2)
    print ("Endereço:",linha3)
    print ("Bairro:",linha4)
    print ("Cidade:",linha5)
    print ("Estado:",linha6)
    print ("Telefone:",linha7)
    print ("Email:",linha8)
    print ("Tipo:",linha9)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tb_pessoas (cpf_cnpj,nome,endereço,bairro,cidade,estado,telefone,email,tipo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str (linha1),str (linha2),str (linha3),str (linha4),str (linha5),str(linha6),str(linha7),str (linha8),str (linha9))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.comboBox.currentText()
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
def Sair():
    formulario.close()
def Sair_da_Segunda_Tela():
    segunda_tela.close()
def chama_segunda_tela():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tb_pessoas"
    cursor.execute(comando_SQL)
    dados_lidos=cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute ("SELECT codigo FROM tb_pessoas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos [linha] [0]
    print (valor_id)
    cursor.execute ("DELETE FROM tb_pessoas WHERE codigo="+str(valor_id))
    banco.commit()

def chama_ordenar():
    ordenar_pessoas.show()
    segunda_tela.show()
def ordenar_por_cpf_cnpj():
    
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY cpf_cnpj")
    cursor.execute (comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def Sair_ordenar():
    ordenar_pessoas.close()
def ordenar_por_tipo():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY tipo")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_nome():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY nome")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_endereco():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY endereço")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_bairro():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY bairro")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_cidade():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY cidade")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_estado():
    cursor = banco.cursor()
    comnado_SQL = ("SELECT * FROM tb_pessoas ORDER BY estado")
    cursor.execute(comnado_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_telefone():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY telefone")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_email():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY email")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()  
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def relatório_botao():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y=0
    pdf = canvas.Canvas("relatório de pessoas.pdf")
    pdf.scale(0.4,1.0)
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Pessoas cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"CPF/CNPJ")
    pdf.drawString(310,750, "Tipo")
    pdf.drawString(410,750, "Nome")
    pdf.drawString(510,750,"Endereço")
    pdf.drawString(600,750,"Bairro")
    pdf.drawString(710,750,"Cidade")
    pdf.drawString(810,750,"Estado")
    pdf.drawString(910,750,"Telefone")
    pdf.drawString(1010,750,"Email")
    

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(310,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][4]))
        pdf.drawString(600,750 - y,str(dados_lidos[i][5]))
        pdf.drawString(710,750 - y,str(dados_lidos[i][6]))
        pdf.drawString(810,750 - y,str(dados_lidos[i][7]))
        pdf.drawString(910,750 - y,(dados_lidos[i][8]))
        pdf.drawString(1010,750 - y,str(dados_lidos[i][9]))
    pdf.save()    
    print ("PDF DE PESSOAS CADASTRADAS FOI GERADO COM SUCESSO!!!")
    class slaok():
        print("hello")

            
           
    
            





formulario=uic.loadUi("formulario_pessoas.ui")
segunda_tela=uic.loadUi("listar_pessoas.ui")
ordenar_pessoas=uic.loadUi("Ordenar_Por.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.comboBox.addItems(["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RR","RO","RJ","RN","RS","SC","SP","SE","TO"])
formulario.pushButton_3.clicked.connect(Sair)
segunda_tela.btExcluirPessoas.clicked.connect(excluir_dados)
segunda_tela.pushButton_2.clicked.connect(Sair_da_Segunda_Tela)
segunda_tela.pushButton_3.clicked.connect(relatório_botao)
segunda_tela.pushButton_5.clicked.connect(chama_ordenar)
ordenar_pessoas.pushButton.clicked.connect(ordenar_por_cpf_cnpj)
ordenar_pessoas.pushButton_2.clicked.connect(ordenar_por_tipo)
ordenar_pessoas.pushButton_3.clicked.connect(ordenar_por_nome)
ordenar_pessoas.pushButton_4.clicked.connect(ordenar_por_endereco)
ordenar_pessoas.pushButton_5.clicked.connect(ordenar_por_bairro)
ordenar_pessoas.pushButton_6.clicked.connect(ordenar_por_cidade)
ordenar_pessoas.pushButton_7.clicked.connect(ordenar_por_estado)
ordenar_pessoas.pushButton_8.clicked.connect(ordenar_por_telefone)
ordenar_pessoas.pushButton_9.clicked.connect(ordenar_por_email)
ordenar_pessoas.pushButton_10.clicked.connect(Sair_ordenar)
formulario.show()
app.exec()