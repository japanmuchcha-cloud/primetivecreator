from Pyside6 import QtCore ,QtGui ,QtWidgets
from shiboken6 import wrapTnstance
import maya.OpenMayaUI as omui

class PrimitiveCreatorDialog(QtWidgets.QDialog) :
	def __init__(self,parent = None) :
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('Primitivecretor')

	def run() :
		global ui 
		
		try:
			ui.close
		except :
			pass
		prt = wrapTnstance(int(omui.WQtUill.mainWindow()),QtWidgets.QtWidgets)
		ui = PrimitiveCreatorDialog(parent = prt)
		ui.show