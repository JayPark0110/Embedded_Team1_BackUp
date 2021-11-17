import sys
import imaplib # 이메일 라이브러리
import email 
from email.header import decode_header, make_header
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from Task import run_email


class emailWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(emailWindow, self).__init__(parent)
        uic.loadUi("Task/task_email (2).ui", self)
        #self.setGeometry(0, 0, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setupUI()
        
        # 사용자 이메일(@daum.net제외), 비밀번호 입력
        self.user_id = "nalbojima"
        self.user_pw = "2agl2sn2st#"
        self.current_row = 0
        self.num_to_load = 24 # 초기화시에 처음에 이메일 몇개 불러올건지에 대한 갯수

        self.label_bar.setStyleSheet('color: white;background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.995, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.305419 rgba(40, 40, 40, 255), stop:0.935961 rgba(10, 11, 18, 0), stop:1 rgba(100, 100, 100, 255)); border=0px')
        
        # 이메일 로딩 버튼 연결
        # self.btn_load_email.clicked.connect(self.loadEmailFunction_test)        
        self.btn_next_page.clicked.connect(self.loadNextPage)
        self.btn_next_page.setIcon(QIcon('image_source/next_p.png'))
        self.btn_next_page.setIconSize(QSize(50,50))
        self.btn_next_page.setStyleSheet('border:0px;')

        self.btn_prev_page.clicked.connect(self.loadPrevPage)
        self.btn_prev_page.setIcon(QIcon('image_source/prev_p.png'))
        self.btn_prev_page.setIconSize(QSize(50,50))
        self.btn_prev_page.setStyleSheet('border:0px;')
        
        # back 버튼 기능 연결
        self.btn_back.clicked.connect(self.backToMainWindow)
        self.btn_back.setIcon(QIcon('image_source/home.png'))
        self.btn_back.setIconSize(QSize(60,60))
        self.btn_back.setStyleSheet('border:0px;')

        # run_email.py 에서 메일 리스트 가져옴
        self.mail_list = run_email.imap_daum(self.user_id, self.user_pw, self.num_to_load)   
        
        self.loadEmailFunction_test()
        self.show()

    # UI 타이틀, 크기 조절
    def setupUI(self):
        # self.tableWidget = QTableWidget(self)
        self.setTableWidgetData() 
        self.setWindowTitle("e-mail")  # 윈도우 타이틀 설정
        
        self.tableWidget.setColumnWidth(0, 90)        
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 300)
        
        

    # 텍스트 샘플
    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("data"))        
        self.tableWidget.setItem(0, 1, QTableWidgetItem("data"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("data"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("data"))

    # 이메일 로딩 테스트함수
    def loadEmailFunction_test(self):
        # 최대 3개 페이지까지 구성, 한 페이지당 메일 목록 8개
        if (self.current_row + 8) <= (self.num_to_load):
            print(f"email loading... start row : {self.current_row}")
            for i in range(0, self.num_to_load // 3):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
                self.tableWidget.setRowCount(i + 1)                
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.mail_list[self.current_row][0]))) # 도착시각 (Nov 11, 12:30)
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.mail_list[self.current_row][1]))) # 보낸 사람 
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.mail_list[self.current_row][2]))) # 제목 
                self.current_row += 1
            print(f"email loaded. current row : {self.current_row}")
        else:
            print("마지막 페이지입니다.")

    # 다음페이지, 이전페이지 로딩
    def loadNextPage(self):
        if (self.current_row + 8) <= (self.num_to_load):
            print("load next page...")
            self.loadEmailFunction_test() 
        else:
            print("마지막 페이지입니다.")
    
    def loadPrevPage(self):
        if (self.current_row - 16) >= 0: 
            print("load prev page...")
            self.current_row -= 16 # 8만큼의 인덱스를 빼줌
            self.loadEmailFunction_test()
        else:
            print("첫 페이지 입니다.")


    
    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")


    # # 이메일 스크래퍼로부터 정보 받아오는 함수
    # def loadEmail(self):
    #     # email=[{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"}]
    #     # row = 0
    #     # self.tableWidget.setRowCount(len(email))
    #     # for mail in email:
    #     #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(mail["from"]))
    #     #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(mail["Title"]))
    #     #     self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("test"))

    #     #     row += 1
    #     pass


