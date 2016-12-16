#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from ui_24 import *
from PyQt4.QtGui import *
import sys,random
import re

def generateTotalExpression(inlNumber):        
    Operator = ["+","-","*","/"]  #List of operator 
    lCalcExpression = []   #List of all calculation expression  
    lProcess = [inlNumber]   # for initial, lProcess only has one object. For example, lProcess = [['11.0', '5.0', '4.0', '6.0']]
    
    while len(lProcess)!=0 :    #Only when there has been some objects in lProcess, the program continues
    #removes and returns the last object of the list
    #For the first time, lNmuber = ['11.0', '5.0', '4.0', '6.0']
    #Then we get the lNumber list which has four object.
        lNumber=lProcess.pop()   
        iLen=len(lNumber)  
        i=0  
        #From the first object of the lNumber list, we combine the first object with the rest in order.
        # i presents the position of first object, j presents the position of the rest object
        while i<iLen-1 :  
            iNumber=lNumber[i]  
            j=i+1  
            while j<iLen :  
                jNumber=lNumber[j]  
                #For the two object which be selected, combine them with operators in order to creat expressions
                for sOp in Operator :  
                    lExpr=[]  
                    lExpr.append(iNumber+sOp+jNumber)  
                    #If the operator is "-" or "/", we need to switch the two numbers to creat new expression
                    if sOp=="-" or sOp=="/":  
                        lExpr.append(jNumber+sOp+iNumber)  
                      
                    for sExpr in lExpr:  
                        #Use the current expression and the objects which haven't been used to creat a new list.
                        NewList=[]  
                        k=0  
                        while k<iLen:  
                            if k!=j and k!=i :  
                                NewList.append(lNumber[k])  
                            k=k+1  
                        NewList.append('('+sExpr+')')  
                        #When the new list only have one object, save it in lCalcExpression
                        #Otherwise, save the objects in lProcess to continue combination
                        if len(NewList)==1:  
                            lCalcExpression.append(sExpr)  
                        else:  
                            lProcess.append(NewList)  
                j=j+1  
            i=i+1  
              
    return list(set(lCalcExpression))  
       
def filterResult(inTotalExpr,inExpect):        
    lRtn=[]  
    for sExpr in inTotalExpr:  
        try:  
            Result=eval(sExpr)  
        except:  
            Result=0  
        if Result-inExpect>=-0.0001 and Result-inExpect<=0.0001:  
            lRtn.append(sExpr)
    return lRtn  


class mainwindow(QMainWindow, Ui_MainWindow):  
  def __init__(self,parent=None):              
    super(mainwindow,self).__init__(parent)
    self.setupUi(self)
    self.setWindowTitle("24 GAME")
    self.lineEdit.setText("")
    self.lineEdit.setFocus()
    self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.Show_solution1)
    self.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.random4int)
    self.connect(self.pushButton_3,QtCore.SIGNAL("clicked()"),self.Show_solution2)
    self.connect(self.pushButton_4,QtCore.SIGNAL("clicked()"),self.check)
    
  def findit(self,num,showplace):              
    inNumbers=str(num)
    self.listWidget.clear()
    if len(inNumbers.split(','))!=4 :  
        QMessageBox.about(self,"error",self.tr("input error"))
    lNumbers=inNumbers.split(',')  
    lNumbersFormated=[]  
    for sNumber in lNumbers:  
        lNumbersFormated.append(sNumber+'.0')  
    lFilteredExpr=filterResult(generateTotalExpression(lNumbersFormated),24)  
    i=0  
    if len(lFilteredExpr) == 0:
       QMessageBox.about(self,"No Solution!",self.tr("No Solution!"))
       return
    if showplace == 1:
		for expr in lFilteredExpr:  
			expr=expr.replace(".0","") 
			self.listWidget.addItem("%d >>  %s"%(i,expr))
			i=i+1   
    elif showplace == 2:
		for expr in lFilteredExpr:  
			expr=expr.replace(".0","")
			self.listWidget_2.addItem("%d >>|%s"%(i,expr))
			i=i+1

			
    elif showplace == 3:
#		list=[]   #This is the first way to check the answer by checking if the answer is in the expressions list
#		for expr in lFilteredExpr:   #however, sometimes this way doesn't work, then I choose the second way
#			expr=expr.replace(".0","")  
#
#			list.append(str(expr))
#			i=i+1
		x = self.lineEdit_3.text()
		y = re.sub("\D", " ", x)  #Use Regular expressiong operation to replace +,-*,/,(,) as " "
		target_list = y.split()   # conver string y to list type
		repeat_list = [a for a in lNumbers if a in target_list]  #check how many objects repeat in both input number list and answer list
		if (eval(self.lineEdit_3.text()) > 23.9 
              and eval(self.lineEdit_3.text()) < 24.1
              and len(target_list)==4 
              and len(repeat_list) == 4):
			QMessageBox.about(self,"You got it!",self.tr("You got it!"))
#		if str(self.lineEdit_3.text()) in list:
#			QMessageBox.about(self,"You got it!",self.tr("You got it!"))
		else:
			QMessageBox.about(self,"Wrong! Try again!",self.tr("Wrong! Try again!"))
  def Show_solution1(self):                    
    self.findit(self.lineEdit.text(),1)
  def Show_solution2(self):                    
    if len(self.lineEdit_2.text().split(",")) ==4: 
       self.findit(self.lineEdit_2.text(),2)

  def random4int(self):                        
    num1=random.randint(1,13)
    num2=random.randint(1,13)
    num3=random.randint(1,13)
    num4=random.randint(1,13)	
    self.lineEdit_2.setText("%d,%d,%d,%d"%(num1,num2,num3,num4))
    self.listWidget_2.clear()
  def check(self):                             
    self.findit(self.lineEdit_2.text(),3)
if __name__=="__main__":                       
  app = QApplication(sys.argv)
  dlg = mainwindow()
  dlg.show()
  app.exec_()