import base64
import json
import pickle
import random
import string
import time
import requests
from lib.ShowapiRequest import ShowapiRequest
from PIL import Image
import os


def get_logger():
    import logging
    import logging.handlers
    import datetime

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def get_code(driver, id):#首先将驱动driver传过来，还有验证码id传过来
    # 获取验证码图片
    t = time.time()#获得时间
    path = os.path.dirname(os.path.dirname(__file__)) + r'\\screenshots'#获得当前文件所在的路径
    picture_name1 = path + r'\\' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element_by_id(id)

    left = ce.location['x'] #左顶点x
    top = ce.location['y'] #左底点y
    right = ce.size['width'] + left #右顶点x
    height = ce.size['height'] + top #右底点y

    dpr = driver.execute_script('return window.devicePixelRatio')

    print(dpr)
    im = Image.open(picture_name1) #打开上边截屏的图片
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))#进行抠图

    #将抠出的图片保存为另一张图片
    t = time.time()
    picture_name2 = path + r'\\' + str(t) + '.png'
    img.save(picture_name2)  # 这里就是截取到的验证码图片

    return base64_api('QAQXIAOBU', 'Zhao16388', picture_name2, typeid=3)

    # r = ShowapiRequest("http://route.showapi.com/184-4", "290728", "1bd001f23c874581aac4db788a92c71d")
    # r.addFilePara("image", picture_name2)
    # r.addBodyPara("typeId", "34")
    # r.addBodyPara("convert_to_jpg", "0")
    # r.addBodyPara("needMorePrecise", "0")
    # res = r.post()
    # text = res.json()['showapi_res_body']
    # code = text['Result']
    # return code


def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8)) #ascii_letters：字母，digits：数字，8：随机生成8位
    return rand_str #输入用户名的时候随机生成


#保存cookie
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


#加载cookie
def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
