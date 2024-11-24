from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your webdriver
webdriver_path = '/path/to/your/chromedriver'

# Initialize Chrome webdriver
driver = webdriver.Chrome(webdriver_path)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(15)  # Allow time for manual login

# Define the target contact or group
target = "Friend's Name"  # Change this to your recipient's name or group name

# Find the target in the search bar
search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
search_box.click()
search_box.send_keys(target)
time.sleep(2)

# Select the target chat
selected_target = driver.find_element_by_xpath(f'//span[@title="{target}"]')
selected_target.click()

# Send multiple messages
messages = [
    "Message 1",
    "Message 2",
    "Message 3"
]

for message in messages:
    input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)

# Close the browser
driver.quit()
