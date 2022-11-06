from sys import argv
from webbrowser import open as web_open
from noticeUI import MainClass
from PyQt5.QtWidgets import QApplication
from noticeScrapping import *

if __name__ == "__main__":
    # noticeTitle.csv 초기화
    f = open("noticeTitle.csv", "w", encoding="utf-8-sig", newline="")
    f.close()
    # Crawling part
    for i in range(1, 20):
        KwCrawling(str(i), "noticeTitle.csv")
        CeCrawling(str(i), "CE.csv")
        CsCrawling(str(i), "CS.csv")
        IcCrawling(str(i), "IC.csv")

    # 광운 대학교 로그인 사이트 open
    web_open("https://klas.kw.ac.kr")
    # UI part
    app = QApplication(argv)
    window = MainClass()
    app.exec_()
