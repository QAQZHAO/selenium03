import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import pytesseract

def test1():
    #打开谷歌浏览器
    browser = webdriver.Chrome()
    #打开首页
    browser.get('http://localhost:8080/jpress/user/register')
    browser.maximize_window()

    #获取验证码图片
    t = time.time() #获得当前的时间
    picture_name1 = str(t)+'.png' #str(t)：将时间转化成字符串
    browser.save_screenshot(picture_name1)#调用save_screenshot进行截屏

    ce = browser.find_element(By.ID,'captchaimg')
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width']+left
    height = ce.size['height']+top

    im = Image.open(picture_name1)
    img = im.crop((left,top,right,height))#crop：抠图 #from PIL import Image

    t = time.time()
    picture_name2 = str(t)+'.png'

    img.save(picture_name2)#这里就是截取到的验证码图片，通过save方法将抠出的图保存为第二张图片
    browser.close()

def test2():
    image1 = Image.open('test.png')
    str = pytesseract.image_to_string(image1)
    print(str)




















