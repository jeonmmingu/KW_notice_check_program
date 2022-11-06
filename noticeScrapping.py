# Library
import csv
import requests
from bs4 import BeautifulSoup


def KwCrawling(pageNum, filename):
    # Save result in csv
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Request url information from the Server
    url = "https://www.kw.ac.kr/ko/life/notice.jsp?MaxRows=10&tpage="+pageNum+"&searchKey=1&searchVal=&srCategoryId="
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    # 서버와 코드 연결
    res = requests.get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")
    noticeArea = soup.find('div', 'list-box')
    noticeInfo = noticeArea.find_all('div', "board-text")

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수]를 행 단위로 csv파일에 입력 (9 line :writerow(list)사용)

    for notice in noticeInfo:
        colum= []
        # url / 제목
        colum.append("https://www.kw.ac.kr" + notice.find('a')['href'])
        colum.append(notice.find('a').find('strong').next_sibling.strip())
        # 작성일 / 수정일 / 기재한 곳 / 조회수
        noticeInfoList = notice.find('p').get_text().strip().split(' ')
        colum.append(noticeInfoList[4])
        colum.append(noticeInfoList[7])
        colum.append(noticeInfoList[9])
        colum.append(noticeInfoList[1])
        writer.writerow(colum)

def CeCrawling(pageNum, filename):
    # Save result in csv
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Request url information from the Server
    url = "https://ce.kw.ac.kr:501/department_office/lecture.php?page=" + pageNum + "&site_type=2&make=&search=&make=&search="
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    # 서버와 코드 연결
    res = requests.get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")

    noticeInfo = soup.find('table', "board-list").find("tbody").find_all('tr')

    # 페이지가 존재하지 않는 경우 return
    if not noticeInfo:
        f.close()
        return

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수]를 행 단위로 csv파일에 입력 (9 line :writerow(list)사용)

    for notice in noticeInfo:
        colum = []
        # url / 제목
        if notice.find('td', "w_cell").find("img"):
            colum.append("0")
        else:
            colum.append("1")
        colum.append("https://ce.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        colum.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        colum.append(notice.find('td', "w_date").get_text().strip())
        colum.append(notice.select("td.w_cell")[1].get_text().strip())
        writer.writerow(colum)

    f.close()

def CsCrawling(pageNum, filename):
    # Save result in csv
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Request url information from the Server
    url = "https://cs.kw.ac.kr:501/department_office/lecture.php?page=" + pageNum + "&site_type=3&make=&search=&make=&search="
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    # 서버와 코드 연결
    res = requests.get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")

    noticeInfo = soup.find('table', "board-list").find("tbody").find_all('tr')

    # 페이지가 존재하지 않는 경우 return
    if not noticeInfo:
        f.close()
        return

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수]를 행 단위로 csv파일에 입력 (9 line :writerow(list)사용)

    for notice in noticeInfo:
        colum = []
        # url / 제목
        if notice.find('td', "w_cell").find("img"):
            colum.append("0")
        else:
            colum.append("1")
        colum.append("https://cs.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        colum.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        colum.append(notice.find('td', "w_date").get_text().strip())
        colum.append(notice.select("td.w_cell")[1].get_text().strip())
        writer.writerow(colum)

    f.close()

def IcCrawling(pageNum, filename):
    # Save result in csv
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Request url information from the Server
    url = "https://ic.kw.ac.kr:501/department_office/lecture.php?page=" + pageNum + "&site_type=4&make=&search=&make=&search="
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    # 서버와 코드 연결
    res = requests.get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")

    noticeInfo = soup.find('table', "board-list").find("tbody").find_all('tr')

    # 페이지가 존재하지 않는 경우 return
    if not noticeInfo:
        f.close()
        return

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수]를 행 단위로 csv파일에 입력 (9 line :writerow(list)사용)

    for notice in noticeInfo:
        colum = []
        # url / 제목
        if notice.find('td', "w_cell").find("img"):
            colum.append("0")
        else:
            colum.append("1")
        colum.append("https://ic.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        colum.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        colum.append(notice.find('td', "w_date").get_text().strip())
        colum.append(notice.select("td.w_cell")[1].get_text().strip())
        writer.writerow(colum)

    f.close()

