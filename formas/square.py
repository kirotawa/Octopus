#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################

from OpenGL.GL import *
from formas import *

class Square(FormasGeometricas):
	"""Classe que desenha um quadrado/retangulo"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)
	
	def drawShape(self):
		"""Desenha o retangulo
			- passados os 4 pontos do retangulo este metodo o desenha atraves do algoritmo de linhas de Bresenham
			- se a variavel de controle fulled for verdadeira, desenha a forma com preenchimento
		"""
		self.Bresenham(self.pontos[0],self.pontos[1])#p0 -> p1
		self.Bresenham(self.pontos[1],self.pontos[2])#p1 -> p2
		self.Bresenham(self.pontos[3],self.pontos[2])#p3 -> p2
		self.Bresenham(self.pontos[0],self.pontos[3])#p0 -> p3
		
		if self.fulled:
			
			#glColor3f(self.colorfill['R'],self.colorfill['G'],self.colorfill['B'])
			#glBegin(GL_POLYGON)
			#glVertex3f(self.pontos[0][0]+1,self.pontos[0][1]-1,0.0)
			#glVertex3f(self.pontos[1][0]-1,self.pontos[1][1]-1,0.0)
			#glVertex3f(self.pontos[2][0]-1,self.pontos[2][1]+1,0.0)	
			#glVertex3f(self.pontos[3][0]+1,self.pontos[3][1]+1,0.0)			
			#glEnd()			
			##########Metodo para preenchimento interativo, deixa o programa muito lento######################			
			if self.pontos[0][1] > self.pontos[2][1]:
				ymax = self.pontos[0][1]
				ymin = self.pontos[2][1]
			else:
				ymax = self.pontos[2][1]
				ymin = self.pontos[0][1]
			if self.pontos[0][0] > self.pontos[2][0]:
				xmax = self.pontos[0][0]
				xmin = self.pontos[2][0]
			else:
				xmax = self.pontos[2][0]
				xmin = self.pontos[0][0]
			self.fillFlood(xmin+1, ymin+1,xmin,xmax, ymin, ymax)
			
	def fillFlood(self, x, y, xmin, xmax, ymin, ymax):
		"""Método de preenchimento de formas Flood Fill
			- Dadas os pontos de mim e max dos eixos na forma este metodo preenche tudo dentro da forma com pontos da cor estabelecida		
		"""
		
		if xmin < xmax and ymin < ymax:		
			for y in range(int(y),int(ymax)):		
				for i in range(int(x),int(xmax)):
					self.drawPointFill((i,y))
		
		
	
		 
	def Bresenham(self,p1,p2):
		"""Algoritmo de bresenham para desenhar linhas"""		
		x0 = int(p1[0])
		y0 = int(p1[1])
		x1 = int(p2[0])
		y1 = int(p2[1])
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
		
			
