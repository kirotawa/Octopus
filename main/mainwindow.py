#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_mainwindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
	"""Classe responsável pelos widgets na tela (menu, botões, etc)"""

	def __init__(self, parent=None):
		"""Construtor"""
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.makeActions()
		self.makeActionMenu()
		self.makeMenu()
		
		
	def on_actionQuit_triggered(self):
		"""Chamado automaticamente quando o evento de sair eh chamado"""
		exit()



	def about(self):
		"""Metodo que chama a janela about"""		
		QMessageBox.about(self,self.tr("Sobre o programa"),
			self.tr("<center>O programa foi feito como trabalho da disciplina de CG em 2009 por Le&ocirc;nidas S. Barbosa(kirotawa)</center>"))

	
	def makeActionMenu(self):
		"""Cria as acoes do menu atraves das funcoes que eles executam"""
		self.newAct = QtGui.QAction(self.tr("&Novo"),self)
		self.newAct.setShortcut(self.tr("Ctrl+N"))
		self.newAct.setStatusTip(self.tr("Cria uma nova area de desenho em branco"))
		self.connect(self.newAct,SIGNAL("triggered()"),self.glwidget.newFile)
		
		self.openAct = QtGui.QAction(self.tr("&Abrir"),self)
		self.openAct.setShortcut(self.tr("Ctrl+o"))
		self.openAct.setStatusTip(self.tr("Abrir arquivo do elvis"))
		self.connect(self.openAct,SIGNAL("triggered()"),self.glwidget.openElvisfile)		

		self.saveAct = QtGui.QAction(self.tr("&Salvar"),self)
		self.saveAct.setShortcut(self.tr("Ctrl+S"))
		self.saveAct.setStatusTip(self.tr("Salva a imagem do canvas"))
		self.connect(self.saveAct,SIGNAL("triggered()"),self.glwidget.saveElvisfile)
		
		self.exportAct = QtGui.QAction(self.tr("&Exportar SVG"),self)
		self.exportAct.setShortcut(self.tr("Ctrl+E"))
		self.exportAct.setStatusTip(self.tr("Exporta para formato SVG"))
		self.connect(self.exportAct,SIGNAL("triggered()"),self.glwidget.ExportSVG)
				
		
		self.exitAct = QtGui.QAction(self.tr("&Sair"),self)
		self.exitAct.setStatusTip(self.tr("Sair do programa"))
		self.connect(self.exitAct,SIGNAL("triggered()"),self.close)
		
	
		self.aboutAct = QtGui.QAction(self.tr("&Sobre"),self)
		self.aboutAct.setStatusTip(self.tr("Sobre o programa"))
		self.connect(self.aboutAct,SIGNAL("triggered()"),self.about)
		
			
		
	def makeMenu(self):
		"""Cria os rotulos dos menus no menuBar"""
		self.fileMenu = self.menuBar().addMenu(self.tr("&Arquivo"))
		self.fileMenu.addAction(self.newAct)
		self.fileMenu.addAction(self.openAct)
		self.fileMenu.addAction(self.saveAct)
		self.fileMenu.addAction(self.exportAct)
		self.fileMenu.addSeparator() 
		self.fileMenu.addAction(self.exitAct)

		self.editMenu = self.menuBar().addMenu(self.tr("&Editar"))
		
		self.helpMenu = self.menuBar().addMenu(self.tr("&Ajuda"))
		self.helpMenu.addAction(self.aboutAct)		
		
	def makeActions(self):
		"""Cria os botoes os adiciona ao toolBar"""
		"""Botoes e ligacao com o glwidget"""
		
		"""seleção"""
		self.selectionBt = QAction(QtGui.QIcon("images/mousepointer.png"),self.tr("&Seleção"),self)	
		self.selectionBt.setStatusTip(self.tr("Seleciona os objetos"))
		self.connect(self.selectionBt, SIGNAL('triggered()'),self.glwidget.select)
		self.toolBar.addAction(self.selectionBt)	

		"""lupas"""
		self.zoomoutBt = QAction(QtGui.QIcon("images/zoomout.png"),self.tr("&Zoom out"),self)
		self.zoomoutBt.setStatusTip(self.tr("Aumenta a imagem"))
		self.connect(self.zoomoutBt, SIGNAL('triggered()'),self.glwidget.zoomout)
		self.toolBar.addAction(self.zoomoutBt)
		"""zoom in"""
		self.zoominBt = QAction(QtGui.QIcon("images/zoomin.png"),self.tr("&Zoom in"),self)
		self.zoominBt.setStatusTip(self.tr("Diminui a imagem"))
		self.zoominBt.connect(self.zoominBt, SIGNAL('triggered()'),self.glwidget.zoomin)
		self.toolBar.addAction(self.zoominBt)
		"""vertice"""
		self.verticeBt = QAction(QtGui.QIcon("images/vertice.png"),self.tr("&Vertice"),self)
		self.verticeBt.setStatusTip(self.tr("Desenha um vertice"))
		self.connect(self.verticeBt,SIGNAL('triggered()'),self.glwidget.vertice)
		self.toolBar.addAction(self.verticeBt)


		"""polilinha"""
		self.plineBt = QAction(QtGui.QIcon("images/plinha.png"),self.tr("&poly linha"),self)
		self.plineBt.setStatusTip(self.tr("Cria uma poly linha"))
		self.connect(self.plineBt,SIGNAL('triggered()'),self.glwidget.lineControl)
		self.toolBar.addAction(self.plineBt)
		"""quadrado/retangulos"""
		self.squareBt = QAction(QtGui.QIcon("images/square.png"),self.tr("&poligono"),self)
		self.squareBt.setStatusTip(self.tr("Cria um poligono"))
		self.connect(self.squareBt,SIGNAL('triggered()'),self.glwidget.squareControl)
		self.toolBar.addAction(self.squareBt)
		"""circulo/elipse"""
		self.circuloBt = QAction(QtGui.QIcon("images/circulo.png"),self.tr("&circulo e elipse"),self)
		self.circuloBt.setStatusTip(self.tr("cria um circulo ou uma elipse"))
		self.connect(self.circuloBt,SIGNAL('triggered()'),self.glwidget.circuloControl)
		self.toolBar.addAction(self.circuloBt)
		

		"""Edição"""
		self.toolBar.addSeparator()
		self.toolBar.addWidget(QLabel('Editar',self.toolBar))		
		"""copiar"""
		self.copyBt = QAction(QtGui.QIcon("images/copy.png"),self.tr("&copiar formas"),self)
		self.copyBt.setStatusTip(self.tr("Copia forma selecionada"))
		self.connect(self.copyBt,SIGNAL('triggered()'),self.glwidget.copyControl)
		self.toolBar.addAction(self.copyBt)
		"""cor de preenchimento"""
		self.colorfillBt = QAction(QtGui.QIcon("images/fill.png"),self.tr("&cor de preenchimento"),self)
		self.colorfillBt.setStatusTip(self.tr("Defina a cor de preenchimento dos objetos"))
		self.connect(self.colorfillBt, SIGNAL('triggered()'),self.glwidget.colorfillControl)
		self.toolBar.addAction(self.colorfillBt)		
	
		"""cor da borda"""
		self.colorBt = QAction(QtGui.QIcon("images/color.png"),self.tr("&cor da borda dos objetos"),self)
		self.colorBt.setStatusTip(self.tr("Define a cor da borda dos objetos"))
		self.connect(self.colorBt, SIGNAL('triggered()'),self.glwidget.colorControl)
		self.toolBar.addAction(self.colorBt)		
	
		"""Pontos de Controle"""
		self.pontoscontroleBt = QAction(QtGui.QIcon("images/pontosdecontrole.png"),self.tr("&pontos de controle"),self)
		self.pontoscontroleBt.setStatusTip(self.tr("Adiciona e remove os pontos de controle"))
		self.connect(self.pontoscontroleBt,SIGNAL('triggered()'),self.glwidget.pontosControle)
		self.toolBar.addAction(self.pontoscontroleBt)
		
		"""rotacionar"""
		self.rotationBt = QAction(QtGui.QIcon("images/rotation.png"),self.tr("&rotacionar"),self)
		self.rotationBt.setStatusTip(self.tr("Rotacionar objeto"))
		self.connect(self.rotationBt,SIGNAL('triggered()'),self.glwidget.rotationControl)
		self.toolBar.addAction(self.rotationBt)
		
 		"""grade"""
		self.gradesBt = QAction(QtGui.QIcon("images/grade.png"),self.tr("&grade"),self)
		self.gradesBt.setStatusTip(self.tr("Adiciona uma grade sobre o canvas"))
		self.connect(self.gradesBt,SIGNAL('triggered()'),self.glwidget.grade)
		self.toolBar.addAction(self.gradesBt)
		

		

