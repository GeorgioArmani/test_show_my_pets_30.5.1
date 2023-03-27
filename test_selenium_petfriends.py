import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(autouse=True)
def set():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('egorkaivanov98@gmail.com')
    pytest.driver.find_element(By.ID, 'pass').send_keys('RollsRoyce23')

    time.sleep(2)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(5)

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'h1').text == 'PetFriends'

    # Неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Явные ожидания
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выйти')]")))

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ' '
        assert names[i].text != ' '
        assert descriptions[i].text != ' '
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
