#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                            #
#########################################################################

from OpenGL.GL import *
from formas import *
from math import fabs, sqrt

class Elipse(FormasGeometricas):
	"""Classe que desenha e controla a elipse"""
	def __init__(self,id):
		FormasGeometricas.__init__(self,id)
	
	def drawShape(self):
		a = fabs(self.pontos[1][0] - self.pontos[0][0])
		b = fabs(self.pontos[1][1] - self.pontos[0][1])
		cx = self.pontos[0][0]
		cy = self.pontos[0][1]
		self.drawElipse(a,b, cx, cy)
		
		if self.fulled:
			self.floodFill(a, b, cx, cy);

	def floodFill(self,a,b,cx,cy):
		"""Metodo de preenchimento interativo"""		
		c = sqrt(a*a - b*b);
		f1 = cx-c, cy
		f2 = cx+c, cy
		
		for i in range(int(cx-a+1),int(cx+a)):
			for j in range(int(cy-b),int(cy+b)):
				if (sqrt(pow(i-f1[0],2) + pow(j-f1[1],2) ) + sqrt(pow(i-f2[0],2) + pow(j-f2[1],2) ) ) < 2* a:
					self.drawPointFill((i,j)) 
	
	

	def drawElipse(self,a,b, cx, cy):
		"""Método interativo para desenhar ume elipse ponto a ponto"""
		x = 0
		y = b
		
		d1 = b * b - a*a*b+a*a /4.0

		self.drawPointElipse(x,y,cx,cy)
	
		while (a*a*(y-.5) > b * b * (x + 1)):
			if (d1 < 0):
				d1 = d1 + b * b *(2*x +3)
			   	x += 1
			else:
				d1 = d1 +  b*b*(2*x + 3)+a*a*(-2*y+2)
				x += 1
				y -= 1
			self.drawPointElipse(x,y,cx,cy)
			
		d2 = b * b * (x+.5)*(x+.5)+a*a*(y-1)*(y-1)-a*a*b*b
		while (y > 0):
			if (d2 < 0):
				d2 = d2 + b*b *(2*x+2) + a*a*(-2*y+3)
				x += 1
				y -= 1
				
			else:
				d2 = d2 + a*a * (-2* y+3)
				y -= 1
			self.drawPointElipse(x,y, cx, cy)

	def drawPointElipse(self,x,y, cx, cy):
		self.drawPoint((cx + x, cy + y))
		self.drawPoint((cx - x, cy + y))
		self.drawPoint((cx + x, cy - y))
		self.drawPoint((cx - x, cy - y))

	
