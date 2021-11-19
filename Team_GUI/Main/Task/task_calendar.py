import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QDate
from calender_source import Calender


class calendarWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(calendarWindow, self).__init__(parent)
        uic.loadUi("Task/task_calender_calType_02.ui", self)
        self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setupTableUI()
        self.setupcalendarUI()
        self.show()
        
        # 캘린더 데이터 받아옴
        # (17,1,0: "테스트 11.17") # 현재 자동으로 받아온 상태
        self.data = Calender.GetEvents(0)        
        print(f"현재데이터: {self.data}")
        # 스타트 타임 - (17,1,1).hour // (17,1,1).minute
        # 엔드 타임 (17,1,2).hour // (17,1,2).minute

        # 데이터 관리 변수
        self.current_row = 0
        self.num_to_load = 24
        self.month = 0
        self.date = 0

        # 캘린더 위젯 기능
        self.calendarWidget.clicked.connect(self.calendarClicked)  # 날짜 선택하여 클릭
        # self.calendarWidget.selectionChanged.connect(self.calendarClicked) # 날짜 선택 변경시 이벤트
        self.calendarWidget.currentPageChanged.connect(
            self.calendarPageChanged)  # 달력 다른 페이지로 넘길 때 이벤트

        # 버튼 기능 연결
        # self.btn_load_schedule.clicked.connect(self.loadSchedule)
        self.btn_next_month.clicked.connect(self.loadNextMonth)
        self.btn_prev_month.clicked.connect(self.loadPrevMonth)
        self.btn_today.clicked.connect(self.loadToday)

        # back 버튼 기능 연결
        self.btn_back.clicked.connect(self.backToMainWindow)

    # tableWidget UI 타이틀, 크기 조절

    def setupTableUI(self):
        # self.tableWidget = QTableWidget(self)
        self.setWindowTitle("Calendar")  # 윈도우 타이틀 설정
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 300)

    # 캘린더 위젯 UI 초기화
    def setupcalendarUI(self):
        self.selected_date = self.calendarWidget.selectedDate()  # QDate 타입으로 저장
        self.label_selectedDate.setText(
            self.selected_date.toString())  # QDate 타입 -> String 타입 캐스팅

    # calendarWidget 시그널에 연결된 함수들
    # 클릭한 날짜 표시
    def calendarClicked(self):
        self.selected_date = self.calendarWidget.selectedDate()  # QDate 타입으로 저장
        self.str_date_info = self.selected_date.toString()
        day, self.month, self.date, year = self.str_date_info.split()
        self.month = int(self.month)
        self.date = int(self.date)  # str -> int, date를 인덱스로 활용하기 위해 정수형으로 캐스팅
        # print(self.data[date][0])
        # print(self.selected_date)

        # 로드된 데이터 중에서 해당 날짜에 맞는 데이터(스케쥴)가 몇 개인지 확인하고, 해당 갯수만큼 테이블 위젯에 표시
        self.task_num = self.data[self.date][0]
        print(f"{self.date}의 스케줄 갯수: {self.task_num}")
        if self.task_num == 0:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("--"))  # 도착시각 (Nov 11, 12:30)
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("--"))  # 보낸 사람
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("스케줄이 없습니다"))  # 스케쥴 내용 (17, 1, 0)
        else:
            for i in range(0, self.task_num):
                print("스케쥴을 표시합니다")
                self.tableWidget.setRowCount(i + 1)
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.data[self.date][i + 1][1].hour)+"시 "+str(self.data[self.date][i + 1][1].minute)+"분"))  # 도착시각 (Nov 11, 12:30)
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.data[self.date][i + 1][2].hour)+"시 "+str(self.data[self.date][i + 1][2].minute)+"분"))  # 보낸 사람
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.data[self.date][i + 1][0])))  # 스케쥴 내용 (17, 1, 0)

        # print(date) # 날짜 확인
        self.label_selectedDate.setText(self.selected_date.toString())  # QDate 타입 -> String 타입 캐스팅

    # def calendarSelectionChanged(self) :
    #     self.selected_date = self.calendarWidget.selectedDate() # QDate 타입으로 저장
    #     print(self.selected_date)
    #     self.label_selectedDate.setText(self.selected_date.toString()) # QDate 타입 -> String 타입 캐스팅

    def calendarPageChanged(self):
        self.year = str(self.calendarWidget.yearShown()) + "년"
        self.month = str(self.calendarWidget.monthShown()) + "월"
        print(self.year, self.month)

    #버튼에 연결된 함수들
    # def loadScheduleFunction(self):
    #     # 최대 3개 페이지까지 구성, 한 페이지당 스케쥴 목록 8개
    #     if (self.current_row + 8) <= (self.num_to_load):
    #         print("loading schdule...")
    #         for i in range(0, 100):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
    #             self.tableWidget.setRowCount(i + 1)
    #             self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 도착시각 (Nov 11, 12:30)
    #             self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 보낸 사람
    #             self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 제목
    #         print(f"schedule loaded. current row : {self.current_row}")

    def loadPrevMonth(self):
        if self.month == 12: # 12월의 날짜를 클릭한 상태에서 이전 달 버튼을 누르면
            self.month = 11
            self.data = Calender.GetEvents(0) # 11월의 데이터로 갱신(갱신 후 11월의 날짜 클릭)
            print(self.data)
        self.calendarWidget.showPreviousMonth()
        # elif self.month == 1: # 1월인 상태에서 
        #     self.month = 12
        #     self.data = Calender.GetEvents(1) 

    def loadNextMonth(self):
        if self.month == 11: # 11월의 날짜를 클릭한 상태에서 다음 달 버튼을 누르면
            self.month = 12
            self.data = Calender.GetEvents(1) # 12월의 데이터로 갱신(갱신 후 12월의 날짜 클릭)
            print(self.data)
        self.calendarWidget.showNextMonth()
        # elif self.month == 12:
            

    def loadToday(self):
        self.calendarWidget.showToday()

    # 현재 dialog 창 종료

    def backToMainWindow(self):
        self.close()
        print("close dialog...")
