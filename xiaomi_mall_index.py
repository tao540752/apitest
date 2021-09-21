import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

def setup_module():
    global wd
    wd = webdriver.Chrome(r'C:\putao\chromedriver.exe')
    wd.get('https://www.mi.com/')
    print('执行初始化')

def teardown_module():
    global wd
    wd.quit()
    print('执行清除')

def test_hot_item():
    global wd
    wd.implicitly_wait(5)
    wd.maximize_window()
    xiaomi_menu=wd.find_element_by_css_selector('#J_navCategory+li')
    ac=ActionChains(wd)
    ac.move_to_element(xiaomi_menu).perform()
    time.sleep(2)
    items = wd.find_elements_by_css_selector('#J_navMenu .title')
    titles=[]
    for item in items:
        titles.append(item.text)

    assert titles==['小米11', '小米10至尊纪念版', '小米10', '小米10 青春版 5G', '小米MIX Alpha']

def test_reami():
    print('执行红米测试任务')



if __name__=='__main__':
    pytest.main(['-vs','xiaomi_mall_index.py','--alluredir=tmp/my_allure_results'])
    os.system('allure serve tmp/my_allure_results')