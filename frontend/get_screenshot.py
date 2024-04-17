import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

# 123.0.6312.122
# /usr/bin/google-chrome



def get_my_screenshot(url):
    email_name = url
    f_email = url.replace("https://","")

    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox") 

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
    chrome_service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    # getting the url
    
    driver.get(email_name)

    # determine the size of screen
    driver.set_window_size(1920, 1080)

    # getting the location to save image
    static_dir = os.path.join(settings.BASE_DIR, "screenshots", "frontend")
    os.makedirs(static_dir, exist_ok=True)
    screenshot_path = os.path.join(static_dir, f'{f_email}.png')
    time.sleep(2)
    try:
        # taking the screenshot
        driver.save_screenshot(screenshot_path)
    except:
        pass
    finally:
        driver.quit()

    return screenshot_path