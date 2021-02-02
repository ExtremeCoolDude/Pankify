#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QApplication, QVBoxLayout, QMessageBox, QDesktopWidget, QHBoxLayout, QFileDialog, QTextEdit, QPlainTextEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
import os
import PySimpleGUI
from PyQt5.QtCore import QProcess

class GUILazy(QWidget):
   
    def __init__(self):
        super().__init__()     
        self.initUI()
                     
    def initUI(self):
        
        self.setGeometry(400,400,400, 220)
        self.setWindowTitle('Pankify')
        self.setWindowIcon(QIcon('icon.png'))
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        
        
        horibox = QHBoxLayout()
        horibox.addStretch(1)
        voribox = QVBoxLayout()
        voribox.addStretch(1)
        voribox.addLayout(horibox)
        
        self.setLayout(voribox)
        
        
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('Convert pgn to anki ')
        openbutton = QPushButton('Browse', self)
        openbutton.setToolTip('Click to open a file')
        openbutton.clicked.connect(self.getfile)
        
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
      
        savebutton = QPushButton("Where to save ?", self)
        savebutton.setToolTip("Click to save")
        savebutton.clicked.connect(self.savefile)
        
        operatebutton = QPushButton("Start optimization")
        operatebutton.clicked.connect(self.callparserlogic)
       
        horibox.addWidget(openbutton)
        horibox.addWidget(savebutton)
        horibox.addWidget(qbtn)
        horibox.addWidget(operatebutton)
        
       
     
    def getfile(self):
            ofilename = QFileDialog.getOpenFileName(self,'OpenFile')
            print(ofilename)
            if ofilename != '':
                filename = list(ofilename).pop(0)
                with open('temp1.pankify','w') as ff:
                    ff.writelines(filename)
            

            
            
    def savefile(self):
            sfilename = QFileDialog.getSaveFileName(self, 'Save File')
            print(sfilename)
            if sfilename != '' :
                filename = list(sfilename).pop(0)
                with open('temp2.pankify','w') as gg:
                    gg.writelines(filename)
    
    def message(self,s):
        self.text.appendPlainText(s)
        
    def callparserlogic(self):
        self.message("Preparing!")
        self.runscript = QProcess()
        self.runscript.start("python3", ['parserlogic.py'])
        
        
                
            
    
   
            



           
        
