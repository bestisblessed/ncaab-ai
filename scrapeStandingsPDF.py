from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.ncaa.com/standings/basketball-men/d1")

# Wait for the necessary elements to load
driver.implicitly_wait(5)

# Use the built-in Selenium method to execute a CDP command
# The command 'Page.printToPDF' is used here to generate the PDF from the current page
pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})

# Convert the base64 encoded data to bytes
pdf_content = base64.b64decode(pdf['data'])

# Ensure the directory for the PDF exists
pdf_dir = "./data"
os.makedirs(pdf_dir, exist_ok=True)

# Write the PDF data to a file
pdf_file_path = os.path.join(pdf_dir, "ncaa_basketball_standings.pdf")
with open(pdf_file_path, "wb") as file:
    file.write(pdf_content)

driver.quit()

