# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Sep 18 15:41:29 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui , Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
       # self.toolBar = QtGui.QToolBar(MainWindow)
	#self.toolBar.setObjectName("toolBar")
	#self.toolBar.setOrientation(QtCore.Qt.Vertical)
	#MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea,self.toolBar)
	self.glwidget = GlWidget(self.centralwidget)
        self.glwidget.setObjectName("glwidget")
        self.verticalLayout.addWidget(self.glwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtGui.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        #self.menubar.setObjectName("menubar")
	#MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
      	self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
	MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Elvis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

from glwidget import GlWidget
