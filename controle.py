import re
from threading import Event
from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import cursor
from reportlab.pdfgen import canvas
from tkinter import *




banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "supernac"
)
def funcao_principal():

    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    
    categoria = ""

    if formulario.radioButton.isChecked():
        print ("CATEGORIA INFORMÁTICA FOI SELECIONADA!")
        categoria = "informática"
    if formulario.radioButton_2.isChecked():
        print ("CATEGORIA ALIMENTOS FOI SELECIONADA!")
        categoria = "alimentos"

    if formulario.radioButton_3.isChecked():
        print ("CATEGORIA ELETRÔNICOS FOI SELECIONADA!")
        categoria = "eletrônicos"

    print ("CÓDIGO:",linha1)
    print ("DESCRIÇÃO:",linha2)
    print ("PREÇO:",linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str (linha1), str (linha2), str (linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #limpado os componentes
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chama_segunda_tela():

    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tb_produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tb_produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos [linha][0]
    print (valor_id)
    cursor.execute("DELETE FROM produtos WHERE id ="+str(valor_id))
    banco.commit()



def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()    
    print ("PDF FOI GERADO COM SUCESSO!!!")
    cursor = banco.cursor()
    if segunda_tela.radioButton.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='alimentos'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()    
    if segunda_tela.radioButton_2.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='eletrônicos'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()    
    if segunda_tela.radioButton_3.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='informática'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()    
    if ordenar_categoria.radioButton.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='alimentos'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()        
    if ordenar_categoria.radioButton_2.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='eletrônicos'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()        
    if ordenar_categoria.radioButton_3.isChecked():
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='informática'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()        
    if  segunda_tela.pushButton_4.isChecked():

        comando_SQL = "SELECT * FROM produtos ORDER BY descricao"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()        



def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tb_produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))
    numero_id = valor_id



def salvar_valor_editado():
    global numero_id
    codigo = tela_editar.lineEdit.text()
    descricao = tela_editar.lineEdit_2.text()
    preco = tela_editar.lineEdit_3.text()
    categoria = tela_editar.lineEdit_4.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}' WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))
    banco.commit()

    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()



def ordenar_por_nome():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY descricao"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()        



def ordenar_por_preco():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos ORDER BY preco")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



def ordenar_por_categoria():
    segunda_tela.show()
    
    
    ordenar_categoria.show()
   


def categoria():
    segunda_tela.show()
    ordenar_categoria.show()
    cursor = banco.cursor()

    if ordenar_categoria.rdAlimentos.isChecked():
        print("A CATEGORIA ALIMENTOS FOI SELECIONADA !!!")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='alimentos'")
    if ordenar_categoria.rdEletronicos.isChecked():
        print("A CATEGORIA ELETRÔNICA FOI SELECIONADA !!! ")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='eletrônicos'")
    if ordenar_categoria.rdInformatica.isChecked():
        print ("A CATEGORIA INFORMÁTICA FOI SELECIONADA !!!")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='informatica'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    ordenar_categoria.close()
    


def ordenar_categoria2():
    segunda_tela.show()
    cursor = banco.cursor()
    
    if segunda_tela.radioButton.isChecked():
        print("A CATEGORIA ALIMENTOS FOI SELECIONADA !!!")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='alimentos'")
    if segunda_tela.radioButton_2.isChecked():
        print("A CATEGORIA ELETRÔNICA FOI SELECIONADA !!! ")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='eletrônicos'")
    if segunda_tela.radioButton_3.isChecked():
        print ("A CATEGORIA INFORMÁTICA FOI SELECIONADA !!!")
        comando_SQL = ("SELECT * FROM produtos WHERE categoria='informática'")
   
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))
    numero_id = valor_id



def salvar_valor_editado():
    global numero_id
    codigo = tela_editar.lineEdit.text()
    descricao = tela_editar.lineEdit_2.text()
    preco = tela_editar.lineEdit_3.text()
    categoria = tela_editar.lineEdit_4.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}' WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))
    banco.commit()

    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()
app=QtWidgets.QApplication([])



def relatorio2():
    segunda_tela.show()
    relatorio.show()



