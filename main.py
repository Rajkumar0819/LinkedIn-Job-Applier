#  importing needed modules and classes
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait

# basic details - email, password and mobile number
email_id = "01sampletesting@gmail.com"
pass_key = "RAJKUMAR@786"
mobile_number = "1234567890"

# initiating the driver
service = Service(executable_path="C:\PythonCode\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# getting the linked in url
driver.get("https://www.linkedin.com/login")


# logging in the website
def login():
    # giving the emamil and password in the input box
    driver.find_element(By.NAME, "session_key").send_keys(email_id)
    driver.find_element(By.NAME, "session_password").send_keys(pass_key)
    time.sleep(2)

    # clicking the sign-in button
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)


# # giving the job name and easy apply feature
def giving_job_name():
    # # Python developer as the job name
    time.sleep(4)
    job_description_key = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    job_description_key.send_keys("Python Developer")
    job_description_key.send_keys(Keys.ENTER)
    time.sleep(3)

    # # giving the easy apply filter button
    easy_apply_filter_btn = driver.find_element(By.LINK_TEXT, "Easy apply")
    easy_apply_filter_btn.click()
    time.sleep(4)

    # # experience tab
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div'
                                  '/ul/li[5]/div/span/button').click()
    time.sleep(1)

    # selecting internship input field
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/'
                                  'div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]/label').click()
    time.sleep(1)

    # selecting Entry level input field
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/'
                                  'ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label').click()
    time.sleep(2)

    # clicking the show result button
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/'
                                  'div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()
    time.sleep(3)


# discard if there is an additional or work experience page
def discard_job():
    # clicking the X button
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'artdeco-modal__header').click()
    x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
    x_button.click()
    time.sleep(2)

    # clicking the discard button
    discard_button = driver.find_element(By.CSS_SELECTOR,
                                         'div[data-test-modal-id="data-test-easy-apply-discard-confirmation"] button.artdeco-button--secondary')

    time.sleep(2)
    discard_button.click()
    time.sleep(2)


def mobile_number_giving():

    # finding the input tag for Mobile Number
    time.sleep(3)
    mobile_number_input_box = driver.find_element(By.CSS_SELECTOR, '[id*=phoneNumber-nationalNumber]')
    mobile_number_input_box.click()
    mobile_number_input_box.send_keys(Keys.CONTROL + "a")
    mobile_number_input_box.send_keys(Keys.DELETE)
    mobile_number_input_box.send_keys(mobile_number)
    time.sleep(3)

    general_click = driver.find_element(By.CLASS_NAME, 'jobs-easy-apply-content')
    general_click.click()
    time.sleep(1)
    next_btn = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
    next_btn.click()
    time.sleep(2)


# resume and cover letter page
def resume_and_cover_page():
    try:
        text_area = driver.find_element(By.TAG_NAME, 'textarea')
        text_area.send_keys(Keys.CONTROL + 'a')
        text_area.send_keys(Keys.DELETE)
        text_area.send_keys("this is a sample letter")

    except NoSuchElementException:
        pass

    driver.find_element(By.CLASS_NAME, 'jobs-easy-apply-content').click()
    next_btn = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
    next_btn.click()


# submit button final
def submit_button():
    time.sleep(2)
    area = driver.find_element(By.CLASS_NAME, 'jobs-easy-apply-content')
    area.click()
    area.send_keys(Keys.TAB)
    time.sleep(1)
    area.send_keys(Keys.END)
    driver.find_element(By.CLASS_NAME, 'artdeco-button--primary').click()
    time.sleep(3)


# main
def main():
    # logs in to the website
    global result
    login()

    # giving the job name as Python developer and clicks the easy apply and experience as Internship and Entry level
    giving_job_name()

    # this will list all the jobs in the job container
    loop_variable = True

    while loop_variable:

        # goes to the end of the list
        load_data = driver.find_element(By.CSS_SELECTOR, '.disabled')
        load_data.send_keys(Keys.TAB)
        load_data.send_keys(Keys.END)
        time.sleep(2)

        # stores all the names of the company's that are listed
        result = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results-list .disabled')
        loop_variable = False

    # iterating through each one of the job
    for each_job in result:
        time.sleep(1)
        each_job.click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]').click()
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        easy_apply_button = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/'
                                                  'div[2]/div[1]/div/div[1]/div/div[1]/div[1]/'
                                                  'div[3]/div/div/div/button')))
        easy_apply_button.click()
        time.sleep(2)

        # giving the mobile number in the form
        mobile_number_giving()

        # iterating through each page of the applying form
        loop_variable = True

        while loop_variable:
            # checking the Name of the section of the form
            section_of_page = driver.find_element(By.CLASS_NAME, 't-bold')

            # the review Application has a different font
            try:
                review_application = driver.find_element(By.CLASS_NAME, 't-18')
            except NoSuchElementException:
                review_application = section_of_page

            if review_application.text == "Review your application":
                loop_variable = False
                submit_button()

            elif review_application.text == 'Resume':
                time.sleep(1)
                resume_and_cover_page()

            elif review_application.text == "Home address":
                time.sleep(1)
                driver.find_element(By.CLASS_NAME, 'artdeco-button--primary').click()

            elif review_application.text == "Screening questions":
                time.sleep(1)
                driver.find_element(By.CLASS_NAME, 'artdeco-button--primary').click()

            elif review_application.text == "Additional Questions" or review_application.text == "Work experience":
                time.sleep(1)
                loop_variable = False
                discard_job()

            else:
                time.sleep(1)
                loop_variable = False
                discard_job()

        time.sleep(1)


main()
driver.quit()
