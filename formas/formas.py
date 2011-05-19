#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################

from OpenGL.GL import *
from math import sqrt, cos, sin



class FormasGeometricas(object):
	"""Classe base para todas as formas (linha, quadrado, circulo, elipse e curva)"""
	def __init__(self,id):
		"""Construtor da classe, que inicializa as cores de borda e de preenchimento para o default"""
		self._id = id
		self.trace = False
		self.fulled = False
		self.selected = False
		self.pontos = list()
		self.color = {'R':0.0,'B':0.0,'G':0.0}
		self.colorfill = {'R':1.0,'B':1.0,'G':1.0}
		
		
	def drawShape(self):
		"""Método abstrato para as classes filhas"""		
		pass
	
	def addPoint(self,ponto):
		"""Adiciona pontos a forma"""
		self.pontos.append(list(ponto))
	
	def drawPoint(self,ponto):
		"""Desenha os pontos de acordo com sua posição e cor"""
		glColor3f(self.color['R'],self.color['G'],self.color['B'])
		glBegin(GL_POINTS)
		glVertex3f(float(ponto[0]),float(ponto[1]),0.0)
		glEnd()
	
	def drawPointFill(self,ponto):
		"""Metodo usado para desenhar pontos com cor no preenchimento de formas"""
		glColor3f(self.colorfill['R'],self.colorfill['G'],self.colorfill['B'])
		glBegin(GL_POINTS)
		glVertex3f(float(ponto[0]),float(ponto[1]),0.0)
		glEnd()     
                                                                	
	def drawControlPoints(self):
		"""Desenha os pontos de controle da forma"""
		for i in self.pontos:
			self.drawVertice(i[0],i[1])

	
	def drawVertice(self,x,y):
		"""Desenha os vertices dos pontos de controle"""
		vertice = SquareControl(0)
		vertice.addPoint((x - 5, y + 5))
		vertice.addPoint((x + 5, y + 5))
		vertice.addPoint((x + 5, y - 5))
		vertice.addPoint((x - 5, y - 5))

		if self.selected:
			vertice.color['R'] = 0.0
			vertice.color['G'] = 1.0
			vertice.color['B'] = 0.0
		else:
			vertice.color['R'] = 1.0
			vertice.color['G'] = 0.0
			vertice.color['B'] = 0.0
		vertice.drawShape()



	def Colide(self,mouse):
		"""Método usado para detectar colisões, ou seja, verificar se uma forma foi selecionada"""
		for pontos in self.pontos:
			if mouse[0] in range(int(pontos[0]-5),int(pontos[0]+6)) and mouse[1] in range(int(pontos[1]-5),int(pontos[1]+6)):
				return True
		return False
				


	def Scale(self,zoom,typ ):
		"""Método usado para escalar a forma"""		
		for index, subl in enumerate(self.pontos):
			if typ == "in":
				self.pontos[index] = [ el * zoom for el in subl]
			else:
				self.pontos[index] = [ el / zoom  for el in subl]				
		
	def Translate(self,desloc,direc):
		"""Método usado para transladar a forma"""
		for index, subl in enumerate(self.pontos):
			if direc == 'up':
				subl[1] += desloc
				self.pontos[index] = [subl[0],subl[1]]
			if direc == 'down':
				subl[1] -= desloc
				self.pontos[index] = [subl[0],subl[1]]
			if direc == 'left':
				subl[0] -= desloc
				self.pontos[index] = [subl[0],subl[1]]
			if direc == 'right':
				subl[0] += desloc
				self.pontos[index] = [subl[0],subl[1]]

	def Rotate(self,degree,point):
		"""Método para aplicar rotação as formas"""
		for index, subl in enumerate(self.pontos):
			x = (subl[0] - point[0])*cos(degree) + (subl[1] - point[1])*sin(degree)
			y = -(subl[0] - point[0])*sin(degree) + (subl[1] - point[1])*cos(degree)
			
			subl[0] = x + point[0]
			subl[1] = y + point[1]
			self.pontos[index] = [subl[0], subl[1]]
					
	def move(self,p1, p2):
		"""Método usado para mover a forma de lugar de forma interativa"""
		dx = p2[0] - p1[0]
		dy = p2[1] - p1[1]	
		
		
		for index, subl in enumerate(self.pontos):
			subl[0] += dx
			subl[1] += dy
			self.pontos[index] = [subl[0],subl[1]]
			

	
	
		
			

class Point(object):
	"""Classe que define pontos ou vertices"""

	def __init__(self,ponto):
		self.ponto = ponto[0], ponto[1]
		

class Vertice(FormasGeometricas):
	"""Classe que define o vertice"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)
	
	
	def drawShape(self):
		self.drawPoint(self.pontos[0])
	


class SquareControl(FormasGeometricas):
	"""Classe que desenha um quadrado/retangulo"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)
	
	def drawShape(self):
		self.Bresenham(self.pontos[0],self.pontos[1])
		self.Bresenham(self.pontos[1],self.pontos[2])
		self.Bresenham(self.pontos[3],self.pontos[2])
		self.Bresenham(self.pontos[0],self.pontos[3])

	def Bresenham(self,p1,p2):
		"""Método de Bresenham para desenhar as quatro linhas do quadrado dos pontos de controle"""
		x0 = p1[0]
		y0 = p1[1]
		x1 = p2[0]
		y1 = p2[1]
		dy = y1 - y0
		dx = x1 - x0
	
		if (dy < 0):
			dy = -dy
			stepy = -1
		else:
			stepy = -1
		if (dx < 0):
			dx = -dx
			stepx = -1
		else:
			stepx = 1
		self.drawPoint((x0,y0))
		if (dx > dy):
			fraction = 2*dy - dx
			while (x0 != x1):
				if fraction >= 0:
					y0 += stepy
					fraction -= dx
				x0 += stepx
				fraction += dy
				self.drawPoint((x0,y0))
		else:
			fraction = 2*dx - dy
			while (y0 != y1):
				if fraction >= 0:
					x0 += stepx
					fraction -= dy
				y0 += stepy
				fraction += dx
				self.drawPoint((x0,y0))


