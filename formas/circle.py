#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################


from OpenGL.GL import *
from math import sqrt
from formas import *

class Circle(FormasGeometricas):
	"""Classe que desenha um circulo"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)

	def addRadius(self):
		self.radius = int(sqrt((self.pontos[1][0] - self.pontos[0][0])**2 + (self.pontos[1][1] - self.pontos[0][1])**2))
		
		
	def drawShape(self):
		self.addRadius()		
		self.BresenhamCircle(self.pontos[0][0],self.pontos[0][1],self.radius)

		if self.fulled:
			self.floodFill(self.radius, self.pontos[0][0],self.pontos[0][1])

	def floodFill(self,radius, cx, cy):
		for i in range(int(cx-radius),int(cx+radius-1)):
			for j in range(int(cy-radius),int(cy+radius-1)):
				if sqrt(pow(i- cx,2) + pow(j -cy,2)) < radius:
					self.drawPointFill((i,j))		
	
			
		
	def BresenhamCircle(self,cx,cy,radius):
		"""Método que usa o algoritmo de Bresenham para desenhar um circulo ponto a ponto"""
		error = -radius
		x = radius
		y = 0
		while (x >= y):
			self.plot8points(cx,cy,x,y)
			error += y
			y += 1
			error += y
			if error >= 0:
				x -= 1
				error -= x
				error -= x

	def plot8points(self,cx,cy,x,y):
		"""Função auxiliar para desenhar o circulo de Bresenham"""
		self.plot4points(cx,cy,x,y)
		if x != y:
			self.plot4points(cx,cy,y,x)
	
	def plot4points(self,cx,cy,x,y):
		"""Função auxiliar a função plot8points para desenhar o algoritmo de Bresenham"""		
		self.drawPoint((cx+x,cy+y))
		if x != 0:
			self.drawPoint((cx - x, cy + y))
		if y != 0:
			self.drawPoint((cx + x, cy - y))
		if x != 0 and y !=0:
			self.drawPoint((cx - x, cy -y))
			
