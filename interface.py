#!/usr/bin/env python

from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG
from PyQt5 import QtWidgets as QtW
import sys
import os
#import selenium
from multiprocessing import process


class Bot_thread(QtC.QThread):
	def __init__(self,parent):
		QtC.QThread.__init__(self)
		


	def run(self):
		print('starting bot script...')
		os.system('./Bot.sh')


class NikeBot(QtW.QMainWindow):	
	def Run(self):
		self.thread = Bot_thread(None)
		self.thread.start()		
	
	def __init__(self):
		QtW.QMainWindow.__init__(self)

		self.setFixedSize(800,600)

		

		#	Actions for Profile Menu

		activeProfile = QtW.QAction('View active profile',self)
		activeProfile.triggered.connect(self.activeProfile)
		
		addProfile = QtW.QAction('New profile',self)
		addProfile.setStatusTip('Create a new profile')
		addProfile.triggered.connect(self.addProfile)
	
		viewProfiles = QtW.QAction('View Profiles',self)
		viewProfiles.triggered.connect(self.viewProfiles)
	
		#	Actions for Run Menu
	
		run = QtW.QAction('Run bot',self)
		run.triggered.connect(self.Run)
		


		#Menu Bar

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
	#	menu_bar.setStyleSheet('Color: RGB(0,0,0)')

		profile_menu = menu_bar.addMenu('Profiles')
		profile_menu.addAction(activeProfile)
		profile_menu.addAction(addProfile)
		profile_menu.addAction(viewProfiles)
			
		run_menu = menu_bar.addMenu('Run')
		run_menu.addAction(run)
		
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
	
		name = QtW.QLineEdit()
		address = QtW.QLineEdit()
		zipcode = QtW.QLineEdit()
		state = QtW.QLineEdit()	
		#zipcode = QtW.QLineEdit()
		address.setTextMargins(0,0,150,0)
		state.setTextMargins(0,0,50,0)
		zipcode.setTextMargins(0,0,50,0)

		print(zipcode.getTextMargins())
		address.setPlaceholderText('Ex: 233 S Wacker Dr')	
		name.setPlaceholderText('Ex: Johnny Appleseed')
		state.setPlaceholderText('Ex: IL')	
		zipcode.setPlaceholderText('Ex: 60606')

		
		
		layout.insertRow(0,'Name: ', name)
		layout.insertRow(1,'Address: ',address)
		layout.addRow(zipcode)
		layout.addRow(state)	
		save = QtW.QPushButton('Save', self)

		cancel = QtW.QPushButton( 'Cancel', self)
		layout.setFormAlignment(QtC.Qt.AlignHCenter | QtC.Qt.AlignTop ) 
		layout.setSpacing(20)
		layout.setLabelAlignment(QtC.Qt.AlignLeft)
		print(layout.itemAt(0,1))
		save.clicked.connect(self.saveProfile)
		cancel.clicked.connect(self.WelcomeWindow)
		layout.addRow( save, cancel )	

		newprofile.setLayout(layout)
		self.setCentralWidget(newprofile)
		self.setWindowTitle('Create a new Bot')
		self.show()
		print(name.text())
	

	def viewProfiles(self):
		self.setWindowTitle('Current user profiles')
		self.setCentralWidget(None)			#Finish later
		self.show()
	
	def activeProfile(self):
		window = QtW.QMessageBox(self)
		window.setWindowTitle('Active profile')
		if (os.path.exists('profiles/activeProfile')):
			pass					#Finish Later
		else:
			window.setText('No active profile')	
		window.setStandardButtons(QtW.QMessageBox.Ok)
		window.show()

	def saveProfile(self):
#		file_selection = QtW.QInputDialog.getText(self,'Enter unique profile name','File name', QtW.QLineEdit.Normal, 'Please refrain from using spaces')
			
		file_selection = QtW.QInputDialog(self)
	
		file_selection.setInputMode(QtW.QInputDialog.TextInput)
		file_selection.setLabelText('Enter unique profile name')
		file_selection.resize(400,300)
		file_selection.setOkButtonText('Save')
		ok = file_selection.exec_()
	#	button = file_selection.buttonClicked(b)
		file_name = file_selection.textValue()
		if ' ' in file_name or file_name == '' and ok:
			warning = QtW.QMessageBox(QtW.QMessageBox.Critical, 'Warning', 'Do not use any spacing within your profile name',QtW.QMessageBox.Ok, parent = file_selection)
			warning.exec_()
			self.saveProfile()

		elif ok:
			if file_name in os.listdir('.gitignore'):
				warning = QtW.QMessageBox(QtW.QMessageBox.Critical, 'Warning', 'Profile name already in use',QtW.QMessageBox.Ok, parent = file_selection)
				warning.exec_()
				self.saveProfile()		
			else:
				open('.gitignore/' + file_name,'w')
				
				
		else:
			self.addProfile()	
			
		



def main():
	app = QtW.QApplication(sys.argv)
	main_window = NikeBot()
	app.exec_()


if __name__ == '__main__': main()	
