from selenium import webdriver # selenium
from selenium.webdriver.common.keys import Keys # selenium
import time # delay
import sys # loading bar
import threading # optimization
from threading import Thread # optimization

def extract_driver(extract_type):
    driver = webdriver.Chrome("/Users/alazsengul/Desktop/chromedriver")
    driver.get("https://www.instagram.com/")

    time.sleep(2)

    # STEP 1 - - - Navigate to login page.
    driver.find_element_by_class_name('izU2O').find_element_by_tag_name('a').click()

    time.sleep(2)

    # STEP 2 - - - Input account information.
    login_inputs = driver.find_element_by_class_name('EPjEi').find_elements_by_class_name('zyHYP')
    login_inputs[0].send_keys('alazsengul')
    login_inputs[1].send_keys('kanyewest')

    # STEP 3 - - - Login.
    driver.find_element_by_class_name('yZn4P').click()

    time.sleep(2)

    # STEP 4 - - - Navigate to profile page of account.
    driver.find_element_by_class_name('coreSpriteDesktopNavProfile').click()

    time.sleep(2)

    # STEP 5 - - - Store information about account.
    li_numbers = driver.find_elements_by_class_name('g47SY ')
    list_count = int(extract_number(li_numbers[extract_type].text))

    # STEP 6 - - - Scroll and store through either followers or following list.
    driver.find_element_by_class_name('k9GMp ').find_elements_by_class_name('Y8-fY ')[extract_type].click()

    time.sleep(2)

    action = webdriver.ActionChains(driver)
    action.send_keys(Keys.END)
    action.click()

    list_index = 0

    while (list_index < (list_count - 5)):
        action.perform()
        list_index = len(driver.find_elements_by_class_name('zsYNt'))

    list_spans = driver.find_elements_by_class_name('zsYNt')

    time.sleep(2)

    final_list = [span.text for span in list_spans]

    if (extract_type == 1):
        owers_list.append(final_list)
    elif (extract_type == 2):
        owing_list.append(final_list)

    driver.quit()

def extract_number(input_string):
    string_list = []
    for character in input_string:
        if character.isdigit():
            string_list.append(character)
    final_string = "".join(string_list)
    return(final_string)

def extract_haters(owers_list, owing_list):
    haters = []
    for following in owing_list:
        if following not in owers_list:
            haters.append(following)
    return(haters)

def owers():
    extract_driver(1)

def owing():
    extract_driver(2)

def main_thread():
    Thread(target = owers).start()
    Thread(target = owing).start()

if __name__ == '__main__':

    owers_list = []
    owing_list = []

    main_thread()

    extract_haters(owers_list[0], owing_list[0])
