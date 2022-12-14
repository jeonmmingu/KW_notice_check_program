from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from noticeScrapping import *
from functools import partial
from webbrowser import open as web_open
from csv import reader
from csv import writer as csv_writer
from os import path
import sys


# 첫 화면
class Ui_MainWindow(object):
    # MainWindow의 요소들을 선언 및 초기화 하는 함수
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 750)
        self.center(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(120, 40, 800, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.totalNoticeLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalNoticeLabel.setGeometry(QtCore.QRect(160, 370, 91, 36))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.totalNoticeLabel.setFont(font)
        self.totalNoticeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalNoticeLabel.setObjectName("totalNoticeLabel")
        self.ceNoticeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ceNoticeLabel.setGeometry(QtCore.QRect(720, 370, 231, 36))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.ceNoticeLabel.setFont(font)
        self.ceNoticeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ceNoticeLabel.setObjectName("ceNoticeLabel")
        self.csNoticeLabel = QtWidgets.QLabel(self.centralwidget)
        self.csNoticeLabel.setGeometry(QtCore.QRect(110, 650, 191, 36))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.csNoticeLabel.setFont(font)
        self.csNoticeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.csNoticeLabel.setObjectName("csNoticeLabel")
        self.icNoticeLabel = QtWidgets.QLabel(self.centralwidget)
        self.icNoticeLabel.setGeometry(QtCore.QRect(750, 650, 171, 36))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.icNoticeLabel.setFont(font)
        self.icNoticeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.icNoticeLabel.setObjectName("icNoticeLabel")
        self.totalNoticeImage = QtWidgets.QPushButton(self.centralwidget)
        self.totalNoticeImage.setGeometry(QtCore.QRect(130, 200, 150, 150))
        KWimage = self.resource_path("Image\KW.png")
        fullPathKW = QtCore.QDir.current().absoluteFilePath(KWimage)
        winPathKW = fullPathKW.replace('\\', '/')

        self.totalNoticeImage.setStyleSheet('''QPushButton{
                                                    border-image:url("''' + winPathKW + '''");
                                                    border:0px;
                                                }

                                                QPushButton:hover{
                                                    border-image:url("''' + winPathKW + '''") 20 20 20 20;
                                                    border:0px;
                                                }'''
                                            )
        self.totalNoticeImage.setText("")
        self.totalNoticeImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.totalNoticeImage.setObjectName("totalNoticeImage")
        self.ceNoticeImage = QtWidgets.QPushButton(self.centralwidget)
        self.ceNoticeImage.setGeometry(QtCore.QRect(750, 200, 150, 150))
        CEimage = self.resource_path("Image\CE.png")
        fullPathCE = QtCore.QDir.current().absoluteFilePath(CEimage)
        winPathCE = fullPathCE.replace('\\', '/')

        self.ceNoticeImage.setStyleSheet('''QPushButton{
                                                    border-image:url("''' + winPathCE + '''");
                                                    border:0px;
                                                }

                                                QPushButton:hover{
                                                    border-image:url("''' + winPathCE + '''") 20 20 20 20;
                                                    border:0px;
                                                }'''
                                         )
        self.ceNoticeImage.setText("")
        self.ceNoticeImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ceNoticeImage.setObjectName("ceNoticeImage")
        self.csNoticeImage = QtWidgets.QPushButton(self.centralwidget)
        self.csNoticeImage.setGeometry(QtCore.QRect(130, 470, 150, 150))
        CSimage = self.resource_path("Image\CS.png")
        fullPathCS = QtCore.QDir.current().absoluteFilePath(CSimage)
        winPathCS = fullPathCS.replace('\\', '/')

        self.csNoticeImage.setStyleSheet('''QPushButton{
                                                    border-image:url("''' + winPathCS + '''");
                                                    border:0px;
                                                }

                                                QPushButton:hover{
                                                    border-image:url("''' + winPathCS + '''") 20 20 20 20;
                                                    border:0px;
                                                }'''
                                         )
        self.csNoticeImage.setText("")
        self.csNoticeImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csNoticeImage.setObjectName("csNoticeImage")
        self.icNoticeImage = QtWidgets.QPushButton(self.centralwidget)
        self.icNoticeImage.setGeometry(QtCore.QRect(750, 470, 150, 150))
        ICimage = self.resource_path("Image\IC.png")
        fullPathIC = QtCore.QDir.current().absoluteFilePath(ICimage)
        winPatIC = fullPathIC.replace('\\', '/')

        self.icNoticeImage.setStyleSheet('''QPushButton{
                                                    border-image:url("''' + winPatIC + '''");
                                                    border:0px;
                                                }

                                                QPushButton:hover{
                                                    border-image:url("''' + winPatIC + '''") 20 20 20 20;
                                                    border:0px;
                                                }'''
                                         )
        self.icNoticeImage.setText("")
        self.icNoticeImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icNoticeImage.setObjectName("icNoticeImage")
        self.kwImage = QtWidgets.QPushButton(self.centralwidget)
        self.kwImage.setGeometry(QtCore.QRect(400, 290, 240, 240))
        KWUimage = self.resource_path("Image\KWU.png")
        fullPathKWU = QtCore.QDir.current().absoluteFilePath(KWUimage)
        winPatKWU = fullPathKWU.replace('\\', '/')

        KWU20image = self.resource_path("Image\KWU_20%.png")
        fullPathKWU20 = QtCore.QDir.current().absoluteFilePath(KWU20image)
        winPatKWU20 = fullPathKWU20.replace('\\', '/')

        self.kwImage.setStyleSheet('''QPushButton{
                                                    border-image:url("''' + winPatKWU + '''");
                                                    border:0px;
                                                }

                                                QPushButton:hover{
                                                    border-image:url("''' + winPatKWU20 + '''");
                                                    border:0px;
                                                }'''
                                   )
        self.kwImage.setText("")
        self.kwImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kwImage.setObjectName("kwImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # MainWindow의 요소들을 세부적으로 설정하는 함수
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KWNOTICE"))
        window_ico = self.resource_path('Image\Kwnotice.ico')
        iconWinpath = QtCore.QDir.current().absoluteFilePath(window_ico)
        real_winpath = iconWinpath.replace('\\', '/')
        MainWindow.setWindowIcon(QtGui.QIcon(real_winpath))

        self.titleLabel.setText(_translate("MainWindow", "K W  N O T I C E"))
        self.totalNoticeLabel.setText(_translate("MainWindow", "전체"))
        self.ceNoticeLabel.setText(_translate("MainWindow", "컴퓨터정보공학부"))
        self.csNoticeLabel.setText(_translate("MainWindow", "소프트웨어학부"))
        self.icNoticeLabel.setText(_translate("MainWindow", "정보융합학부"))
        self.kwImage.clicked.connect(lambda: self.printKlasPage())
    # exe파일로 만들 시, Resource들의 절대 경로를 알아야 하기 때문에
    # 절대 경로를 찾을 수 있는 함수 생성
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
        return path.join(base_path, relative_path)
    # UI Label들의 글자를 가운데로 정렬 시키는 함수
    def center(self, Mainwindow):
        qr = Mainwindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Mainwindow.move(qr.topLeft())
    # 광운대학교 로고를 눌렀을 때 klas 페이지를 띄우도록 하는 kwImage 버튼의 clicked lambda 함수
    def printKlasPage(self):
        web_open("http://klas.kw.ac.kr")

# 공지사항 화면
class Ui_noticeWindow(object):
    # 공지사항 window 요소들을 선언 및 초기화 하는 함수
    def __init__(self, noticeWindow, filename, flag):
        noticeWindow.setObjectName("noticeWindow")
        noticeWindow.resize(1300, 750)
        self.center(noticeWindow)
        self.centralwidget = QtWidgets.QWidget(noticeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 20, 60, 32))
        self.backButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.backButton.setObjectName("backButton")
        self.majorTitle = QtWidgets.QLabel(self.centralwidget)
        self.majorTitle.setGeometry(QtCore.QRect(310, 30, 400, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(24)
        self.majorTitle.setFont(font)
        self.majorTitle.setAutoFillBackground(False)
        self.majorTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.majorTitle.setTextFormat(QtCore.Qt.AutoText)
        self.majorTitle.setScaledContents(True)
        self.majorTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.majorTitle.setObjectName("majorTitle")
        self.noticeTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.noticeTableWidget.setGeometry(QtCore.QRect(40, 110, 931, 581))
        self.noticeTableWidget.setObjectName("noticeTableWidget")
        self.noticeTableWidget.setColumnCount(0)
        self.noticeTableWidget.setRowCount(0)
        self.fixButton = QtWidgets.QPushButton(self.centralwidget)
        self.fixButton.setGeometry(QtCore.QRect(40, 80, 436, 30))
        self.fixButton.setObjectName("fixButton")
        self.generalButton = QtWidgets.QPushButton(self.centralwidget)
        self.generalButton.setGeometry(QtCore.QRect(476, 80, 436, 30))
        self.generalButton.setObjectName("fixButton_2")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(912, 80, 57, 30))
        self.refreshButton.setObjectName("refreshButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1040, 80, 181, 30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bookMarkTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.bookMarkTableWidget.setGeometry(QtCore.QRect(1010, 110, 241, 581))
        self.bookMarkTableWidget.setObjectName("bookMarkTableWidget")
        self.bookMarkTableWidget.setColumnCount(0)
        self.bookMarkTableWidget.setRowCount(0)
        noticeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(noticeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 24))
        self.menubar.setObjectName("menubar")
        noticeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(noticeWindow)
        self.statusbar.setObjectName("statusbar")
        noticeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(noticeWindow, filename, flag)
        QtCore.QMetaObject.connectSlotsByName(noticeWindow)
    # NoticeWindow 요소들을 세부적으로 설정하는 함수
    def retranslateUi(self, noticeWindow, filename, flag):
        _translate = QtCore.QCoreApplication.translate
        if filename == "KW.csv":
            noticeWindow.setWindowTitle(_translate("noticeWindow", "전체 공지사항"))
            self.majorTitle.setText(_translate("noticeWindow", "전체 공지사항"))
        if filename == "CE.csv":
            noticeWindow.setWindowTitle(_translate("noticeWindow", "컴퓨터정보공학부 공지사항"))
            self.majorTitle.setText(_translate("noticeWindow", "컴퓨터정보공학부 공지사항"))
        if filename == "CS.csv":
            noticeWindow.setWindowTitle(_translate("noticeWindow", "소프트웨어학부 공지사항"))
            self.majorTitle.setText(_translate("noticeWindow", "소프트웨어학부 공지사항"))
        if filename == "IC.csv":
            noticeWindow.setWindowTitle(_translate("noticeWindow", "정보융학학부 공지사항"))
            self.majorTitle.setText(_translate("noticeWindow", "정보융합학부 공지사항"))
        self.backButton.setText(_translate("noticeWindow", "Back"))
        self.refreshButton.setText(_translate("noticeWindow", "Refresh"))
        self.fixButton.setText(_translate("noticeWindow", "고정 공지사항"))
        self.label.setText(_translate("noticeWindow", "즐겨찾기"))
        self.generalButton.setText(_translate("noticeWindow", "일반 공지사항"))
        self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget, filename, flag)
        self.setBookMarkTableWidgetData(self.bookMarkTableWidget, filename)
        self.fixButton.clicked.connect(
            lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                  filename,
                                                  "0"))
        self.generalButton.clicked.connect(
            lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                  filename,
                                                  "1"))
        if filename == "KW.csv":
            self.refreshButton.clicked.connect(lambda: crawling(3, filename))
            self.refreshButton.clicked.connect(
                lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                      filename, flag))
        elif filename == "CE.csv":
            self.refreshButton.clicked.connect(lambda: crawling(3, filename))
            self.refreshButton.clicked.connect(
                lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                      filename, flag))
        elif filename == "CS.csv":
            self.refreshButton.clicked.connect(lambda: crawling(3, filename))
            self.refreshButton.clicked.connect(
                lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                      filename, flag))
        elif filename == "IC.csv":
            self.refreshButton.clicked.connect(lambda: crawling(3, filename))
            self.refreshButton.clicked.connect(
                lambda: self.setNoticeTableWidgetData(noticeWindow, self.noticeTableWidget, self.bookMarkTableWidget,
                                                      filename, flag))
    # crawling을 통해 저장한 csv파일의 내용을 table로 전달하여 화면에 나오도록 하는 함수
    def setNoticeTableWidgetData(self, noticewindow, tableWidget, bookMarkTableWidget, filename, flag):
        if filename == "KW.csv":
            # csv 파일 정보를 list로 받아옴
            noticeInfo = self.loadNoticeInfo(filename, flag)
            # 행/열 개수 설정
            tableWidget.setRowCount(len(noticeInfo))
            tableWidget.setColumnCount(6)
            # 행의 폭을 열 마다 다르게 조정
            tableWidget.setColumnWidth(5, int(noticewindow.width() * 1 / 50))
            tableWidget.setColumnWidth(4, int(noticewindow.width() * 2 / 50))
            tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            # 열 이름 붙이는 부분
            colum_title = ["제목", "작성일", "수정일", "기재한 곳", "조회수", "Add"]
            tableWidget.setHorizontalHeaderLabels(colum_title)
            # 리스트 테이블 내용 입력
            list_seq = 0
            row = 0
            column = 0
            url = ""
            buttonList = []
            for i in noticeInfo:
                hyperlink = ""
                for j in i:
                    # url
                    if list_seq == 0:
                        url = j
                    # 제목
                    elif list_seq == 1:
                        label1 = QLabel()
                        hyperlink = "<a href=\"" + url + "\">" + j + "</a>"
                        label1.setText(hyperlink)
                        label1.setOpenExternalLinks(True)
                        tableWidget.setCellWidget(column, row, label1)
                        row += 1
                    else:
                        tableWidget.setItem(column, row, QTableWidgetItem(j))
                        row += 1
                    list_seq += 1
                # add 부분에 button 추가
                button = QPushButton()
                button.setText("")
                buttonList.append([button, hyperlink, column])
                list_seq = 0
                row = 0
                column += 1
            for button in buttonList:
                button[0].clicked.connect(partial(self.addBookMark, button[1], bookMarkTableWidget, filename))
                tableWidget.setCellWidget(button[2], 5, button[0])
        else:
            # csv 파일 정보를 list로 받아옴
            noticeInfo = self.loadNoticeInfo(filename, flag)
            # 행/열 개수 설정
            tableWidget.setRowCount(len(noticeInfo))
            tableWidget.setColumnCount(4)
            # 행의 폭을 열 마다 다르게 조정
            tableWidget.setColumnWidth(2, int(tableWidget.width() * 3 / 50))
            tableWidget.setColumnWidth(3, int(tableWidget.width() * 2 / 50))
            tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            # 열 이름 붙이는 부분
            colum_title = ["제목", "작성일", "조회수", "Add"]
            tableWidget.setHorizontalHeaderLabels(colum_title)
            # 리스트 테이블 내용 입력
            list_seq = 0
            row = 0
            column = 0
            url = ""
            buttonList = []
            for i in noticeInfo:
                hyperlink = ""
                for j in i:
                    # url
                    if list_seq == 0:
                        url = j
                    # 제목
                    elif list_seq == 1:
                        label1 = QLabel()
                        hyperlink = "<a href=\"" + url + "\">" + j + "</a>"
                        label1.setText(hyperlink)
                        label1.setOpenExternalLinks(True)
                        tableWidget.setCellWidget(column, row, label1)
                        row += 1
                    else:
                        tableWidget.setItem(column, row, QTableWidgetItem(j))
                        row += 1
                    list_seq += 1
                # add 부분에 button 추가
                button = QPushButton()
                button.setText("")
                buttonList.append([button, hyperlink, column])
                list_seq = 0
                row = 0
                column += 1

            for button in buttonList:
                button[0].clicked.connect(partial(self.addBookMark, button[1], bookMarkTableWidget, filename))
                tableWidget.setCellWidget(button[2], 3, button[0])
    # csv파일을 읽어 해당 정보를 2중 리스트 형태로 반환하는 함수
    def loadNoticeInfo(self, filename, flag) -> list:
        path = "./csvFiles/" + filename
        f = open(path, "r", encoding="utf-8")
        rdr = reader(f)
        a = []
        for i in rdr:
            if i[-1] == flag:
                i.pop()
                a.append(i)
        f.close()
        return a
    # noticeTable의 add 버튼을 눌렀을 때 실행되는 lambda 함수
    # bookmark에 관한 csv파일에 추가된 정보를 저장하는 함수
    def addBookMark(self, titleLabel, bookMarkTableWidget, major):
        f = open("BookMark/KW_BookMark.csv", "r", encoding="utf-8")

        if major == "KW.csv":
            f = open("BookMark/KW_BookMark.csv", "r", encoding="utf-8")
        elif major == "CE.csv":
            f = open("BookMark/CE_BookMark.csv", "r", encoding="utf-8")
        elif major == "CS.csv":
            f = open("BookMark/CS_BookMark.csv", "r", encoding="utf-8")
        elif major == "IC.csv":
            f = open("BookMark/IC_BookMark.csv", "r", encoding="utf-8")
        rdr = reader(f)
        result = []
        for i in rdr:
            result.append(i)
        for i in result:
            if i[0] == titleLabel:
                Qtwid = QtWidgets.QWidget(self.centralwidget)
                QMessageBox.about(Qtwid, "중복 에러", "이미 즐겨 찾기에 존재하는 공지입니다.")
                return
        if major == "KW.csv":
            f = open("BookMark/KW_BookMark.csv", "a", encoding="utf-8", newline="")
        elif major == "CE.csv":
            f = open("BookMark/CE_BookMark.csv", "a", encoding="utf-8", newline="")
        elif major == "CS.csv":
            f = open("BookMark/CS_BookMark.csv", "a", encoding="utf-8", newline="")
        elif major == "IC.csv":
            f = open("BookMark/IC_BookMark.csv", "a", encoding="utf-8", newline="")
        writer = csv_writer(f)
        writer.writerow([titleLabel])
        f.close()
        self.setBookMarkTableWidgetData(bookMarkTableWidget, major)
    # BookMarkTable의 del 버튼을 눌렀을 때 실행되는 lambda 함수
    # bookmark에 관한 csv파일에 del버튼에 해당하는 정보를 삭제하는 함수
    def delBookMark(self, titleLabel, bookMarkTableWidget, major):
        f = open("BookMark/KW_BookMark.csv", "r", encoding="utf-8")
        if major == "KW.csv":
            f = open("BookMark/KW_BookMark.csv", "r", encoding="utf-8")
        elif major == "CE.csv":
            f = open("BookMark/CE_BookMark.csv", "r", encoding="utf-8")
        elif major == "CS.csv":
            f = open("BookMark/CS_BookMark.csv", "r", encoding="utf-8")
        elif major == "IC.csv":
            f = open("BookMark/IC_BookMark.csv", "r", encoding="utf-8")
        rdr = reader(f)
        result = []
        for i in rdr:
            result.append(i)

        for i in result:
            if i[0] == titleLabel:
                result.remove(i)

        if major == "KW.csv":
            f = open("BookMark/KW_BookMark.csv", "w", encoding="utf-8", newline="")
        elif major == "CE.csv":
            f = open("BookMark/CE_BookMark.csv", "w", encoding="utf-8", newline="")
        elif major == "CS.csv":
            f = open("BookMark/CS_BookMark.csv", "w", encoding="utf-8", newline="")
        elif major == "IC.csv":
            f = open("BookMark/IC_BookMark.csv", "w", encoding="utf-8", newline="")
        writer = csv_writer(f)
        writer.writerows(result)
        f.close()

        self.setBookMarkTableWidgetData(bookMarkTableWidget, major)
    # 해당하는 BookMark csv파일의 정보를 BookMarkTable에 전달하여 정보를 출력하는 함수
    def setBookMarkTableWidgetData(self, bookMarkTableWidget, major):
        bookMarkInfo = []
        if major == "KW.csv":
            bookMarkInfo = self.loadBookMarkInfo("BookMark/KW_BookMark.csv")
        elif major == "CE.csv":
            bookMarkInfo = self.loadBookMarkInfo("BookMark/CE_BookMark.csv")
        elif major == "CS.csv":
            bookMarkInfo = self.loadBookMarkInfo("BookMark/CS_BookMark.csv")
        elif major == "IC.csv":
            bookMarkInfo = self.loadBookMarkInfo("BookMark/IC_BookMark.csv")

        # 행/열 개수 설정
        bookMarkTableWidget.setRowCount(len(bookMarkInfo))
        bookMarkTableWidget.setColumnCount(2)
        # 행의 폭을 열 마다 다르게 조정
        bookMarkTableWidget.setColumnWidth(1, int(bookMarkTableWidget.width() * 1 / 40))
        bookMarkTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        # 열 이름 붙이는 부분
        colum_title = ["제목", "Del"]
        bookMarkTableWidget.setHorizontalHeaderLabels(colum_title)
        # 내용 추가
        row = 0
        column = 0
        for i in bookMarkInfo:
            label = QLabel()
            label.setText(i[0])
            label.setOpenExternalLinks(True)
            bookMarkTableWidget.setCellWidget(row, column, label)
            column += 1
            button = QPushButton()
            button.setText("")
            button.clicked.connect(partial(self.delBookMark, i[0], self.bookMarkTableWidget, major))
            bookMarkTableWidget.setCellWidget(row, column, button)
            row += 1
            column = 0
    # bookmark csv파일을 읽어 해당 정보를 2중 리스트 형태로 반환하는 함수
    def loadBookMarkInfo(self, filename) -> list:
        f = open(filename, "r", encoding="utf-8")
        rdr = reader(f)
        a = []
        for i in rdr:
            a.append(i)
        f.close()
        return a
    # UI label의 글자를 중앙으로 정렬하는 함수
    def center(self, Mainwindow):
        qr = Mainwindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Mainwindow.move(qr.topLeft())

