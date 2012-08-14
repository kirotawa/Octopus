#!/usr/bin/env python
# -*- coding: utf-8-*-

#########################################################################
#     Desenvolvido por: Leônidas S. Barbosa - 2009                      #
#     E-mail: kirotawa(arroba)gmail.com                                 #                                                        
#     		                                                        #
#########################################################################

__version__ = '0.0.1'
__autor__ = 'Leônidas S. Barbosa (kirotawa)'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main import mainwindow
import sys

app = QApplication(sys.argv)
form = mainwindow.MainWindow()
form.show()
app.exec_()
