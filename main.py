from time import sleep
from testcases import testcase1,testcase2,testcase3
from util import util
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_category import TestCategory

if __name__ == '__main__':
        # testcase1.test1()
        # testcase1.test2()
        # testcase2.test1()
        # testcase2.test2()

        # print(util.gen_random_str())

        # driver = webdriver.Chrome()
        # driver.get('http://localhost:8080/jpress/user/register')
        # driver.maximize_window()
        # sleep(1)
        # print(util.get_code(driver, 'captchaimg'))

        # case01 = TestUserRegister()
        # case01.test_register_code_error()
        # case01.test_register_ok()

        # case02 = TestUserLogin()
        # case02.test_user_login_username_error()
        # case02.test_user_login_ok()

        # case03 = TestAdminLogin()
        # case03.test_admin_login_code_error()
        # case03.test_admin_login_code_ok()

        # 登录成功后才能进行分类的操作
        login = TestAdminLogin()
        login.test_admin_login_code_ok()
        case04 = TestCategory(login)
        case04.test_add_category_error()
        case04.test_add_category_ok()









