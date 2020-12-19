from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QFileDialog,QShortcut
from PyQt5.QtCore import QTimer, QTime, Qt, QDate, QDateTime
import sys,os
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QKeySequence

from scanner import Scanner


def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		# this will hide the title bar
		#self.setWindowFlag(Qt.FramelessWindowHint)
		uic.loadUi(resource_path("MainScreen.ui"), self)
		self.setGeometry(0,0,1280,720)
		self.setWindowTitle("Compiler Project")
		self.init_ui()
		self.scanner = Scanner()

	def init_ui(self):
		print("Initialization")
		self.Output_Area.setReadOnly(True)
		self.console.setReadOnly(True)


		self.Code_Area.textChanged.connect(self.Color_Code)
		self.Open_File.triggered.connect(self.openFileNameDialog)
		self.Save_File.triggered.connect(self.saveFileDialog)
		self.Open_shortcut = QShortcut(QKeySequence("Ctrl+O"),self)
		self.Open_shortcut.activated.connect(self.openFileNameDialog)
		self.Save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
		self.Save_shortcut.activated.connect(self.saveFileDialog)

		self.ScannerTab.triggered.connect(self.Run_Scanner)
		self.Run_shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
		self.Run_shortcut.activated.connect(self.Run_Scanner)

	def Color_Code(self):
		text=self.Code_Area.toPlainText()
		if(text[-5:]==" int "):
			Newint =" <span style=\" font-size:15pt;font:Consolas;color:RED;Bold=true\">int</span>"
			cursor = self.Code_Area.textCursor()
			self.Code_Area.setHtml(text[:-4])
			self.Code_Area.setTextCursor(cursor)
			self.Code_Area.insertHtml(Newint)
			self.Code_Area.setTextColor(QColor(255,255,255))

		print(text)
  
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			with open(fileName,"r+") as file:
				self.Code_Area.setText(file.read())
		
	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"Save File","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
			with open(fileName,"w") as file:
				text = self.Code_Area.toPlainText()
				file.write(text)

	def Run_Scanner(self):
		text = self.Code_Area.toPlainText()
		self.scanner.charPointer=0
		self.Output_Area.clear()
		for index in range(len(text)):
			token = self.scanner.getToken(text)
			if(token != None):
				self.Output_Area.append(token)
def window():
	app = QApplication(sys.argv)
	wind = MyWindow()
	wind.show()
	sys.exit(app.exec_())

window()