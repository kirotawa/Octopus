#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                            #
#########################################################################

from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from formas.line import *
from formas.square import *
from formas.circle import *
from formas.elipse import *
from PyQt4 import QtGui, QtCore

class GlWidget(QGLWidget):
	"""Painel OpenGL"""

	def __init__(self, parent=None):
		"""Metodo construtor para inicializar o que for preciso"""		
		super(GlWidget, self).__init__(parent)
		self.initializeVars()
		self.setFocus()	
		self.setMouseTracking(1)
		self.shapes = list()		
		self.poliline = None
		self.poli = False
		self.shape_colide = None
		self.firstPointMove = None

	def initializeVars(self):
		"""Metodo para inicilar alguns valores de variaveis de controle interno"""
		self.firstPoint  = None
		self.secondPoint = None
		self.line = False
		self.square = False
		self.circle = False	
		self.control = False
		self.zoomin_ = False
		self.zoomout_ = False
		self.pcontrole = False
		self.grid = False
		self.vert = False
		self.selectMode = False	
		self.rotation = False
		self.copy = False			

	def initializeGL(self):
		"""Metodo do glwidget para inicializar o opengl
			- glClearColor(1.0,1.0,1.0,1.0): Limpa o buffer para branco.	
		"""
		glDisable(GL_DEPTH_TEST)		
		glClearColor(1.0,1.0,1.0,1.0)
		

	def paintGL(self):
		"""Metodo responsavel por pintar objetos no painel opengl
			- Controla o zoom, o grid, o desenho o desenho das formas.
		if self.zoomin_ == True:
			self.zoomin_ = False
			for i in self.shapes:
				i.Scale(0.75,'in')
		if self.zoomout_ == True:
			self.zoomout_ = False	
			for i in self.shapes:
				i.Scale(0.75,'out')

		if self.grid:
			self.drawGrid(self.gridsize)			
		
		
		for i in self.shapes:
			i.drawShape()
			if self.pcontrole or i.selected:
				i.drawControlPoints()
			
		glPopMatrix()
		glFlush()		
		"""
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(0.0,0.0,0.0)
		glPushMatrix()

		if self.zoomin_ == True:
			self.zoomin_ = False
			for i in self.shapes:
				i.Scale(0.75,'in')
		if self.zoomout_ == True:
			self.zoomout_ = False	
			for i in self.shapes:
				i.Scale(0.75,'out')

		if self.grid:
			self.drawGrid(self.gridsize)			
		
		
		for i in self.shapes:
			i.drawShape()
			if self.pcontrole or i.selected:
				i.drawControlPoints()
		
		glPopMatrix()
		glFlush()
		

	def resizeGL(self, width, height):
		"""Metodo que resetar as dimensoes da tela do opengl"""	
		self.widthX = width
		self.heightY = height
		
		glViewport(0,0,width,height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0.0,self.widthX,0.0,self.heightY)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		

	def select(self):
		"""Metodo de controle da seleção"""
		self.initializeVars()		
		self.selectMode = True
		self.setCursor(QtCore.Qt.PointingHandCursor) 	
			
		
	def zoomout(self):
		"""Metodo que efetua o zoom out"""
		self.zoomout_ = True
		self.updateGL()	
		
	def zoomin(self):
		"""Metodo que efetua o zoom in """
		self.zoomin_ = True
		self.updateGL()

	def vertice(self):
		"""Metodo de controle de inserção de vertices"""
		self.vert = True
		self.line = False
		self.square = False
		self.circle = False
		self.selectMode = False		
		self.setCursor(QtCore.Qt.CrossCursor)	

	def lineControl(self):
		"""Método de controle de linhas"""
		self.initializeVars()
		self.line = True	
		self.setCursor(QtCore.Qt.CrossCursor)


	def squareControl(self):
		"""Metodo de controle do retangulo/quadrado"""
		self.square = True
		self.line = False
		self.circle = False
		self.vert = False
		self.selectMode = False	
		self.setCursor(QtCore.Qt.CrossCursor)

	def circuloControl(self):
		"""Metodo de controle do circulo e da elipse"""
		self.circle = True
		self.line = False
		self.square = False
		self.vert = False
		self.selectMode = False	
		self.setCursor(QtCore.Qt.CrossCursor)

	def colorControl(self):
		"""Controle de cores de borda"""
		self.color = QtGui.QColorDialog.getColor()
		self.color = self.color.toRgb()
		if self.shape_colide != None:
					
			self.shape_colide.color['R'] = self.color.redF()
			self.shape_colide.color['G'] = self.color.greenF()
			self.shape_colide.color['B'] = self.color.blueF()
			self.updateGL()

	def copyControl(self):
		"""Metodo que controla a copia de objetos"""
		self.copy = True
		self.square = False
		self.line = False
		self.circle = False
		self.vert = False
		self.selectMode = False
		
			
	def colorfillControl(self):
		"""Metodo que define a cor e manda preencher os objetos"""
		self.colorfill = QtGui.QColorDialog.getColor()
		self.colorfill = self.colorfill.toRgb()
		if self.shape_colide != None:
			self.shape_colide.fulled = True	
			self.shape_colide.colorfill['R'] = self.colorfill.redF()
			self.shape_colide.colorfill['G'] = self.colorfill.greenF()
			self.shape_colide.colorfill['B'] = self.colorfill.blueF()
			self.updateGL()
		
	def pontosControle(self):
		"""Metodo que controla a inserção e remoção de pontos de controle"""
		if self.pcontrole == False:
			self.pcontrole = True
		else:
			self.pcontrole = False
		self.updateGL()
	
	def rotationControl(self):
		"""Metodo que controla a rotação dos objetos"""		
		self.square = False
		self.line = False
		self.circle = False
		self.vert = False
		self.selectMode = False	
		self.rotation = True

	def grade(self):
		"""Chamada para definição da grade
			- É dado ao usuário o direito de escolher as dimensões da grade.
			- Se uma grade já está desenhanda ele retira a grade, senão ele a desenha com as dimenões passadas
		"""
		if self.grid == False:
			result = QtGui.QInputDialog.getInteger(None,"Grid", "Entre com a dimensao do grid:",0,50,300,1)
			if result[1]:
				self.grid = True
				self.gridsize = result[0]
				
		else:
			self.grid = False

		self.updateGL()

	def drawGrid(self,size):
		"""Desenha um grid dadas dimensões passadas pelo usuário"""
		
			
		for y in range(size,self.widthX,size):
			glColor3f(.5,0.0,0.0)			
			glBegin(GL_LINES)
			glVertex2f(0.0,y)
			glVertex2f(self.widthX,y)
			glEnd()

		for x	in range(size,self.widthX,size):
			glColor3f(.5,0.0,0.0)	
			glBegin(GL_LINES)
			glVertex2f(x,0.0)
			glVertex2f(x,self.widthX)
			glEnd()
		
	def newFile(self):
		"""Metodo chamado quando um novo arquivo é acionado
			- Pergunta se é desejavel salvar o arquivo atual
			- Limpa a lista de formas e inicializa as variaveis de controle
		"""
		dlg = QtGui.QMessageBox(None)
		dlg.setWindowTitle("Deseja salvar o arquivo atual?")
		dlg.setIcon(QtGui.QMessageBox.Question)
		dlg.setText("Deseja salvar o arquivo atual?")
		dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
		resp = dlg.exec_()		
		if resp == 16384:
			self.saveElvisfile()
		else:
			self.shapes = list()
			self.initializeVars()		
			self.updateGL()

		
		
			
	def saveElvisfile(self):
		"""Metodo mágico que salva as imagens em .elv
			- Todos os objetos/formas são exportados para um arquivo
		"""
		filepath = QtGui.QFileDialog.getSaveFileName(None,'Salvar imagem','/home','Imagem (*.elv)')
		filename = file(filepath,'w')
		
		
		import cPickle as p
		
		p.dump(self.shapes,filename)
		filename.close()
		
	def openElvisfile(self):
		"""Método mágico que abre arquivo .elv
			- Todos os objetos salvos no arquivo .elv são recarregados para lista de formas
		"""
		filepath = QtGui.QFileDialog.getOpenFileName(None, "Escolha um arquivo para abrir", "/home","Imagem (*.elv)");
		filename = file(filepath)
		
		import cPickle as p
		
		shapes = p.load(filename)
		if shapes != None:
			self.shapes = shapes
		self.updateGL()

	def ExportSVG(self):
		"""Metodo acionado para exportar imagem .svg
			-  Salva um arquivo XML com as caracteristicas de um arquivo .SVG dado um nome e uma localização pelo usuário
		"""		

		filepath = QtGui.QFileDialog.getSaveFileName(None,'Exportar para SVG','/home','Imagem (*.SVG)')
		filename = file(filepath,'w')
		
		xml = """<?xml version="1.0" standalone="no"?>
		    	<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
			"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
			<svg width="100%" height="100%" version="1.1"
			 xmlns="http://www.w3.org/2000/svg">"""
		
		for shape in self.shapes:
			if shape.__class__.__name__ == 'Square':
				xml += """<rect x="%f" y="%f" width="%f" height="%f" """ % (shape.pontos[0][0],shape.pontos[0][1], shape.pontos[1][0] - shape.pontos[0][0], shape.pontos[0][1] - shape.pontos[1][1])
				cor = self.RGBtoHex((shape.color['R'],shape.color['G'],shape.color['B']))
				corfill = self.RGBtoHex((shape.colorfill['R'],shape.colorfill['G'],shape.colorfill['B']))
					
				if shape.fulled == False:

					xml += """ style="fill:none;stroke:%s;stroke-width:1" />\n""" %(cor)
				else:
					xml += """ style="fill:%s;stroke:%s;stroke-width:1" /> \n""" % (corfill,cor)
			if shape.__class__.__name__ == 'Circle':
				xml += """<circle cx="%f" cy="%f" r="%f """ % (shape.pontos[0][0],shape.pontos[0][1],shape.radius)
				cor = self.RGBtoHex((shape.color['R'],shape.color['G'],shape.color['B']))
				corfill = self.RGBtoHex((shape.colorfill['R'],shape.colorfill['G'],shape.colorfill['B']))	
				if shape.fulled == False:
					xml += """ style="fill:none;stroke:%s;stroke-width:1" />\n""" %(cor)
				else:
					xml += """ style="fill:%s;stroke:%s;stroke-width:1" /> \n"""  % (corfill,cor)
			if shape.__class__.__name__ == 'Elipse':
				xml += """<elipse cx="%f" cy="%f" rx="%f" ry="%f" """ % (shape.pontos[0][0],shape.pontos[0][1], shape.pontos[1][0] - shape.pontos[0][0], shape.pontos[1][1] - shape.pontos[0][1])
				cor = self.RGBtoHex((shape.color['R'],shape.color['G'],shape.color['B']))
				corfill = self.RGBtoHex((shape.colorfill['R'],shape.colorfill['G'],shape.colorfill['B']))	
				if shape.fulled == False:
					xml += """ style="fill:none;stroke:%s;stroke-width:1" />\n""" % (cor)
				else:
					xml += """ style="fill:%s;stroke:%s;stroke-width:1" /> \n""" % (corfill,cor)
							
			if shape.__class__.__name__ == 'Line':
				cor = self.RGBtoHex((shape.color['R'],shape.color['G'],shape.color['B']))
				xml += """<line x="%f" y="%f" style="fill:none;stroke:%s;stroke-width:1" />""" % (cor)

		xml += "</svg>"
		filename.write(xml)
		filename.close()	
	
	def RGBtoHex(self,color):
		"""Metodo que converte as cores de RGB float para RGB em hexadecimal"""		

		colorHex = "#"		
		for c in color:
			if str(hex(int(round(float(c*255)))))[2:] == '0':
				colorHex += '00'
			else:
				colorHex += str(hex(int(round(float(c*255)))))[2:]	
		return colorHex	
			
	def mousePressEvent(self, event):
		"""Método de controle de eventos de de pressionamento do mouse
			- Neste metodo são tratado os cliques que irão dar origem a objetos, controlar a seleção, a copia, a rotação.
			- Nesse metodo é capturado o primeiro ponto de cada forma.
		"""
		if self.selectMode and len(self.shapes) > 0:
			for shape in self.shapes:
				if shape.Colide((event.x(),self.heightY - event.y())):
					
					if self.shape_colide != None and self.shape_colide != shape:
						self.shape_colide.selected = False
					
					shape.selected = True
					self.shape_colide = shape
					
					
					self.firstPointMove = event.x(), self.heightY - event.y()
					
					
			self.updateGL()
		

		if event.button() == 2:
			self.shapes.remove(self.shapes[-1])		
			self.updateGL()

		if self.vert and event.button() == 1:
			vertice = Vertice(len(self.shapes)+1)
			vertice.addPoint((event.x(), self.heightY - event.y()))
			self.shapes.append(vertice)
			self.updateGL()

		if self.line and event.button() == 1:
			if self.firstPoint == None:
				self.firstPoint =  event.x(),self.heightY - event.y()
						
			if self.firstPoint != None and self.poliline != None:
				self.poli = True
							
		if self.square and event.button() == 1:
			if self.firstPoint == None:
				self.firstPoint =  event.x(), self.heightY - event.y()
		if self.circle and event.button() == 1:
			if self.firstPoint == None:
				self.firstPoint = event.x() , self.heightY - event.y()
		
		if self.rotation:
			for shape in self.shapes:
				if shape.Colide((event.x(),self.heightY - event.y())):
					if shape.__class__.__name__ != 'Square':
						shape.Rotate(90,(event.x(),self.heightY - event.y()))
					self.updateGL()
		if self.copy:
			
			if self.shape_colide != None:
				
				if self.shape_colide.__class__.__name__ == 'Square':
					cp = Square(len(self.shapes)+1)
					cp.pontos = list(self.shape_colide.pontos)
					self.shapes.append(cp)
					cp.selected = False	
					self.copy = False
				if self.shape_colide.__class__.__name__=='Circle':
					cp = Circle(len(self.shapes)+1)
					cp.pontos = list(self.shape_colide.pontos)
					self.shapes.append(cp)
					cp.selected = False	
					self.copy = False	
				if self.shape_colide.__class__.__name__=='Elipse':
					cp = Elipse(len(self.shapes)+1)
					cp.pontos = list(self.shape_colide.pontos)
					self.shapes.append(cp)
					cp.selected = False	
					self.copy = False
				if self.shape_colide.__class__.__name__=='Line':
					cp = Line(len(self.shapes)+1)
					cp.pontos = list(self.shape_colide.pontos)
					self.shapes.append(cp)
					cp.selected = False	
					self.copy = False			
				self.updateGL()
	

	def mouseReleaseEvent(self, event):
		"""Metodo analogo ao press, controla o release do mouse e desenha as formas de fato"""
		if self.selectMode and len(self.shapes) > 0 and self.copy == False:
								
			if self.firstPointMove != None:
				if self.secondPoint != None:
					self.shape_colide.move(self.firstPointMove,self.secondPoint)
					#self.firstPointMove  = None
					self.secondPoint = None
			self.updateGL()
		if self.line:
			
			if event.button() == 2:
				self.shapes.remove(self.shapes[-1])		
				self.updateGL()
			if event.button() == 4:
				if self.firstPoint != None:
					if self.secondPoint != None:
				
						self.poliline.addPoint(self.firstPoint)
						self.poliline.addPoint(self.secondPoint)
						self.updateGL()
						self.firstPoint = None
						self.secondPoint = None
						self.poliline = None
						self.poli = False

					elif self.secondPoint != None and self.poliline != None:
						
						self.poliline.addPoint(self.firstPoint)
						self.poliline.addPoint(self.secondPoint)
						self.updateGL()
						self.firstPoint = None
						self.secondPoint = None	
						self.poliline = None
						self.poli = False					
			
			elif event.button() == 1:
				if self.firstPoint != None: 
					if self.secondPoint != None and self.poli:
						self.poliline.addPoint(self.firstPoint)
						self.poliline.addPoint(self.secondPoint)
						self.firstPoint = self.secondPoint[0],self.secondPoint[1]
						self.secondPoint = None
						self.updateGL()
						

					elif self.secondPoint != None:	
						_lineshapeMove = Line(len(self.shapes)+1)
						_lineshapeMove.addPoint(self.firstPoint)
						_lineshapeMove.addPoint(self.secondPoint)					
						
						self.shapes.append(_lineshapeMove)
						self.updateGL()
						self.firstPoint = self.secondPoint[0],self.secondPoint[1]
						self.poliline = _lineshapeMove
						self.secondPoint = None

		if self.square and event.button() == 4:
			 if self.firstPoint != None:
				if self.secondPoint != None:
					_squarerelease = Square(len(self.shapes)+1)
					_squarerelease.addPoint(self.firstPoint)
					_squarerelease.addPoint((self.secondPoint[0],self.firstPoint[1]))
					_squarerelease.addPoint(self.secondPoint)
					_squarerelease.addPoint((self.firstPoint[0],self.secondPoint[1]))
					
					self.shapes.append(_squarerelease)
					self.updateGL()
					self.firstPoint = None
					self.secondPoint = None
		if self.circle and event.button() == 4:
			if self.firstPoint != None:
				if self.secondPoint != None:
					if self.control:
						shape = Elipse(len(self.shapes)+1)
					else:
						shape = Circle(len(self.shapes)+1)
						
					shape.addPoint(self.firstPoint)
					shape.addPoint(self.secondPoint)
					self.shapes.append(shape)
					
					self.updateGL()
					self.firstPoint = None
					self.secondPoint = None

	def mouseMoveEvent(self , event):
		"""Metodo responsável principalmente por capturar o segundo ponto de cada forma"""
		
		if self.selectMode and len(self.shapes) > 0:
				if self.firstPointMove != None:
					self.secondPoint = event.x(),self.heightY - event.y()
					
		
		if self.line:
			if self.firstPoint != None:
				self.secondPoint = event.x(), self.heightY - event.y()
				_lineshapeMove = Line(len(self.shapes)+1)
				_lineshapeMove.addPoint(self.firstPoint)
				_lineshapeMove.addPoint(self.secondPoint)
				
				self.shapes.append(_lineshapeMove)
				self.updateGL()
				self.shapes.remove(_lineshapeMove)

		if self.square:
			if self.firstPoint != None:
				self.secondPoint =  event.x() ,self.heightY - event.y()
				_squareMove = Square(len(self.shapes)+1)
				_squareMove.addPoint(self.firstPoint)
				_squareMove.addPoint((self.secondPoint[0],self.firstPoint[1]))
				_squareMove.addPoint(self.secondPoint)
				_squareMove.addPoint((self.firstPoint[0],self.secondPoint[1]))
				self.shapes.append(_squareMove)
				self.updateGL()
				self.shapes.remove(_squareMove)

		if self.circle:
			if self.firstPoint != None:
				self.secondPoint =  event.x() ,self.heightY - event.y()
				if self.control:
					shape = Elipse(len(self.shapes)+1)
				else:
					shape = Circle(len(self.shapes)+1)
					
				
				shape.addPoint(self.firstPoint)
				shape.addPoint(self.secondPoint)
				self.shapes.append(shape)
				self.updateGL()
				self.shapes.remove(shape)

	def keyPressEvent(self,event):
		"""Controla eventos de pressionamento de teclas
			- Controla o pan da tela realizando translações nas formas de acordo com a  sua orientação dada pelo teclado de setas.
			- Controla se uma elipse deve ser desenhanda ao inves de um circulo
			- Apaga uma forma se esta estiver selecionada e a telca delete for acionada
		"""		
		
		if event.key() == QtCore.Qt.Key_Escape:
			self.shapes.remove(self.shapes[-1])
		if self.circle:
			if event.key() == QtCore.Qt.Key_Control and event.isAccepted():
				self.control = True
				
		if event.key() == QtCore.Qt.Key_Delete and self.shape_colide != None:
			self.shapes.remove(self.shapes[self.shapes.index(self.shape_colide)])
			
		if event.key() == QtCore.Qt.Key_Up:
			for i in self.shapes:
				i.Translate(1.75,'up')
		if event.key() == QtCore.Qt.Key_Down:
			for i in self.shapes:
				i.Translate(1.75,'down')
		if event.key() == QtCore.Qt.Key_Left:
			for i in self.shapes:
				i.Translate(1.75,'left')
		if event.key() == QtCore.Qt.Key_Right:	
			for i in self.shapes:
				i.Translate(1.75,'right')


		self.updateGL()


	def keyReleaseEvent(self,event):
		"""Controla os eventos da liberação das teclas do teclado"""		
		if event.key() == QtCore.Qt.Key_Control:
			self.control = False

	
			
