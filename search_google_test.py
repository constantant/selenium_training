import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('chromedriver.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_search(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    search_box = driver.find_element_by_name('q')
    search_box.submit()
    WebDriverWait(driver, 1).until(EC.title_is("webdriver - Поиск в Google"))

