from PySide6 import QtCore ,QtGui ,QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'icons'))

class PrimitiveCreatorDialog(QtWidgets.QDialog) :
	def __init__(self,parent = None) :
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('Primitivecretor')

		self.main_Layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_Layout)

		self.Primitive_listwidget = QtWidgets.QListWidget()
		self.Primitive_listwidget.setIconSize(QtCore.QSize(60,60))
		self.Primitive_listwidget.setSpacing(8)
		self.Primitive_listwidget.setViewMode(QtWidgets.QListView.IconMode)
		self.Primitive_listwidget.setMovement(QtWidgets.QListView.Static)
		self.Primitive_listwidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_Layout.addWidget(self.Primitive_listwidget)

		self.name_Layout =QtWidgets.QHBoxLayout()
		self.main_Layout.addLayout(self.name_Layout)

		self.name_label = QtWidgets.QLabel('Name : ')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_Layout.addWidget(self.name_label)
		self.name_Layout.addWidget(self.name_lineEdit)

		self.button_lay = QtWidgets.QHBoxLayout()
		self.main_Layout.addLayout(self.button_lay)
		self.create_but = QtWidgets.QPushButton('create')
		self.cancel_but = QtWidgets.QPushButton('cancel')
		self.button_lay.addStretch()
		self.button_lay.addWidget(self.create_but)
		self.button_lay.addWidget(self.cancel_but)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['cone','cube' , 'sphere','torus']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH,f'{prim}.png')))
			self.Primitive_listwidget.addItem(item)

def run() :
	global ui 

	try:
		ui.close
	except :
		pass
	prt = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent= prt)
	ui.show()