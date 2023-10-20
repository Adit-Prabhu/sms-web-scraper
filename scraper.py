from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Define the URL of the webpage you want to scrape
url = "https://online-sms.org/free-phone-number-15746215096?page=1"  # Replace with the URL of your choice

# Initialize a Selenium webdriver
driver = webdriver.Chrome()  # You'll need to have the Chrome driver installed and in your PATH

# Navigate to the webpage
driver.get(url)

# Wait for the page to load (you might need to adjust the time depending on the website)
driver.implicitly_wait(10)

# Find the pagination elements
pagination_xpath = "/html/body/div[1]/div[4]/div/ul/li"

# Create a list to store SMS messages
sms_messages = []

page_number = 1

while True:
    # Find the table using its XPath
    table_xpath = "/html/body/div[1]/div[4]/div/table"
    table = driver.find_element(By.XPATH, table_xpath)

    # Get the HTML source of the table
    table_html = table.get_attribute("outerHTML")

    # Parse the table using BeautifulSoup
    soup = BeautifulSoup(table_html, "html.parser")

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 2:
            sms_message = cells[1].get_text(strip=True)
            sms_messages.append(sms_message)

    try:
        page_element = driver.find_element(By.XPATH, f"{pagination_xpath}[{page_number + 1}]")
        page_element.click()
        time.sleep(2)  # Adjust the time to allow the new content to load
        page_number += 1

    except Exception as e:
        print(f"Reached the last page: {e}")
        break

# Close the Selenium driver
driver.quit()

# Extract SMS messages and save them to a text file
with open("sms_messages_15746215096.txt", "w") as file:
    for message in sms_messages:
        file.write(message + "\n")

print("All SMS messages have been scraped and saved to 'sms_messages.txt'.")