def relatorio_nome():
    segunda_tela.show()
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos ORDER BY descricao")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    y=0
    pdf = canvas.Canvas("relatório de produtos ordenados por nome.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(70,800, "Produtos ordenados por nome cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF GERADO COM SUCESSO")


def relatorio_preco():
    segunda_tela.show()
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos ORDER BY preco")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    y=0
    pdf = canvas.Canvas("relatório de produtos ordenados por preço.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF GERADO COM SUCESSO")
    

def relatorio_informatica():
    segunda_tela.show()
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'informatica'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    y=0
    pdf = canvas.Canvas("relatório de produtos de informática.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(125,800, "Produtos de informática cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF GERADO COM SUCESSO")
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()




def relatorio_eletronicos():
    segunda_tela.show()
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'eletrônicos'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    y=0
    pdf = canvas.Canvas("relatório de eletrônicos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(1354,800, "Produtos eletrônicos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF GERADO COM SUCESSO")
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()



def relatorio_alimentos():
    segunda_tela.show()
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'alimentos'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    y=0
    pdf = canvas.Canvas("relatório de alimentos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(115,800, "Produtos alimentícios cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF GERADO COM SUCESSO")
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()




def relatorio_tudo():

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y=0
    pdf = canvas.Canvas("relatório de todos os produtos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(130,800, "Todos os produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    pdf.save()    
    print ("PDF FOI GERADO COM SUCESSO")

def relatório_combo():
    cursor = banco.cursor()
    categoria = segunda_tela.comboBox.currentText()
    segunda_tela.label_5.setText("Categoria: "+ categoria)
    
    if segunda_tela.comboBox.currentIndex() == 0:
        comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'alimentos'")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        y=0
        pdf = canvas.Canvas("relatório de alimentos.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(115,800, "Produtos alimentícios cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
            pdf.save() 
            print("PDF DE ALIMENTOS GERADO COM SUCESSO")
    if segunda_tela.comboBox.currentIndex() == 1:         
        comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'eletrônicos'")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        y=0
        pdf = canvas.Canvas("relatório de eletrônicos.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(1354,800, "Produtos eletrônicos cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
            pdf.save() 
            print("PDF DE ELETRÔNICOS GERADO COM SUCESSO")
   
    if segunda_tela.comboBox.currentIndex() == 2:
        comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'informatica'")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        y=0
        pdf = canvas.Canvas("relatório de produtos de informática.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(125,800, "Produtos de informática cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
        pdf.save() 
        print("PDF DE INFORMÁTICA GERADO COM SUCESSO")
    if segunda_tela.comboBox.currentIndex() == 3:
        comando_SQL = ("SELECT * FROM produtos ORDER BY descricao")
        cursor.execute (comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
        y=0
        pdf = canvas.Canvas("relatório de produtos ordenados por nome.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(70,800, "Produtos ordenados por nome cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
        pdf.save() 
        print("PDF ORDENADO POR NOME GERADO COM SUCESSO")
    
    if segunda_tela.comboBox.currentIndex() == 4:
        comando_SQL = ("SELECT * FROM produtos ORDER BY preco")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
        y=0
        pdf = canvas.Canvas("relatório de produtos ordenados por preço.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(200,800, "Produtos cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
        pdf.save() 
        print("PDF ORDENADO POR PREÇO GERADO COM SUCESSO")
        
    if segunda_tela.comboBox.currentIndex() == 5:
        comando_SQL = ("SELECT * FROM produtos")
        cursor.execute (comando_SQL)
        dados_lidos = cursor.fetchall()
        y=0
        pdf = canvas.Canvas("relatório de todos os produtos.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(130,800, "Todos os produtos cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
        pdf.save()    
        print ("PDF DE TODOS OS PRODUTOS FOI GERADO COM SUCESSO")

def relatorio_nome_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos ORDER BY descricao")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    y=0
    pdf = canvas.Canvas("relatório de produtos ordenados por nome.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(70,800, "Produtos ordenados por nome cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF ORDENADO POR NOME GERADO COM SUCESSO")


def relatorio_preco_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos ORDER BY preco")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    y=0
    pdf = canvas.Canvas("relatório de produtos ordenados por preço.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF ORDENADO POR PREÇO GERADO COM SUCESSO")
def relatorio_informatica_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'informatica'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    y=0
    pdf = canvas.Canvas("relatório de produtos de informática.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(125,800, "Produtos de informática cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF DE INFORMÁTICA GERADO COM SUCESSO")
def relatorio_eletronicos_menu():
        segunda_tela.show()
        cursor = banco.cursor()
        comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'eletrônicos'")
    
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        y=0
        pdf = canvas.Canvas("relatório de eletrônicos.pdf")
        pdf.setFont("Times-Bold",25)
        pdf.drawString(1354,800, "Produtos eletrônicos cadastrados:")
        pdf.setFont("Times-Bold",18)
        pdf.setStrokeColorRGB(0.2,0.5,0.3)
        pdf.setFillColorRGB(0,100,0)
        pdf.drawString(110,750,"Código")
        pdf.drawString(210,750,"Produto")
        pdf.drawString(410,750, "Preço")
        pdf.drawString(510,750, "Categoria")
        pdf.drawString(10,750,"ID")

        for i in range(0,len(dados_lidos)):
            y = y + 50
            pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
            pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
            pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
            pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
            pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
        pdf.save() 
        print("PDF DE ELETRONICOS GERADO COM SUCESSO")


def relatorio_alimentos_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM produtos WHERE categoria = 'alimentos'")
    
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    y=0
    pdf = canvas.Canvas("relatório de alimentos.pdf")
    pdf.setFont("Times-Bold",25)
    pdf.drawString(115,800, "Produtos alimentícios cadastrados:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(110,750,"Código")
    pdf.drawString(210,750,"Produto")
    pdf.drawString(410,750, "Preço")
    pdf.drawString(510,750, "Categoria")
    pdf.drawString(10,750,"ID")

    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(110,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,750 - y,str (dados_lidos[i][2]))
        pdf.drawString(510,750 - y,str (dados_lidos[i][3]))
        pdf.drawString(10,750 - y,str (dados_lidos[i][4]))
    
    
    pdf.save() 
    print("PDF DE ALIMENTOS GERADO COM SUCESSO")
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()






    
          

   
    



formulario=uic.loadUi( "formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
tela_editar = uic.loadUi("editar_produto.ui")
ordenar_categoria = uic.loadUi("ordenar_categoria.ui")
relatorio = uic.loadUi("gerar_relatorio.ui")

formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.actionEditar_2.triggered.connect(editar_dados)
segunda_tela.actionExcluir.triggered.connect(excluir_dados)
segunda_tela.actionNome.triggered.connect(relatorio_nome_menu)
segunda_tela.actionPre_o.triggered.connect(relatorio_preco_menu)
segunda_tela.actionAlimentos.triggered.connect(relatorio_alimentos_menu)
segunda_tela.actionEletr_nicos.triggered.connect(relatorio_eletronicos_menu)
segunda_tela.actionInform_tica.triggered.connect(relatorio_informatica_menu)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)
segunda_tela.pushButton_4.clicked.connect(ordenar_por_nome)
segunda_tela.pushButton_5.clicked.connect(ordenar_por_preco)
segunda_tela.pushButton_6.clicked.connect(ordenar_por_categoria)
segunda_tela.radioButton.clicked.connect(ordenar_categoria2)
segunda_tela.radioButton_2.clicked.connect(ordenar_categoria2)
segunda_tela.radioButton_3.clicked.connect(ordenar_categoria2)
segunda_tela.pushButton_8.clicked.connect(relatorio2)
segunda_tela.comboBox.addItems(["Alimentos","Eletrônicos","Informática","Nome","Preço","Tudo"])
segunda_tela.pushButton_9.clicked.connect(relatório_combo)
relatorio.pushButton.clicked.connect(relatorio_nome)
relatorio.pushButton_2.clicked.connect(relatorio_preco)
relatorio.pushButton_3.clicked.connect(relatorio_informatica)
relatorio.pushButton_4.clicked.connect(relatorio_alimentos)
relatorio.pushButton_5.clicked.connect(relatorio_eletronicos)
relatorio.pushButton_6.clicked.connect(relatorio_tudo)
ordenar_categoria.radioButton.clicked.connect(categoria)
ordenar_categoria.radioButton_2.clicked.connect(categoria)
ordenar_categoria.radioButton_3.clicked.connect(categoria)



formulario.show()
app.exec()


  