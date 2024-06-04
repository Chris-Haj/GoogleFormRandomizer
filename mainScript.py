import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver executable
chrome_driver_path = 'C:\\Users\\chris\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
chrome_options.add_argument("--lang=en")  # Set Chrome language to English

# Set up the web driver
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# Function to randomly fill checkbox questions
def fill_checkbox(question_element):
    options = question_element.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
    if options:
        number_of_options_to_select = random.randint(1, len(options))
        options_to_select = random.sample(options, number_of_options_to_select)
        for option in options_to_select:
            option.click()


# Function to randomly fill single choice questions
def fill_single_choice(question_element):
    options = question_element.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
    if options:
        option = random.choice(options)
        option.click()


# Function to fill out questions on the current page
def fill_out_current_page():
    questions = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')
    for question in questions:
        if question.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]'):
            fill_checkbox(question)
        elif question.find_elements(By.CSS_SELECTOR, 'div[role="radio"]'):
            fill_single_choice(question)


# Function to complete the form filling and submission
def complete_form():
    driver.get(form_url)
    time.sleep(2)  # wait for the page to load

    while True:
        fill_out_current_page()

        # Check if the "Submit" button is present on the current page
        try:
            submit_button = driver.find_element(By.XPATH, '//span[contains(text(),"שליחה")]')
            submit_button.click()
            print("Form submitted successfully.")
            break
        except:
            pass

        # If no "Submit" button, try to find and click the "Next" button
        try:
            next_button = driver.find_element(By.XPATH, '//span[contains(text(),"הבא")]')
            next_button.click()
            time.sleep(2)  # wait for the next page to load
        except Exception as e:
            print(f"Next button not found or an error occurred: {e}")
            break


# Function to handle unexpected alerts
def handle_alert():
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        pass


# Open the Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfkwBPCnOKP5Vyrh9pTmx8Sg_4Fk0els5l6jY1aDRiwq3VFig/viewform'

# Fill and submit the form 20 times
for i in range(3):
    print(f"Filling out form iteration {i + 1}")
    try:
        complete_form()
    except:
        handle_alert()

# Close the browser
driver.quit()
#
# submit_button = driver.find_element(By.XPATH, '//span[contains(text(),"שליחה")]')
#
# next_button = driver.find_element(By.XPATH, '//span[contains(text(),"הבא")]')
