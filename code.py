import datetime 
import time
import requests
from bs4 import BeautifulSoup
import tkinter
import subprocess
import sys


now = datetime.datetime.now() ##현재 시간

url = 'https://school.jbedu.kr/namwon-h/M01040601/list'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

menu = []
length_of_menu = 0

def day_of_the_week(week_day, lang_type='en'): #요일 말하기 함수 복붙 ㅎ
  
    tm = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if lang_type == 'ko':
        tm = ['월', '화', '수', '목', '금', '토', '일']
    return tm[week_day]

if now.hour >= 13 : ##suck식
    for i in range(15):  # suck식 반찬 개수 구하기
        temp = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(3) > dl > dd.tch-lnc > ul > li:nth-child(' + str(length_of_menu + 1) + ')')
        if str(temp) == 'None':
            break
        length_of_menu += 1

    for i in range(0, length_of_menu):  ## suck식 크롤링
        element = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(3) > dl > dd.tch-lnc > ul > li:nth-child(' + str(i + 1) + ')')
        menu.append(element.get_text()) #텍스트만 뽑는것(내 공부)
else: ##중식
    for i in range(15):  # 중식 반찬 개수 구하기
        temp = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(2) > dl > dd.tch-lnc > ul > li:nth-child(' + str(length_of_menu + 1) + ')')
        if str(temp) == 'None':
         break
        length_of_menu += 1


    for i in range(0, length_of_menu):  ## 중식크롤링
        element = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(2) > dl > dd.tch-lnc > ul > li:nth-child(' + str(i + 1) + ')')
        menu.append(element.get_text())

good = [1, 2, 6, 10, 13, 15, 16] 
goodgaesoo = 0

for goodgoodgood in good:
    for i in range(0, length_of_menu):
        if menu[i].find(str(goodgoodgood)) != -1:
            if goodgoodgood == 1:
                if menu[i][menu[i].find(str(goodgoodgood)) + 1] == '.':
                    goodgaesoo += 1
            elif goodgoodgood == 13:
                goodgaesoo += 0.7
            else:
                goodgaesoo += 1
            
if __name__ == '__main__': # 오늘의 날짜 복붙
  
    today = "{wday}요일 ".format(
    year=time.localtime().tm_year, month=time.localtime().tm_mon,
    day=time.localtime().tm_mday, wday=day_of_the_week(time.localtime().tm_wday, 'ko')
    )


  # 여기부터는 출력부분

script_path = "project1.py" 

window=tkinter.Tk()
window.title("Today's menu")
window.geometry("550x600+721+262")
window.resizable(True, True)
text=tkinter.Text(window)



if now.hour >= 13:
    text.insert(tkinter.CURRENT, str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 " + str(today) + "석식\n") #날짜임 today는 요일 위 if문장에서 추가
else:
    text.insert(tkinter.CURRENT, str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 " + str(today) + "중식\n")


if goodgaesoo > 9:
    text.insert("current", "오늘의 급식 개(같이)추(천)~\n")
elif 6 < goodgaesoo <= 9:
    text.insert("current", "평타치\n")
else:
    text.insert("current", "오늘은.. Umm...\n")

text.insert("current", "\n")

for i in range(0, length_of_menu):  ## 뒤에 있는 숫자들 없애기 
    if menu[i].find('(') != -1:
        temp = menu[i][0:menu[i].find('(')]
        menu[i] = temp
    text.insert("current", menu[i] + "\n")

text.pack()

text.configure(font=("Courier", 26, "italic"))

window.mainloop()


