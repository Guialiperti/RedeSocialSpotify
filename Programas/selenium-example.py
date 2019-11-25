# standard python libraries
from time import sleep
from getpass import getpass

# pip install selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# the file save.py must be in the same folder
from save import Saver


# A proper driver for your operating system can be downloaded from
# https://sites.google.com/a/chromium.org/chromedriver/downloads.
# Please check your Chrome version before downloading the driver.
DRIVER_PATH = r'C:\Users\marce\Desktop\Nova pasta\chromedriver.exe'
OUTPUT_PATH = r'linkedin'

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

SLEEP_TIME = 2


def get_username(url):
    left = url.rfind('/', 0, -1) + 1
    return url[left:-1]


def get_name(browser):
    element = browser.find_element_by_css_selector('.inline.t-24.t-black.t-normal.break-words')
    return element.text


def get_usernames(browser, selector):
    usernames = set()
    currY = browser.execute_script('return window.pageYOffset;')

    while True:
        while True:
            elements = browser.find_elements_by_css_selector(selector)
            for element in elements:
                href = element.get_attribute('href')
                username = get_username(href)
                usernames.add(username)

            browser.execute_script('window.scrollBy(0, {});'.format(WINDOW_HEIGHT))
            nextY = browser.execute_script('return window.pageYOffset;')

            if currY == nextY:
                break

            currY = nextY
            sleep(SLEEP_TIME)

        try:
            element = browser.find_element_by_css_selector('.artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view')
        except NoSuchElementException:
            break

        if element.get_attribute('disabled') is not None:
            break

        element.click()
        sleep(SLEEP_TIME)

    return usernames


def main():
    saver = Saver(OUTPUT_PATH)

    email = input('Email: ')
    password = getpass('Password: ')

    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    browser.get('https://www.linkedin.com/login')
    sleep(SLEEP_TIME)

    browser.find_element_by_id('username').send_keys(email)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_css_selector('.btn__primary--large.from__button--floating').click()
    sleep(SLEEP_TIME)

    browser.get('https://www.linkedin.com/in/')
    sleep(SLEEP_TIME)

    ego_username = get_username(browser.current_url)

    name = get_name(browser)

    browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections')
    sleep(SLEEP_TIME)

    usernames = get_usernames(browser, '.mn-connection-card__link.ember-view')

    saver.save(ego_username, name, usernames)

    for username in usernames:
        if saver.exists(username):
            continue

        browser.get('https://www.linkedin.com/in/' + username)
        sleep(SLEEP_TIME)

        name = get_name(browser)

        alter_usernames = set()

        try:
            element = browser.find_element_by_id('highlights-container')
        except NoSuchElementException:
            pass
        else:
            for a in element.find_elements_by_tag_name('a'):
                try:
                    h3 = a.find_element_by_tag_name('h3')
                except NoSuchElementException:
                    continue

                if h3.text.endswith('conexões em comum'):
                    href = a.get_attribute('href')

                    browser.get(href)
                    sleep(SLEEP_TIME)

                    alter_usernames = get_usernames(browser, '.search-result__result-link.ember-view')

                    break

        saver.save(username, name, alter_usernames)


if __name__ == '__main__':
    main()
