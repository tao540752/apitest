import pytest


class Testlogin():


    def test_case1(self):
        print('打开浏览器')
        print("执行登录测试用例")

    def test_case2(self):
        print('执行购物车测试用例')


class TestLogout():

    def test_case1(self):
        print('执行测试用例1')
        assert  2020==2019

    def test_cese2(self):
        print('执行测试用例2')

if __name__ == '__main__':
    pytest.main(['-vs','./test_login.py'])