"""
Requirements:
-Automated Bot for all easy applications (tailored to you)
-Goes through entire, if immediate application send. Otherwise exist and change search parameters, and repeat
-Catches necessary exceptions
-Well structured code - simplify + compartmentalize as best as possible (ask senior dev)
-Run continuously (reap benefits from it) every 24h/hour
-Applies to all types of software engineering jobs you'd like
(Quant Intern, Intern, Junior Developer, Engineer I, Associate Developer, Data Intern)
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Application Credentials
ACCOUNT_EMAIL = Enter your Username
ACCOUNT_PASSWORD = Enter your Password
city = Enter your city
phone_number = Enter your phone number

summary = Enter a summary of your employment history, skills, and education.

soup = BeautifulSoup()

# chrome_driver_path = r"C:\Users\Owner\source\repos\chromedriver.exe"
chrome_driver_path = r"C:\Users\User\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
website = "https://www.linkedin.com/jobs/search?keywords=Intern&location=Canada&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
driver.get(website)

def apply_to_jobs():
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()

    #Wait for the next page to load.
    time.sleep(5)

    username = driver.find_element(By.ID, "username")
    username.send_keys(ACCOUNT_EMAIL)
    password = driver.find_element(By.ID, "password")
    password.send_keys(ACCOUNT_PASSWORD)

    sign_in_final_button = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    sign_in_final_button.click()

    #get easy apply listings
    time.sleep(8)
    easy_apply_listings = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
    easy_apply_listings.click()

    #wait for the job listings to load after easy apply filter has been set
    time.sleep(5)

    #get listings < 24h
    date_posted = driver.find_element(By.XPATH,
    '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button')
    date_posted.click()

    """If element is hidden behind other HTML (Message: element click intercepted:)"""
    wait = WebDriverWait(driver, 40)

    """arguments[0].click(); will click the element - click() not required"""
    twenty_four_hours = driver.execute_script("arguments[0].click();", wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='timePostedRange-r86400']"))))

    show_24h_results = driver.find_element(By.XPATH,
    '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')
    show_24h_results.click()

    #narrow down listings to full-time opportunities
    all_filters = driver.find_element(By.XPATH,
    '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button')
    all_filters.click()

    time.sleep(1)
    full_time = driver.execute_script("arguments[0].click();", wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='advanced-filter-jobType-F']"))))

    internship = driver.execute_script("arguments[0].click();", wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='advanced-filter-jobType-I']"))))

    time.sleep(3)

    #narrow filters to specify based on location
    remote = driver.execute_script("arguments[0].click();", wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[2]/input'))))
    on_site = driver.execute_script("arguments[0].click();", wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[1]/input'))))
    hybrid = driver.execute_script("arguments[0].click();", wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[3]/input'))))

    location = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-location-id-ember26"]')
    finalize_query = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/button[2]')
    finalize_query.click()

    time.sleep(3)

    def exit_application():
        time.sleep(2)
        discard = driver.execute_script("arguments[0].click();", wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Dismiss']"))))
        print("C")

        time.sleep(2)
        final_exit = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
        print("D")
        final_exit.click()

    time.sleep(2)
    all_applications = driver.find_elements(By.CLASS_NAME ,'job-card-container')
    print(len(all_applications))
    for i in range(len(all_applications)):  # get proper length of all apps
        # try:
        time.sleep(1)
        all_applications[i].click()
        print("a")
        time.sleep(1)

        easy_apply = driver.find_element(By. CLASS_NAME, 'jobs-apply-button')
        easy_apply.click()
        print("A2")

        try:
            time.sleep(1)
            submit_application = driver.execute_script("arguments[0].click();", wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Submit application']"))))
            print("b")
        except:
            exit_application()

    # apply = driver.find_element(By.XPATH,
    # '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button')
    # apply.click()


    # submit_application.click()



    """Paramters to fix - If Location == Canada/Calgary + others. Listings over a certain amount. """

    #get listings that pay >= 80k
    desired_salary = driver.execute_script("arguments[0].click();", wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[15]/fieldset/div/ul/li[3]/input'))))

    response = requests.get(website)
    alocation_bar = response.text
    print(alocation_bar)
    soup_website = BeautifulSoup(alocation_bar, "html.parser")
    location = soup.find("address", attrs={'data-job-search-box-location-input-trigger': 'Canada'})
    print(location)

    location = driver.find_element(By.XPATH, '//*[@id="location-typeahead-instance-ember26"]/div/input[2]').get_attribute('Canada')
    # (By.NAME, 'data-job-search-box-location-input-trigger').get_attribute('Canada')
    print(location)
    if location.text == 'Canada':
        print("A")

apply_to_jobs()