from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to Chrome User Data (Session) Folder in AppData
chrome_user_data_path = r"C:\Users\besta\AppData\Local\Google\Chrome\User Data"

# Initialize WebDriver and set options
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_user_data_path}")  # Points to existing WhatsApp Web session
options.add_argument("profile-directory=Default")  # Use the Default profile where WhatsApp is logged in

# Initialize WebDriver with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def check_whatsapp_number(phone_number):
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
    
    # Open WhatsApp Web with your session
    driver.get(whatsapp_url)
    
    try:
        # Wait until the error message appears (indicating the number is invalid)
        error_message = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Phone number shared via url is invalid')]"))
        )
        
        print(f"❌ {phone_number} is NOT registered on WhatsApp.")
        
        # Wait for the "OK" button to appear and click it to close the modal
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'OK')]"))
        )
        ok_button.click()
        time.sleep(2)  # Wait for the modal to close
        
        # Write invalid numbers to a file
        with open("canadian_invalid_numbers.txt", "a") as invalid_file:
            invalid_file.write(phone_number + "\n")
        
    except:
        print(f"✅ {phone_number} is registered on WhatsApp.")
        
        # Write valid numbers to a file
        with open("canadian_valid_numbers.txt", "a") as valid_file:
            valid_file.write(phone_number + "\n")

# Read phone numbers from the file
with open("phone_numbers.txt", "r") as file:
    phone_numbers = [line.strip() for line in file.readlines()]

# Check each number from the list
for number in phone_numbers:
    check_whatsapp_number(number)

# Close the browser after checking
driver.quit()
