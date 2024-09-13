# -- Import the necessary libraries --
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

# -- Set the path to the chromedriver.exe file --
service = Service('chromedriver.exe')

# -- Function to get the driver --
def get_driver(link: str):
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # to prevent the infobars popups to interfere with the script
    options.add_argument("start-maximized")  # some webpages may change the content depending on the size of the window so we access the maximized version of the browser
    options.add_argument("disable-dev-shm-usage")  # to avoid issues while interacting with the browser on a linux computer and replit is a linux computer
    options.add_argument("no-sandbox")  # to disable sandbox in the browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    return driver

# -- Function to increase the GitHub views --
def increase_github_views(link: str, refresh_count: int):
    # -- Get the driver --
    try:
        driver = get_driver(link)
    except:
        print("!!! Unable to get the driver")

    count: int = 0 

    try:
        # -- Loop to refresh the page --
        while count < refresh_count or refresh_count == 0:
            try:
                # -- Wait for the page to load --
                wait(driver, 90).until(EC.visibility_of_element_located((By.XPATH, "//body")))
            except:
                print("!!! Unable to find the element")
                return

            driver.refresh()
            time.sleep(2)  # Adding a small delay between refreshes to avoid being flagged as a bot

            # -- Increase the refresh count --
            count += 1

            if refresh_count > 0 and count >= refresh_count:
                break
    except:
        print("!!! An error occurred while refreshing the page")

    finally:
        # -- Close the driver --
        driver.quit()

    print(f"Driver completed {count} refreshes for {link}")


if __name__=="__main__":
    # -- Set the link to the GitHub repository --
    link = "https://github.com/SubhojitGuin"

    # -- Set the number of times to refresh the page --
    refresh_count = 0
    
    try:
        increase_github_views(link, refresh_count)
    except:
        print("!!! An error occurred while increasing the GitHub views")