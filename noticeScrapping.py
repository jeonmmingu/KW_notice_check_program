# Library
import csv
import requests
from bs4 import BeautifulSoup
from os import path, makedirs
from multiprocessing import Pool
from functools import partial


def crawling(pageNum, filename):
    iterable = [i for i in range(1, pageNum + 1)]
    pool = Pool(processes=4)

    # 폴더가 없을 시 생성
    if not path.isdir("./csvFiles"):
        makedirs("./csvFiles")

    csvPath = "./csvFiles/" + filename
    if path.isfile(csvPath):
        f = open(csvPath, "w", encoding="utf-8-sig", newline="")
        f.close()

    if filename == "KW.csv":
        func = partial(kwCrawling, filename)
        pool.map(func, iterable)
    elif filename == "CE.csv":
        func = partial(ceCrawling, filename)
        pool.map(func, iterable)
    elif filename == "CS.csv":
        func = partial(csCrawling, filename)
        pool.map(func, iterable)
    elif filename == "IC.csv":
        func = partial(icCrawling, filename)
        pool.map(func, iterable)

    pool.close()
    pool.join()


def kwCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Request url information from the Server
    url = "https://www.kw.ac.kr/ko/life/notice.jsp?MaxRows=10&tpage=" + str(
        pageNum) + "&searchKey=1&searchVal=&srCategoryId="

    # 서버와 코드 연결
    res = requests.get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")
    noticeArea = soup.find('div', 'list-box')
    noticeInfo = noticeArea.find_all("li")

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수]를 행 단위로 csv파일에 입력 (9 line :writerow(list)사용)

    for notice in noticeInfo:
        row = []
        # url / 제목
        row.append("https://www.kw.ac.kr" + notice.find('a')['href'])
        row.append(notice.find('a').find('strong').next_sibling.strip())
        # 작성일 / 수정일 / 기재한 곳 / 조회수
        noticeInfoList = notice.find('p').get_text().strip().split(' ')
        row.append(noticeInfoList[4])
        row.append(noticeInfoList[7])
        row.append(noticeInfoList[9])
        row.append(noticeInfoList[1])
        # 0: fixed / 1 : general
        if notice.find('span', 'ico-notice'):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)


def ceCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Request url information from the Server
    url = "https://ce.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=2&make=&search=&make=&search="

    # 서버와 코드 연결
    res = requests.get(url, headers=headers, verify=False)

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
        row = []
        # url / 제목
        row.append("https://ce.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        row.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        row.append(notice.find('td', "w_date").get_text().strip())
        row.append(notice.select("td.w_cell")[1].get_text().strip())
        # 0: fixed / 1 : general
        if notice.find('td', "w_cell").find("img"):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)
    f.close()


def csCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Request url information from the Server
    url = "https://cs.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=3&make=&search=&make=&search="

    # 서버와 코드 연결
    res = requests.get(url, headers=headers, verify=False)

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
        row = []
        # url / 제목
        row.append("https://cs.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        row.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        row.append(notice.find('td', "w_date").get_text().strip())
        row.append(notice.select("td.w_cell")[1].get_text().strip())
        # 0: fixed / 1 : general
        if notice.find('td', "w_cell").find("img"):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)
    f.close()


def icCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Request url information from the Server
    url = "https://ic.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=4&make=&search=&make=&search="

    # 서버와 코드 연결
    res = requests.get(url, headers=headers, verify=False)

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
        row = []
        # url / 제목
        row.append("https://ic.kw.ac.kr:501" + notice.find('td', "subject").find('a')['href'])
        row.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 / 조회수
        row.append(notice.find('td', "w_date").get_text().strip())
        row.append(notice.select("td.w_cell")[1].get_text().strip())
        # 0: fixed / 1 : general
        if notice.find('td', "w_cell").find("img"):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)
    f.close()
