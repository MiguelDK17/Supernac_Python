import os
import sys
from ast import Module
from cProfile import run
from hashlib import new
from pathlib import Path
from re import T
from sys import modules
from tkinter import Canvas, Scrollbar, dialog
from tokenize import String
from typing import Any
from xml.etree.ElementInclude import include
from colorama import Cursor

import mysql.connector
from mysqlx import View
from PyQt5 import (QtCore, QtGui, QtWebEngine, QtWebEngineWidgets, QtWidgets,
                   uic)
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from reportlab.pdfgen import canvas

app = QtWidgets.QApplication([])
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "supernac"
)
def funcao_login():
    global nome_usuario
    nome_usuario = tela_login.edt_usuario.text()
    edt_senha = tela_login.edt_senha.text()
    cursor = banco.cursor()
    comando_Login = ("SELECT usuario,senha FROM tb_pessoas WHERE usuario = '{}' AND senha = '{}';".format(nome_usuario,edt_senha))
    cursor.execute(comando_Login)
    
    for (usuario,senha) in cursor:
        if nome_usuario == usuario and edt_senha == senha:
            tela_principal.show()
        else: 
            tela_login.tv_Login.setText("Nome de usuario ou senha incorretos")
            #ela_principal.show()
       
def logout():
    tela_principal.close()
    tela_login.show()
def controle():
        tela_pessoas.show()
def funcao_principal():
    linha1 = tela_pessoas.lineEdit.text()
    linha2 = tela_pessoas.lineEdit_2.text()
    linha3 = tela_pessoas.lineEdit_3.text()
    linha4 = tela_pessoas.lineEdit_4.text()
    linha5 = tela_pessoas.lineEdit_5.text()
    linha6 = tela_pessoas.comboBox.currentText()
    linha7 = tela_pessoas.lineEdit_7.text()
    linha8 = tela_pessoas.lineEdit_8.text()
    linha9 = tela_pessoas.lineEdit_9.text()
    linha10 = tela_pessoas.lineEdit_6.text()
    linha11 = tela_pessoas.lineEdit_10.text()

    print ("CPF-CNPJ:",linha1)
    print ("Nome:",linha2)
    print ("Endereço:",linha3)
    print ("Bairro:",linha4)
    print ("Cidade:",linha5)
    print ("Estado:",linha6)
    print ("Telefone:",linha7)
    print ("Email:",linha8)
    print ("Tipo:",linha9)
    print("Usuario",linha10)
    print("Senha:",linha11)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tb_pessoas (cpf_cnpj,nome,endereço,bairro,cidade,estado,telefone,email,tipo,usuario,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str (linha1),str (linha2),str (linha3),str (linha4),str (linha5),str(linha6),str(linha7),str (linha8),str (linha9),str (linha10), str (linha11))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    tela_pessoas.lineEdit.setText("")
    tela_pessoas.lineEdit_2.setText("")
    tela_pessoas.lineEdit_3.setText("")
    tela_pessoas.lineEdit_4.setText("")
    tela_pessoas.lineEdit_5.setText("")
    tela_pessoas.comboBox.currentText()
    tela_pessoas.lineEdit_7.setText("")
    tela_pessoas.lineEdit_8.setText("")
    tela_pessoas.lineEdit_9.setText("")
    tela_pessoas.lineEdit_6.setText("")
    tela_pessoas.lineEdit_10.setText("")
def Sair():
    tela_pessoas.close()
def Sair_da_Segunda_Tela():
    tela_principal_pessoas.close()
