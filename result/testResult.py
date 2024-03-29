# -*- coding: utf-8 -*-
from result.HTMLTestRunner import HTMLTestRunner
import unittest
from testCase.testcase_login import Login
from common.getpathInfo import get_path
import os
import time


class TestResult:
    def __init__(self):
        self.path = get_path()
        self.html_report_path = os.path.join(get_path(), "../result/HTMLReport", time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())) + "HTMLReport.html")
        self.text_report_path = os.path.join(get_path(), "../result/TextReport", time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())) + "TextReport.txt")
        self.suite = unittest.TestSuite()

    def get_html_report(self):
        with open(self.html_report_path, 'w', encoding='utf-8') as f:
            runner = HTMLTestRunner(stream=f, title='testReport', description='generated by htmlTestReport', verbosity=3)
            runner.run(self.suite)

    def get_text_result(self):
        with open(self.text_report_path, 'w', encoding='utf-8') as f:
            runner = unittest.TextTestRunner(stream=f, descriptions='generated by textTestReport', verbosity=2)
            runner.run(self.suite)


if __name__ == "__main__":
    h1 = TestResult()
    h1.suite.addTest(Login('test_login'))
    h1.get_html_report()

