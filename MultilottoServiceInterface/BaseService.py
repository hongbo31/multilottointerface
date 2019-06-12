from common.readCase import *
from common.readConfig import *
from common.configHttp import ConfigHttp

"""
    基本接口类，其他接口需继承该类，传入case_name生成对应的接口对象
    具体请求直接实现request_service方法即可

"""


class BaseService:

    def __init__(self, case_name):
        self.config = ReadConfig()
        self.case_excle = ReadCase('mltest.xlsx', '工作表1')  # 写死，就用这个excle作为接口测试的用例
        self.case_name = case_name
        self.serivce_url = self.case_excle.get_interface_url(self.case_name)
        self.service_header = self.case_excle.get_intetface_headers(self.case_name)
        self.service_data = self.case_excle.get_interface_data(self.case_name)
        self.service_method = self.case_excle.get_method(self.case_name)
        self.config_http = ConfigHttp(self.serivce_url, self.service_header, self.service_data, self.service_method)

    # 默认返回dict类型的result， 如果需要str类型的，设置str_format=True
    def set_case_name(self, case_name):
        self.case_name = case_name


    def get_case_name(self):
        return self.case_name

     # 传入result_type_is_str字段，传入False返回dict类型，传入True返回Str类型
    def request_service(self, result_type_is_str):
        return self.config_http.request_result(result_type_is_str)

    # 获得返回状态码
    def status_code(self):
        return self.config_http.status_code

    # 获得返回的text文本
    def text(self):
        return self.config_http.text

    # 获得返回的content
    def content(self):
        return self.config_http.content

    # 返回一个cookiejar
    def cookies(self):
        return self.config_http.cookies

    def cookie(self):
        return self.config_http.get_cookie()

    def add_cookie(self, cookie):
        self.service_header.update(cookie)
        return self.service_header


if __name__ == '__main__':
    bs = BaseService("login_by_account")
    print(bs.case_name)
    print(bs.request_service(False))

