import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import *
from Task import run_news

class newsWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(newsWindow, self).__init__(parent)
        uic.loadUi("Task/task_news.ui", self)
        self.setTableWidgetData()
        # 윈도우 타이틀, 사이즈 설정
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("NEWS") # 윈도우 타이틀 설정     
        self.show()

        self.label_bar.setStyleSheet('color: white;background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.995, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.305419 rgba(40, 40, 40, 255), stop:0.935961 rgba(10, 11, 18, 0), stop:1 rgba(100, 100, 100, 255)); border=0px')        
               
        
        self.tableWidget.setColumnWidth(0, 450)
        # news section
        self.current_row = 0    # 초기화

        self.btn_issue.clicked.connect(self.load_Issue_news)
        self.Issue_list = run_news.daum_news() 

        self.btn_entertain.clicked.connect(self.load_entertain_news)
        self.enter_list = run_news.daum_entertain() 
        
        self.btn_sport.clicked.connect(self.load_sports_news)
        self.sports_list = run_news.daum_sports() 

        self.btn_politics.clicked.connect(self.load_politics_news)
        self.politics_list = run_news.daum_politics() 

        self.btn_it.clicked.connect(self.load_IT_news)
        self.IT_list = run_news.daum_IT() 

        self.btn_economics.clicked.connect(self.load_eco_news)
        self.eco_list = run_news.daum_economic()        

        # Back: Close Window
        self.btn_back.clicked.connect(self.backToMainWindow)
        self.btn_back.setIcon(QIcon('image_source/home.png'))
        self.btn_back.setIconSize(QSize(60,60))
        self.btn_back.setStyleSheet('border:0px;')

    # 이미지 로드
    def loadImageFromFile(self, source_url, width_size): # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width_size)  # 크기 조절
        return self.qPixmapFileVar
  

    # def news_economics(self):
    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("data"))
    
    def load_eco_news(self):
        self.current_row = 0
        for i in range(len(self.eco_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.eco_list[self.current_row])))             
            self.current_row += 1

    def load_IT_news(self):
        self.current_row = 0        
        for i in range(len(self.IT_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.IT_list[self.current_row])))             
            self.current_row += 1
    
    def load_Issue_news(self):
        self.current_row = 0        
        for i in range(len(self.Issue_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.Issue_list[self.current_row])))             
            self.current_row += 1   

    def load_sports_news(self):
        self.current_row = 0        
        for i in range(len(self.sports_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.sports_list[self.current_row])))             
            self.current_row += 1

    def load_entertain_news(self):
        self.current_row = 0        
        for i in range(len(self.enter_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.enter_list[self.current_row])))             
            self.current_row += 1

    def load_politics_news(self):
        self.current_row = 0        
        for i in range(len(self.politics_list)):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(i + 1)                
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.politics_list[self.current_row])))             
            self.current_row += 1

    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")
