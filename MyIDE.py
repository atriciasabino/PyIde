#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qsci import *
import sys
 
class IDE(QsciScintilla):
    def __init__(self,parent=None):
        super(IDE,self).__init__(parent)
        fonte = QFont()
        fonte.setFamily("Consolas")
        fonte.setPointSize(10)
        fonte_margem = QFontMetrics(fonte)
        self.setFont(fonte)
        self.setMarginsFont(fonte)
        self.setMarginWidth(0,fonte_margem.width("0000")-1)
        self.setMarginLineNumbers(0,True)
        self.setEdgeMode(QsciScintilla.EdgeLine)
        self.setEdgeColumn(80)
        self.setEdgeColor(QColor("#FF0000"))
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#F8F8FF"))
        self.setMarginsBackgroundColor(QColor("#2F4F4F")) # #000000
        self.setMarginsForegroundColor(QColor("#CCCCCC")) #CCCCCC
        self.setFoldMarginColors(QColor("#F5F5F5"),QColor("#856363")) ##856363 #333300 #qcolor #F5F5F5 
        sintaxe = QsciLexerPython()
        self.setLexer(sintaxe)
        self.resize(500,650)
root = QApplication(sys.argv)
app = IDE()
app.show()
root.exec_()
