import pytest
from selenium import webdriver
import time
search_list=['小米11', '小米10至尊纪念版', '小米10', '小米10 青春版 5G', '小米MIX Alpha']

def setup_module():
    global wd
    wd=webdriver.Chrome(r'C:\putao\chromedriver.exe')
    wd.implicitly_wait(5)

def teardowm_module():
    global wd
    wd.quit()

@pytest.mark.parametrize('item',search_list)
def test_search_item(item):
    global wd
    wd.get('https://mi.com/')
    wd.find_element_by_id('search').send_keys(item+'\n')
    time.sleep(2)
    item_titles=wd.find_elements_by_css_selector('.goods-item .title')
    # item_list=[]
    # for item_title in item_titles:
    #     item_list.append(item_title.text)
    # print(item_list)
    titles=[item.text for item in item_titles]
    assert item in titles
    wd.quit()

if __name__=='__main__':
    pytest.main(['-vs','xiaomi_search_test.py'])