import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


def get_element(browser: webdriver.Chrome, by: By, val: str) -> WebElement:
    time.sleep(5)
    # WebDriverWait(browser, 20).until(EC.presence_of_element_located((by, val)))

    return browser.find_element(by, val)


def get_elements(browser: webdriver.Chrome, by: By, val: str) -> list[WebElement]:
    time.sleep(5)
    # WebDriverWait(browser, 20).until(EC.presence_of_element_located((by, val)))

    return browser.find_elements(by, val)


def login(email: str, password: str) -> None:
    browser.get(
        'https://www.meetup.com/login/?returnUri=https://www.meetup.com/groups/')

    # Entering email
    get_element(browser, By.XPATH, '//*[@id="email"]').send_keys(email)

    # Entering password
    get_element(browser, By.XPATH,
                '//*[@id="current-password"]').send_keys(password)

    # Clicking the login button
    get_element(browser, By.XPATH,
                '//*[@id="main"]/div/div/div/section/form/div[2]/div[1]/button').click()

    time.sleep(5)


def get_groups(browser: webdriver.Chrome) -> list[str]:
    groups = get_elements(browser, By.CSS_SELECTOR,
                          'li.flex.flex-col.justify-between')

    group_urls = []

    for group in groups:
        url = get_element(group, By.CSS_SELECTOR, 'a').get_attribute('href')
        group_urls.append(url)

    return group_urls


def not_RSVPed(browser: webdriver.Chrome, counter) -> bool:
    pass


def get_events(browser: webdriver.Chrome, group_urls: list[str]) -> list[str]:
    pass


def rsvp_to_events(browser: webdriver.Chrome, events: list[str]) -> None:
    pass


def success(browser: webdriver.Chrome) -> None:
    print('RSVPed to all events successfully!')
    browser.close()


if __name__ == '__main__':
    load_dotenv()

    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    login(email, password)

    groups = get_groups(browser)

    events = get_events(browser, groups)

    rsvp_to_events(browser, events)

    success(browser)
