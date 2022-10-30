import sys
import csv
from PyQt5.QtWidgets import *
import webbrowser


# PY 형식 파일 import
from noticeUI import Ui_MainWindow
from noticeScrapping import crawling


# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # UI 선언
        main_ui = Ui_MainWindow()
        # UI 준비
        main_ui.setupUi(self)
        self.setTableWidgetData(main_ui.tableWidget)
        # 화면을 보여준다.
        self.show()

    def setTableWidgetData(self, tableWidget):
        # csv 파일 정보를 list로 받아옴
        noticeInfo = self.loadNoticeInfo()
        # 행/열 개수 설정
        tableWidget.setRowCount(len(noticeInfo))
        tableWidget.setColumnCount(5)
        # 행의 폭을 열 마다 다르게 조정
        tableWidget.setColumnWidth(0, int(self.width() * 15 / 30))
        tableWidget.setColumnWidth(1, int(self.width() * 3 / 30))
        tableWidget.setColumnWidth(2, int(self.width() * 3 / 30))
        tableWidget.setColumnWidth(3, int(self.width() * 4 / 30))
        tableWidget.setColumnWidth(4, int(self.width() * 2 / 30))
        # 열 이름 붙이는 부분®
        colum_title = ["제목", "작성일", "수정일", "기재한 곳", "조회수"]
        tableWidget.setHorizontalHeaderLabels(colum_title)
        # 리스트 테이블 내용 입력
        list_seq = 0
        row = 0
        column = 0
        url = ""
        for i in noticeInfo:
            for j in i:
                # url
                if list_seq == 0:
                    url = j
                # 제목
                elif list_seq == 1:
                    label1 = QLabel()
                    label1.setText('<a href="'+url+'">'+j+'</a>')
                    label1.setOpenExternalLinks(True)
                    tableWidget.setCellWidget(column, row, label1)
                    row += 1
                else:
                    tableWidget.setItem(column, row, QTableWidgetItem(j))
                    row += 1
                list_seq += 1
            list_seq = 0
            row = 0
            column += 1

    # csv 파일로 부터 정보를 불러오는 부분
    def loadNoticeInfo(self) -> list:
        filename = "noticeTitle.csv"
        f = open(filename, "r", encoding="utf-8-sig")
        rdr = csv.reader(f)
        a = []
        for i in rdr:
            a.append(i)
        f.close()
        return a


if __name__ == "__main__":
    # noticeTitle.csv 초기화
    f = open("noticeTitle.csv", "w", encoding="utf-8-sig", newline="")
    f.close()
    # Crawling part
    for i in range(1, 20):
        crawling(str(i))
    # 광운대학교 로그인 사이트 open
    webbrowser.open("https://klas.kw.ac.kr")
    # UI part
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()