# 화면 관리자
class Manager(QMainWindow):
    # 초기에 즐겨찾기 관련 폴더 혹은 csv파일이 없는 경우 생성 및
    # 첫 화면(MainWindow)을 실행하도록 하는 초기 함수
    def __init__(self):
        # 즐겨찾기 관련 폴더 혹은 csv 파일이 없는 경우 생성
        if not path.isdir("./BookMark"):
            makedirs("./BookMark")
        if not path.isfile("./BookMark/KW_BookMark.csv"):
            f = open("./BookMark/KW_BookMark.csv", "w")
            f.close()
        if not path.isfile("./BookMark/CE_BookMark.csv"):
            f = open("./BookMark/CE_BookMark.csv", "w")
            f.close()
        if not path.isfile("./BookMark/CS_BookMark.csv"):
            f = open("./BookMark/CS_BookMark.csv", "w")
            f.close()
        if not path.isfile("./BookMark/IC_BookMark.csv"):
            f = open("./BookMark/IC_BookMark.csv", "w")
            f.close()
        # 첫 화면
        QMainWindow.__init__(self)
        self.mainWindow()
    # MainWindow에서 설정한 4개의 버튼(totalNoticeImage, ceNoticeImage, csNoticeImage, icNoticeImage)
    # 을 click 했을 때 버튼에 해당하는 NoticeWindow를 실행 시키도록 하는 lambda 함수
    def noticeWindow(self, filename, flag):
        ui = Ui_noticeWindow(self, filename, flag)
        ui.backButton.clicked.connect(lambda: self.mainWindow())
        self.show()
    # NoticeWindow의 backButton을 clicked 했을 때 MainWindow를 실행 시키도록 하는 lambda 함수
    def mainWindow(self):
        ui = Ui_MainWindow(self)
        ui.totalNoticeImage.clicked.connect(lambda: self.noticeWindow("KW.csv", '0'))
        ui.ceNoticeImage.clicked.connect(lambda: self.noticeWindow("CE.csv", '0'))
        ui.csNoticeImage.clicked.connect(lambda: self.noticeWindow("CS.csv", '0'))
        ui.icNoticeImage.clicked.connect(lambda: self.noticeWindow("IC.csv", '0'))
        self.show()
    # exe파일로 만들 시, Resource들의 절대 경로를 알아야 하기 때문에
    # 절대 경로를 찾을 수 있는 함수 생성

