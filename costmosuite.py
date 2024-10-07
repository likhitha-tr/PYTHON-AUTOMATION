from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options) # type: ignore

# Open the ebay website
driver.get("https://www.mytheresa.com/us/en")

# Maximize the browser window
driver.maximize_window()

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,50)')  # scroll down by 50 pixels
    time.sleep(0.5)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  # wait for 1 second


# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div/a[1]/span"))
)

# Click the Sign In button
sign_in_button.click()  

email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/label/input"))
)
# Enter the email address
email_input.send_keys("rnithin@aol.com")

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/label/input"))
)
# Enter the password
password_input.send_keys("Nithin@2004")

# Wait for the Sign In button to be clickable again
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div"))
)

# Click the Sign In button
sign_in_button.click()

# Find and click the "EXPLORE NEW ARRIVALS" button
new_arrivals_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div/a/span")
new_arrivals_button.click()

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,50)')  # scroll down by 50 pixels
    time.sleep(0.5)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  # wait for 1 second

# Find and click the "EXPLORE JEWELRY" button
jewelry_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div/div[7]/div/a/span")
jewelry_button.click()

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,50)')  # scroll down by 50 pixels
    time.sleep(0.5)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  # wait for 1 second

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div/a[1]/span"))
)

# Click the Sign In button
sign_in_button.click() 

# Wait for the "Log Out" button to be clickable
wait = WebDriverWait(driver, 10)
log_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[6]/a")))

# Click the "Log Out" button
log_out_button.click()

# Close the browser
driver.quit()

