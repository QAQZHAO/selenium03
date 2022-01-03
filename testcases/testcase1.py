from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui


def test1():
    print('test1')


def test2():
    driver = webdriver.Chrome()
    driver.get('http://jpress.io/user/register')
    driver.maximize_window()
    sleep(1)
    elem = driver.find_element(By.ID,'agree')
    rect = elem.rect
    print(rect)  # 拿到该元素的坐标
    pyautogui.click(rect['x']+300,rect['y']+475) #具体的偏移量可以通过截图计算 #import pyautogui
    sleep(5)



