from sys import argv
from noticeUI import Manager
from PyQt5.QtWidgets import QApplication
from noticeScrapping import *



if __name__ == "__main__":
    # Define crawling number constant
    KW_PAGE = 10
    CE_PAGE = 10
    CS_PAGE = 10
    IC_PAGE = 10

    # Crawling part
    crawling(KW_PAGE, "KW.csv")
    crawling(CE_PAGE, "CE.csv")
    crawling(CS_PAGE, "CS.csv")
    crawling(IC_PAGE, "IC.csv")

    # UI 연결
    app = QApplication(argv)
    window = Manager()
    app.exec_()