def chama_tela_principal_pessoas():
    tela_principal_pessoas.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tb_pessoas"
    cursor.execute(comando_SQL)
    dados_lidos=cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(12)
    for i in range(0,len(dados_lidos)):
        for j in range (0,12):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def excluir_dados():
    linha = tela_principal_pessoas.tableWidget.currentRow()
    tela_principal_pessoas.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute ("SELECT codigo FROM tb_pessoas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos [linha] [0]
    print (valor_id)
    cursor.execute ("DELETE FROM tb_pessoas WHERE codigo="+str(valor_id))
    banco.commit()

def chama_ordenar():
    ordenar_pessoas.show()
    tela_principal_pessoas.show()
def ordenar_por_cpf_cnpj():
    
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY cpf_cnpj")
    cursor.execute (comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def Sair_ordenar():
    ordenar_pessoas.close()
def ordenar_por_tipo():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY tipo")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_nome():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY nome")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_endereco():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY endereço")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_bairro():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY bairro")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_cidade():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY cidade")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range (0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_estado():
    cursor = banco.cursor()
    comnado_SQL = ("SELECT * FROM tb_pessoas ORDER BY estado")
    cursor.execute(comnado_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_telefone():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY telefone")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ordenar_por_email():
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_pessoas ORDER BY email")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()  
    tela_principal_pessoas.tableWidget.setRowCount(len(dados_lidos))
    tela_principal_pessoas.tableWidget.setColumnCount(10)
    for i in range(0,len(dados_lidos)):
        for j in range(0,10):
            tela_principal_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

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
    

    print("ABAIXO CADASTRO DE PRODUTOS")











def controle_produtos():
    tela_produtos.show()
def funcao_principal_produtos():
    

    linha1 = tela_produtos.lineEdit.text()
    linha2 = tela_produtos.lineEdit_2.text()
    linha3 = tela_produtos.lineEdit_3.text()
    linha4 = tela_produtos.lineEdit_4.text()

    
    categoria = ""

    if tela_produtos.radioButton.isChecked():
        print ("CATEGORIA INFORMÁTICA FOI SELECIONADA!")
        categoria = "informática"
    if tela_produtos.radioButton_2.isChecked():
        print ("CATEGORIA ALIMENTOS FOI SELECIONADA!")
        categoria = "alimentos"
    if tela_produtos.radioButton_3.isChecked():
        print ("CATEGORIA ELETRÔNICOS FOI SELECIONADA!")
        categoria = "eletrônicos"
    if tela_produtos.radioButton_4.isChecked():
        categoria = "jogos"    

    print ("CÓDIGO:",linha1)
    print ("DESCRIÇÃO:",linha2)
    print ("PREÇO:",linha3)
    print ("QUANTIDADE:",linha4)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tb_produtos (codigo,descricao,preco,quantidade,categoria) VALUES (%s,%s,%s,%s,%s)"
    dados = (str (linha1), str (linha2), str (linha3),str (linha4), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #limpado os componentes
    tela_produtos.lineEdit.setText("")
    tela_produtos.lineEdit_2.setText("")
    tela_produtos.lineEdit_3.setText("")
    tela_produtos.lineEdit_4.setText("")
def Sair_Produtos():
    tela_produtos.close()


def chama_segunda_tela():

    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tb_produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(6)
    for i in range(0, len(dados_lidos)):
        for j in range(0,6):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def excluir_dados_produtos():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tb_produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos [linha][0]
    print (valor_id)
    cursor.execute("DELETE FROM tb_produtos WHERE id ="+str(valor_id))
    banco.commit()
def Sair_dados_produtos():
    segunda_tela.close()

def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    
    cursor.execute("SELECT id FROM tb_produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tb_produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][4]))
    tela_editar.lineEdit_5.setText(str(produto[0][5]))
    tela_editar.lineEdit_6.setText(str(produto[0][3]))
    

    numero_id = valor_id



def salvar_valor_editado():
    global numero_id
    codigo = tela_editar.lineEdit.text()
    descricao = tela_editar.lineEdit_2.text()
    preco = tela_editar.lineEdit_3.text()
    quantidade = tela_editar.lineEdit_6.text()
    categoria = tela_editar.lineEdit_4.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE tb_produtos SET codigo = '{}', descricao = '{}', preco = '{}',quantidade = '{}', categoria = '{}' WHERE id = {}".format(codigo,descricao,preco,quantidade,categoria,numero_id))
    banco.commit()

    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()





def relatório_combo():
    cursor = banco.cursor()
    categoria = segunda_tela.cbCategoria.currentText()
    segunda_tela.label_5.setText("Categoria: "+ categoria)
    
    if segunda_tela.cbCategoria.currentIndex() == 0:
        comando_SQL = ("SELECT * FROM tb_produtos WHERE categoria = 'alimentos'")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        
   
    if segunda_tela.cbCategoria.currentIndex() == 2:
        comando_SQL = ("SELECT * FROM tb_produtos WHERE categoria = 'informatica'")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
        
    if segunda_tela.cbCategoria.currentIndex() == 3:
        comando_SQL = ("SELECT * FROM tb_produtos ORDER BY descricao")
        cursor.execute (comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
        
    if segunda_tela.cbCategoria.currentIndex() == 4:
        comando_SQL = ("SELECT * FROM tb_produtos ORDER BY preco")
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
        
        
    if segunda_tela.cbCategoria.currentIndex() == 5:
        comando_SQL = ("SELECT * FROM tb_produtos")
        cursor.execute (comando_SQL)
        dados_lidos = cursor.fetchall()
       
    
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(5)
        for i in range(0, len(dados_lidos)):
            for j in range(0,5):
                segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    


def relatorio_nome_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_produtos ORDER BY descricao")
    
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
    comando_SQL = ("SELECT * FROM tb_produtos ORDER BY preco")
    
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
def relatorio_preco_menu():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = ("SELECT * FROM tb_produtos ORDER BY preco")
    
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
    comando_SQL = ("SELECT * FROM tb_produtos WHERE categoria = 'informatica'")
    
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
        comando_SQL = ("SELECT * FROM tb_produtos WHERE categoria = 'eletrônicos'")
    
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
    comando_SQL = ("SELECT * FROM tb_produtos WHERE categoria = 'alimentos'")
    
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
    comando_SQL = "SELECT * FROM tb_produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
def Vendas():
        tela_vendas.show()
        cursor = banco.cursor()
        comando_SQL = "SELECT codigo,descricao,preco,quantidade,categoria,id FROM tb_produtos"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        cursor.fetchall()

def Vendas_Informações():
    tela_vendas.show()
    global numero_id



#def buscaProdutoNome():
           
            
            # Abrindo a Sessao
            
            #cursor = banco.cursor()
            #nome =  tela_vendas.edtNome.text()
            
            
            #sql = ("SELECT codigo,preco from tb_produtos WHERE descricao = '{}'".format(nome))

            #cursor.execute(sql)
            
            #for (codigo, preco) in cursor:
                
                #if tela_vendas.edtQuantidade.text() == "":
                    #print("Tem que ter pelo menos um valor em Quantidade para que o programa prossiga")
                    #exit()
                #else:
                    #quantidade_final = int(tela_vendas.edtQuantidade.text())
                    #tela_vendas.edtTotalItem.setText(str(preco))
                    #valor_inicial = float(preco)
                    #tela_vendas.edtCodigo.setText(str(codigo))
                    #total = valor_inicial * quantidade_final
                    #tela_vendas.listNome.addItem(nome)
                    #tela_vendas.listTotal.addItem(str(total))
                    #preco_temp=float(tela_vendas.edtTotalGeral.text())
                    #total_temp = preco_temp + valor_inicial
                    #tela_vendas.edtTotalGeral.setText(str(total_temp))
                    #print (total_temp)
                    
                    
                            
               

def buscaProdutoCodigo():
    if tela_vendas.edtNome.text() == "":
        cursor = banco.cursor()
        codigo = tela_vendas.edtCodigo.text()
        edtPreco = tela_vendas.edtTotalItem.text()
    
        sql = ("SELECT descricao,preco,quantidade from tb_produtos WHERE codigo = '{}'".format(codigo))
        cursor.execute(sql)
    
    
    
   

        for(descricao,preco,quantidade) in cursor:
            if quantidade == 0:
                cursor = banco.cursor()
                comando_SQL = ("DELETE FROM tb_produtos WHERE quantidade = 0")
                cursor.execute(comando_SQL)
                print("Esse produto acabou")
            
            
            else:    
                cursor = banco.cursor()
                comando_SQL_Dois = "SELECT codigo,descricao,preco,quantidade,categoria,id FROM tb_produtos"
                cursor.execute(comando_SQL_Dois)
                dados_lidos = cursor.fetchall()
                tela_vendas.edtNome.setText("")
                nome = tela_vendas.edtNome.setText(str(descricao))
                tela_vendas.edtTotalItem.setText(str(preco))
            
        if tela_vendas.edtTotalItem.text() == "":
            tela_vendas.tvInformacao.setText("Este produto não existe ou acabou")
        else:
            tela_vendas.tvInformacao.setText("")        
            valor_inicial = float(preco)         
            tela_vendas.listTotal.addItem(str(valor_inicial))
            tela_vendas.listNome.addItem(str(descricao))
            preco_temp=float(tela_vendas.edtTotalGeral.text())
            total_temp = preco_temp + valor_inicial
            tela_vendas.edtTotalGeral.setText(str(total_temp))
            quant_temp = int(quantidade)
            total_quant = quant_temp - 1
            cursor = banco.cursor()   
            comando_SQL_Três = ("UPDATE tb_produtos SET quantidade = '{}' WHERE codigo = '{}'".format(total_quant,codigo))
            cursor.execute(comando_SQL_Três)
            banco.commit()
            
            nome = tela_vendas.edtNome.text()
            preco = tela_vendas.edtTotalItem.text()
            codigo = tela_vendas.edtCodigo.text()
            cursor=banco.cursor()
            comando_Inserir = ("INSERT INTO venda (nome,preco,codigo) VALUES (%s,%s,%s)")
            dados = (str(nome),str(preco),str(codigo))
            cursor.execute(comando_Inserir,dados)
            banco.commit()
            print(nome)
            
            
            nome = tela_vendas.edtNome.text()
            
            print(total_quant)
    
            
            #tela_vendas.edtCodigo.setText("")
            #tela_vendas.edtTotalItem.setText("")
    
    
    
    elif tela_vendas.edtCodigo.text() == "":
        #Aqui Começa o Eliff do Nome !!!!!
        
        cursor = banco.cursor()
        nome = tela_vendas.edtNome.text()
    
        sql = ("SELECT descricao,preco,quantidade,codigo from tb_produtos WHERE descricao = '{}'".format(nome))
        cursor.execute(sql)
    
    
    
   

        for(descricao,preco,quantidade,codigo) in cursor:
            if quantidade == 0:
                cursor = banco.cursor()
                comando_SQL = ("DELETE * FROM tb_produtos WHERE quantidade = 0")
                cursor.execute(comando_SQL)
                print("Esse produto acabou")
            
            
            else:    
                cursor = banco.cursor()
                comando_SQL_Quatro = "SELECT codigo,descricao,preco,quantidade,categoria,id FROM tb_produtos"
                cursor.execute(comando_SQL_Quatro)
                dados_lidos = cursor.fetchall()
                codigo_nome = tela_vendas.edtCodigo.setText(str(codigo))
                tela_vendas.edtTotalItem.setText(str(preco))
            
        if tela_vendas.edtTotalItem.text() == "":
            tela_vendas.tvInformacao.setText("Este produto não existe ou acabou")
        else:
            tela_vendas.tvInformacao.setText("")        
            valor_inicial = float(preco)         
            tela_vendas.listTotal.addItem(str(valor_inicial))
            tela_vendas.listNome.addItem(str(descricao))
            preco_temp=float(tela_vendas.edtTotalGeral.text())
            total_temp = preco_temp + valor_inicial
            tela_vendas.edtTotalGeral.setText(str(total_temp))
            quant_temp = int(quantidade)
            total_quant = quant_temp - 1
            cursor = banco.cursor()   
            comando_SQL_Três = ("UPDATE tb_produtos SET quantidade = '{}' WHERE codigo = '{}'".format(total_quant,codigo))
            cursor.execute(comando_SQL_Três)
            banco.commit()
            print("O problema não está aqui")
            print(total_quant)
    
        
            #tela_vendas.edtCodigo.setText("")
            tela_vendas.edtTotalItem.setText("")
    #Fim do ifelse 
    else: 
        tela_vendas.tvInformacao.setText("Não é permitido nome e codigo estarem preenchidos ao selecionar")
        
        if tela_vendas.btSelecionar.isChecked():
            tela_vendas.tvInformacao.setText("")
    

def Método_Pagamento():
    if tela_vendas.cb_Metodos.currentIndex() == 0:
        tela_vendas.tv_Metodos.setText("Dinheiro")
    if tela_vendas.cb_Metodos.currentIndex() == 1:
        tela_vendas.tv_Metodos.setText("Cartão Supernac")
    if tela_vendas.cb_Metodos.currentIndex() == 2:
        tela_vendas.tv_Metodos.setText("Pix")
    if tela_vendas.cb_Metodos.currentIndex() == 3:
        tela_vendas.tv_Metodos.setText("Cartão de Crédito")
    if tela_vendas.cb_Metodos.currentIndex() == 4:
        tela_vendas.tv_Metodos.setText("Cartão de Débito")   
def Calcular_Troco():
    if tela_vendas.edtTotalRecebido.text() == "":
        tela_vendas.tvInformacao.setText("Não há valor algum inserido")
    else:
        tela_vendas.tvInformacao.setText("")    
        Valor_Inserido = float(tela_vendas.edtTotalRecebido.text())
        Valor_Total = float(tela_vendas.edtTotalGeral.text())
        Total_Geral = Valor_Inserido - Valor_Total
        tela_vendas.edtTroco.setText(str(round(Total_Geral, 2)))

    
def Apagar_Tudo():
    tela_vendas.edtNome.setText("")
    tela_vendas.edtTotalItem.setText("")
    tela_vendas.edtCodigo.setText("")
    tela_vendas.listNome.clear()
    tela_vendas.listTotal.clear()
    cursor = banco.cursor()
    comando_Apagar = ("TRUNCATE TABLE venda")
    cursor.execute(comando_Apagar)

    print("Boof Apagou")
def Gerar_Nota_Fiscal():
    cursor = banco.cursor()
    comando_Nota = ("SELECT * FROM venda")
    cursor.execute(comando_Nota)
    dados_lidos = cursor.fetchall()
    y=0
    pdf = canvas.Canvas("Nota Fiscal.pdf")
    pdf.scale(1.1,1.0)
    pdf.setFont("Times-Bold",25)
    pdf.drawString(150,800, "Supernac Supermercados")
    pdf.setFont("Times-Bold",20)
    pdf.drawString(50,750, "Nome do Usuario:")
    pdf.drawString(150,700,"Abaixo,os produtos:")
    pdf.setFont("Times-Bold",18)
    pdf.setStrokeColorRGB(0.2,0.5,0.3)
    pdf.setFillColorRGB(0,100,0)
    pdf.drawString(21,580,"Nome")
    pdf.drawString(310,570,"Preço")
    pdf.drawString(410,5700, "Código")
    pdf.drawString(400,120, "Total da Compra")
    pdf.drawString(210,50, "Método de Pagamento:")
    pdf.drawString(210,750 - y,str(tela_login.edt_usuario.text()))
    pdf.drawString(400,410 - y,str(tela_vendas.edtTotalGeral.text()))
    pdf.drawString(390,50 - y,str(tela_vendas.tv_Metodos.text()))
    for i in range(0,len(dados_lidos)):
        y = y + 50
        pdf.drawString(21,550 - y,str(dados_lidos[i][0]))
        pdf.drawString(310,550 - y,str (dados_lidos[i][1]))
        pdf.drawString(410,550 - y,str (dados_lidos[i][2]))
        
    pdf.save()
    print("Isso talvez ainda não está funcionando como deveria")
def Sair_Vendas():
    tela_vendas.close()
def facebook():
    tela_facebook.widget.load(QtCore.QUrl("https://www.facebook.com/Supernac-Supermercados-103494018984263/"))
    tela_facebook.show()
    
    

tela_login = uic.loadUi("Tela_de_Login.ui")
tela_principal = uic.loadUi("Tela_Principal.ui")
tela_pessoas = uic.loadUi("formulario_pessoas.ui")
tela_principal_pessoas = uic.loadUi("listar_pessoas.ui")
ordenar_pessoas = uic.loadUi("Ordenar_Por.ui")
tela_produtos = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
tela_editar = uic.loadUi("editar_produto.ui")
tela_vendas = uic.loadUi("tela_vendas.ui")
tela_facebook = uic.loadUi("web_facebook.ui")

tela_login.bt_entrar.clicked.connect(funcao_login)
tela_principal.bt_logout.clicked.connect(logout)
tela_principal.bt_pessoas.clicked.connect(controle)
tela_principal.bt_produtos.clicked.connect(controle_produtos)
tela_principal.bt_vendas.clicked.connect(Vendas)
tela_principal.bt_face.clicked.connect(facebook)
tela_vendas.btSelecionar.clicked.connect(Vendas_Informações)
#tela_vendas.btSelecionar.clicked.connect(buscaProdutoNome)
tela_vendas.btSelecionar.clicked.connect(buscaProdutoCodigo)
tela_vendas.btOk.clicked.connect(Método_Pagamento)
tela_vendas.btOk.clicked.connect(Gerar_Nota_Fiscal)
tela_vendas.cb_Metodos.addItems(["Dinheiro","Cartão Supernac","Pix","Cartão de Crédito","Cartão de Débito"])
tela_vendas.bt_Calcular.clicked.connect(Calcular_Troco)
tela_vendas.btApagarTudo.clicked.connect(Apagar_Tudo)
tela_vendas.btSair.clicked.connect(Sair_Vendas)
tela_pessoas.btEnviarPessoas.clicked.connect(funcao_principal)
tela_pessoas.comboBox.addItems(["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RR","RO","RJ","RN","RS","SC","SP","SE","TO"])
tela_pessoas.btListarPessoas.clicked.connect(chama_tela_principal_pessoas)
tela_pessoas.btSairPessoas.clicked.connect(Sair)
tela_principal_pessoas.btExcluirPessoas.clicked.connect(excluir_dados)
tela_principal_pessoas.btOrdenarPorPessoas.clicked.connect(chama_ordenar)
tela_principal_pessoas.btSairPessoas.clicked.connect(Sair_da_Segunda_Tela)
tela_principal_pessoas.btGerarRelatorioPessoas.clicked.connect(relatório_botao)
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
tela_produtos.btEnviar.clicked.connect(funcao_principal_produtos)
tela_produtos.btListar.clicked.connect(chama_segunda_tela)
tela_produtos.btSairProdutos.clicked.connect(Sair_Produtos)
segunda_tela.btExcluirProdutos.clicked.connect(excluir_dados_produtos)
segunda_tela.btEditarProdutos.clicked.connect(editar_dados)
segunda_tela.btSairProdutos.clicked.connect(Sair_dados_produtos)
segunda_tela.cbCategoria.addItems(["Alimentos","Eletrônicos","Informática","Nome","Preço","Tudo"])
segunda_tela.btokcategoria.clicked.connect(relatório_combo)
segunda_tela.actionEditar_2.triggered.connect(editar_dados)
segunda_tela.actionExcluir.triggered.connect(excluir_dados)
segunda_tela.actionNome.triggered.connect(relatorio_nome_menu)
segunda_tela.actionPre_o.triggered.connect(relatorio_preco_menu)
segunda_tela.actionAlimentos.triggered.connect(relatorio_alimentos_menu)
segunda_tela.actionEletr_nicos.triggered.connect(relatorio_eletronicos_menu)
segunda_tela.actionInform_tica.triggered.connect(relatorio_informatica_menu)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)


tela_login.show()
app.exec()
