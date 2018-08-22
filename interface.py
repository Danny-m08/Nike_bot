from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG
from PyQt5 import QtWidgets as QtW
import sys
import os


class addProfile(QtW.QWidget):
	def __init__(self):
		QtW.QWidget.__init__(self)

	def view(self):
		pass

class NikeBot(QtW.QMainWindow):
	
	def __init__(self):
		QtW.QMainWindow.__init__(self)
		self.setFixedSize(800,600)
		self.setWindowTitle('Sneaker Bot')




		addProfile = QtW.QAction('New profile',self)
		addProfile.setStatusTip('Create a new profile')
		addProfile.triggered.connect(self.addProfile)
		


		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
		profile_menu = menu_bar.addMenu('Profiles')
		profile_menu.addAction(addProfile)
	#	self.Image = DrawImage(self)
		self.show()




	def addProfile(self):
		self.newprofile = QtW.QGroupBox('Enter all fields:')
		layout = QtW.QFormLayout()		
		layout.addRow( QtW.QLabel('Name:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Shipping Address:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Billing Address:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Credit Card #:'), QtW.QLineEdit() )	
		layout.addRow( QtW.QPushButton('Save', self), QtW.QPushButton( 'Cancel', self))

		self.newprofile.setLayout(layout)
		self.setCentralWidget(self.newprofile)
		self.setWindowTitle('Create a new Bot')
		self.show()
	
def main():
	app = QtW.QApplication(sys.argv)
	main_window = NikeBot()
	app.exec_()

if __name__ == '__main__': main()	
