# Library
from csv import writer as csv_writer
from requests import get as request_get
from bs4 import BeautifulSoup
from os import path, makedirs
from multiprocessing import Pool, freeze_support
from functools import partial
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# 4개의 크롤링 함수를 묶은 함수
# filename을 통해 어떤 크롤링 함수를 사용할지 결정
# 4개의 프로세스로 멀티프로세싱을 진행하여 크롤링 속도를 향상
def crawling(pageNum, filename):
    # 윈도우에서 멀티 프로세싱 사용할 때 메모리 에러가 발생하여 메모리가 freeze됨
    # 아래의 함수로 해결
    freeze_support()
    iterable = [i for i in range(1, pageNum + 1)]

    # 프로세스를 4개로 지정하여 멀티 프로세싱을 진행 => 크롤링 속도 2배 향상
    pool = Pool(processes=4)

    # 폴더가 없을 시 생성
    if not path.isdir("./csvFiles"):
        makedirs("./csvFiles")

    # csv 폴더에 해당 학부에 대한 csv 파일이 없을 시 csv 파일을 생성
    csvPath = "./csvFiles/" + filename
    if path.isfile(csvPath):
        f = open(csvPath, "w", encoding="utf-8", newline="")
        f.close()

    # filename에 따라서 crawling할 함수를 정해서 실행
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
    # 멀티 프로세싱이 끝난 프로세스들을 종료
    pool.close()
    pool.join()

# 광운대학교 전체 공지사항을 크롤링 하는 함수
def kwCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8", newline="")
    writer = csv_writer(f)

    # set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Request url information from the Server
    url = "https://www.kw.ac.kr/ko/life/notice.jsp?MaxRows=10&tpage=" + str(
        pageNum) + "&searchKey=1&searchVal=&srCategoryId="

    # 서버와 코드 연결
    res = request_get(url, headers=headers)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")
    noticeArea = soup.find('div', 'list-box')
    noticeInfo = noticeArea.find_all("li")

    # [url / title / 작성일 / 수정일 / 기재한 곳 / 조회수 / 고정 or 일반]
    for notice in noticeInfo:
        row = []
        # url / 제목
        row.append("https://www.kw.ac.kr" + notice.find('a')['href'])
        row.append(notice.find('a').find('strong').next_sibling.strip())
        # 작성일 / 수정일 / 기재한 곳 / 조회수
        noticeInfoList = notice.find('p').get_text().strip().split(' ')
        row.append(noticeInfoList[4].strip())
        row.append(noticeInfoList[7].strip())
        row.append(noticeInfoList[9].strip())
        row.append(noticeInfoList[1].strip())
        # 0: fixed / 1 : general
        if notice.find('span', 'ico-notice'):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)

# 광운대학교 컴퓨터정보공학부 공지사항을 크롤링 하는 함수
def ceCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8", newline="")
    writer = csv_writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    # Disable warnings code
    disable_warnings(InsecureRequestWarning)
    # Request url information from the Server
    url = "https://ce.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=2&make=&search=&make=&search="

    # 서버와 코드 연결
    res = request_get(url, headers=headers, verify=False)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance
    soup = BeautifulSoup(res.text, 'lxml')
    noticeArea = soup.find('tbody')
    noticeInfo = noticeArea.find_all('tr')

    # 페이지가 존재하지 않는 경우 return
    if not noticeInfo:
        f.close()
        return

    # [title/ url / 작성일 / 조회수/ 고정 or 일반]를 행 단위로 csv파일에 입력
    for notice in noticeInfo:
        row = []
        # url
        row.append('https://ce.kw.ac.kr:501/' + notice.find('td', 'subject').find('a')['href'])
        # title
        row.append(notice.find('td', 'subject').find('a').get_text().strip())
        # 작성일
        date = notice.find('td', 'w_date').get_text().strip()
        row.append(date)
        # 조회수
        w_cell = notice.find_all('td', 'w_cell')[1].get_text().strip()
        row.append(w_cell)
        # 0: fixed 1: general
        if notice.find('td', "w_cell").find("img"):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)
    f.close()

# 광운대학교 소프트웨어학부 공지사항을 크롤링 하는 함수
def csCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8", newline="")
    writer = csv_writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Disable warnings code
    disable_warnings(InsecureRequestWarning)

    # Request url information from the Server
    url = "https://cs.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=3&make=&search=&make=&search="

    # 서버와 코드 연결
    res = request_get(url, headers=headers, verify=False)

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

    # [url / title / 작성일/ 조회수 / 고정 or 일반]를 행 단위로 csv파일에 입력

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

# 광운대학교 정보융합학부 공지사항을 크롤링 하는 함수
def icCrawling(filename, pageNum):
    # Save result in csv
    csvPath = "./csvFiles/" + filename
    f = open(csvPath, "a", encoding="utf-8", newline="")
    writer = csv_writer(f)

    # Set headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    # Disable warnings code
    disable_warnings(InsecureRequestWarning)

    # Request url information from the Server
    url = "https://ic.kw.ac.kr:501/department_office/lecture.php?page=" + str(
        pageNum) + "&site_type=4&make=&search=&make=&search="

    # 서버와 코드 연결
    res = request_get(url, headers=headers, verify=False)

    # Check success or fail to load url information
    res.raise_for_status()

    # Make a soup instance (crawling part)
    # lxml error 발생 시 lxml library 다운로드 받기
    # 페이지의 원하는 부분을 특정하는 코드
    soup = BeautifulSoup(res.text, "lxml")

    soup = BeautifulSoup(res.text, "lxml")
    noticeArea = soup.find('div', 'board_listW').find('tbody')
    noticeInfo = noticeArea.find_all('tr')

    # 페이지가 존재하지 않는 경우 return
    if not noticeInfo:
        f.close()
        return

    # [url / title / 작성일 / 조회수 / 고정 or 일반]를 행 단위로 csv파일에 입력
    for notice in noticeInfo:
        row = []
        # url 제목
        row.append("https://cs.kw.ac.kr:501/" + notice.find('a')['href'])
        row.append(notice.find('td', "subject").find('a').get_text().strip())
        # 작성일 조회수
        list = notice.find_all('td', "w_cell")
        row.append(notice.find('td', "w_date").get_text().strip())
        row.append(list[1].get_text().strip())
        # 0: fixed 1: general
        if notice.find('td', "w_cell").find("img"):
            row.append("0")
        else:
            row.append("1")
        writer.writerow(row)
    f.close()
