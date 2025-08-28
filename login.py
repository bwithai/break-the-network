import json
import os
import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your Chrome profile
chrome_profile_path = os.path.expanduser('~/.config/google-chrome/Zak_FSE')

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")
options.add_argument("start-maximized")

# Initialize the WebDriver with the existing profile
driver = webdriver.Chrome(options=options)
# Create a wait object
wait = WebDriverWait(driver, 20)


def _validate_login():
    url = f"..."
    driver.get(url)
    time.sleep(5)
    return driver.current_url


def _save_json(data, filename="output.json"):
    """Save dictionary data into a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def _type_like_human(type: str, text_area, enter=False):
    for char in type:
        text_area.send_keys(char)
        time.sleep(0.1)  # Adjust the delay as needed
    if enter:
        time.sleep(0.3)
        # Press Enter to submit
        text_area.send_keys(Keys.RETURN)


def _login_handle_by_ui():
    url = f"..."
    driver.get(url)

    # Wait until email field is visible and fill it
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="..."]')))
    email_input.clear()
    _type_like_human("...", email_input)
    # email_input.send_keys("")

    # Wait until password field is visible and fill it
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "...")))
    password_input.clear()
    _type_like_human("...", password_input, True)
    # password_input.send_keys("your_password")


def get_local_storage():
    """Return all items from browser's localStorage as a dict."""
    storage = driver.execute_script(
        "let items = {}; "
        "for (let i = 0; i < localStorage.length; i++) { "
        "   let key = localStorage.key(i); "
        "   items[key] = localStorage.getItem(key); "
        "} "
        "return items;"
    )
    return storage


if __name__ == "__main__":
    # _login_handle_by_ui()
    # time.sleep(0.3)

    validate_url = _validate_login()
    print("current url: ", validate_url)

    print("storage after login -------------------")
    data = get_local_storage()
    data['current_url'] = validate_url
    _save_json(data)

    input("Press Enter to close the browser...")
    # Close the browser
    driver.quit()

# jalalayn, Jalalhaddad