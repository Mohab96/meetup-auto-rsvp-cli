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
    xpath = f'//*[@id="event-card-e-{counter}"]/div[2]/div/div[2]/div/div/span'

    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True

    return False


def get_events(browser: webdriver.Chrome, group_urls: list[str]) -> list[str]:
    events_urls = []

    for group_url in group_urls:
        browser.get(group_url + '/events/')
        RSVPed_events_counter = 1

        while RSVPed_events_counter <= 10:
            id = f'event-card-e-{RSVPed_events_counter}'

            try:
                event = browser.find_element(By.ID, id)

                if not_RSVPed(browser, RSVPed_events_counter):
                    events_urls.append(event.get_attribute('href'))
            except NoSuchElementException:
                break

            RSVPed_events_counter += 1

    return events_urls


def rsvp_to_events(browser: webdriver.Chrome, events: list[str]) -> None:
    for event in events:
        browser.get(event)
        get_element(browser, By.XPATH,
                    '//*[@id="main"]/div[4]/div/div/div[2]/div/div[2]/div[3]/button').click()
        try:
            get_element(
                browser, By.XPATH, '//*[@id="modal"]/div/div[1]/div/div/div/div/div[2]/div/div/button').click()
        except NoSuchElementException:
            continue


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
