import unittest
from MultilottoServiceInterface.userService.login import Login
import json
from common.log import Log


class LoginTest(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("测试开始")

    def test_login_suc(self):
        """登入测试用例!!!!"""
        lg_suc = Login('login_by_account')
        result = lg_suc.login_service()
        self.log.info("登录的status code为:" + str(lg_suc.status_code()))
        "断言二：结果msg信息是否是登录成功" + str(self.assertEqual(result['info']['countryid'], 'JP'))


    # def test_login_error(self):
    #     """登入错误的测试用例"""
    #     s = ConfigHttp().run_main('get', self.login_url_error, self.login_headers_error, self.login_data_error)
    #     self.assertEqual(s['code'], -1)
    #     self.assertEqual(s['message'], '账号密码错误')

    def tearDown(self):
        self.log.info('测试结束')


if __name__ == '__main__':
    unittest.main().runTests()
