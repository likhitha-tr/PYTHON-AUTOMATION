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
driver.get("https://www.saucedemo.com/v1/")

# Maximize the browser window
driver.maximize_window()

# Find the username field and enter your username
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Find the password field and enter your password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

# Find the login button using XPath and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
)
login_button.click()

# Now you should be logged in to Swag Labs!

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
time.sleep(1)  # wait for 1 second

# Find all add to cart buttons on the page
add_to_cart_buttons = driver.find_elements(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button[contains(text(), 'ADD TO CART')]")

# Click on each add to cart button
for button in add_to_cart_buttons:
    button.click()

# Click on the cart button
cart_button = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart_button.click()

# Wait for the cart page to load
driver.implicitly_wait(5)

# Print the cart contents
cart_contents = driver.find_elements(By.XPATH, "//*[@id='cart_contents_container']/div/div")
for item in cart_contents:
    print(item.text)

# Close the browser
driver.quit()

# Wait for the cart page to load
driver.implicitly_wait(5)

# Print the cart contents
cart_contents = driver.find_elements(By.XPATH, "//*[@id='shopping_cart_container']/a/svg/path")
for item in cart_contents:
    print(item.text)

# Close the browser
driver.quit()

