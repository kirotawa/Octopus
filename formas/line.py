#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################


from OpenGL.GL import *
from math import *
from formas import *

class Line(FormasGeometricas):
	"""Classe que desenha a linha Breserham"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)
	
	
	def drawShape(self):

		tam = len(self.pontos)
		for i in range(0,tam+1,2):
			if i == tam:
				pass
			else:
				self.Bresenham(self.pontos[i:i+2][0],self.pontos[i:i+2][1])
				
		
				
	
	
	def Bresenham(self, p1,p2):
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
			stepy = 1
		if (dx < 0):
			dx = -dx
			stepx = -1
		else:
			stepx = 1

		dy = 2*dy #dy <<= 1
		dx = 2*dx #dx <<= 1#
	
		self.drawPoint((x0,y0))
		if (dx > dy):
			fraction = 2*dy - dx#dy - (dx >> 1)
			while (x0 != x1):
				if fraction >= 0:
					y0 +=stepy
					fraction -= dx
				x0 += stepx
				fraction += dy
				self.drawPoint((x0,y0))
		else:
			fraction = 2*dx - dy #dx - (dy >> 1)
			while (y0 != y1):
				if fraction >= 0:				
					x0 += stepx
					fraction -= dy
				y0 += stepy
				fraction += dx
				self.drawPoint((x0,y0))
				

		

	
