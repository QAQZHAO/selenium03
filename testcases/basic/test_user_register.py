from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #等到某个元素出现，或者alert出现
from selenium.webdriver.support.wait import WebDriverWait #等待
from util import util


#用户注册的类
class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确' #期望的验证信息

        self.driver.find_element(By.NAME,'username').send_keys(username)
        self.driver.find_element(By.NAME,'email').send_keys(email)

        self.driver.find_element(By.NAME,'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME,'confirmPwd').send_keys(confirmPwd)

        self.driver.find_element(By.NAME,'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present()) #等待5秒钟，如果超时会弹出timeout，期望一个alert出现alert_is_present
        alert = self.driver.switch_to.alert #切换到这个弹框
        # python 的断言
        assert alert.text == expected #拿到弹框上的信息
        alert.accept()

        sleep(5)

    # 测试成功
    def test_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        self.driver.find_element(By.NAME,'username').clear()
        self.driver.find_element(By.NAME,'username').send_keys(username)
        # email
        self.driver.find_element(By.NAME,'email').clear()
        self.driver.find_element(By.NAME,'email').send_keys(email)
        # 密码
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element(By.NAME,'confirmPwd').clear()
        self.driver.find_element(By.NAME,'confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        # 输入验证码
        self.driver.find_element(By.NAME,'captcha').clear()
        self.driver.find_element(By.NAME,'captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证
        assert alert.text == expected
        alert.accept()

        sleep(5)

        self.driver.close()
        self.driver.quit()