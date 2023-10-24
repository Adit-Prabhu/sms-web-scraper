from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Initialize a Selenium webdriver
driver = webdriver.Chrome()  # You'll need to have the Chrome driver installed and in your PATH

# Create a list to store SMS messages
sms_messages = []

base_url = "https://online-sms.org/free-phone-number-15746215096?page="

for page_number in range(1, 605):  # Loop from page 1 to 604
    url = base_url + str(page_number)

    # Navigate to the webpage
    driver.get(url)

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

# Close the Selenium driver
driver.quit()

# Extract SMS messages and save them to a text file
with open("sms_messages.txt", "w") as file:
    for message in sms_messages:
        file.write(message + "\n")

print("All SMS messages have been scraped and saved to 'sms.txt'.")