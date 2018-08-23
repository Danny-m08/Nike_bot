from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG
from PyQt5 import QtWidgets as QtW
import sys
import os
import selenium




class NikeBot(QtW.QMainWindow):
	
	def __init__(self):
		QtW.QMainWindow.__init__(self)

		self.setFixedSize(800,600)
		
		addProfile = QtW.QAction('New profile',self)
		addProfile.setStatusTip('Create a new profile')
		addProfile.triggered.connect(self.addProfile)
	
		viewProfiles = QtW.QAction('View Profiles',self)
		viewProfiles.triggered.connect(self.viewProfiles)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
		menu_bar.setStyleSheet('Color: RGB(0,0,0)')

		profile_menu = menu_bar.addMenu('Profiles')
		profile_menu.addAction(addProfile)
		profile_menu.addAction(viewProfiles)
		self.WelcomeWindow()

	def WelcomeWindow(self):


		self.setWindowTitle('Sneaker Bot')
		Welcome = QtW.QLabel()
		Welcome.setText('Welcome to sneaker bot')

		
		WelcomeWidget = QtW.QWidget()
		layout = QtW.QVBoxLayout(WelcomeWidget)
		l1 = QtW.QLabel()
		l1.setText('Welcome to Sneaker Bot')
		l1.setAlignment(QtC.Qt.AlignHCenter )
#		WelcomeWidget.addWidget(l1)
		image = QtW.QLabel()
		
		image.setPixmap(QtG.QPixmap('.gitignore/Sneaker_bot.png'))
		layout.addWidget(l1)	
		layout.addWidget(image)
		#WelcomeWidget.addWidget(image)
		self.setCentralWidget(WelcomeWidget)

		
			#	self.Image = DrawImage(self)
		self.show()




	def addProfile(self):
		newprofile = QtW.QGroupBox('Enter all text fields:')
		layout = QtW.QFormLayout()		
		layout.addRow( QtW.QLabel('Name:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Shipping Address:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Billing Address:'), QtW.QLineEdit() )
		layout.addRow( QtW.QLabel('Credit Card #:'), QtW.QLineEdit() )	
		save = QtW.QPushButton('Save', self)
		cancel = QtW.QPushButton( 'Cancel', self)
		layout.setFormAlignment(QtC.Qt.AlignHCenter | QtC.Qt.AlignVCenter ) 
		layout.setSpacing(20)
		layout.setLabelAlignment(QtC.Qt.AlignLeft)
	
		save.clicked.connect(self.saveProfile)
		cancel.clicked.connect(self.WelcomeWindow)
		layout.addRow( save, cancel )	

		newprofile.setLayout(layout)
		self.setCentralWidget(newprofile)
		self.setWindowTitle('Create a new Bot')
		self.show()


	def viewProfiles(self):
		self.setWindowTitle('Current user profiles')
		self.setCentralWidget(None)
		self.show()
	
	


	def saveProfile(self):
		file_selection = QtW.QInputDialog(self)
		file_selection.setInputMode(QtW.QInputDialog.TextInput)
		file_selection.show()



def main():
	app = QtW.QApplication(sys.argv)
	main_window = NikeBot()
	app.exec_()


if __name__ == '__main__': main()	
