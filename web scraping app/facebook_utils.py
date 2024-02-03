from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login_to_facebook(browser, username, password):
    try:
        browser.get('https://mbasic.facebook.com/')
        WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        username_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_btn = browser.find_element_by_xpath('//*[@id="login_form"]/ul/li[3]/input')
        login_btn.click()
        login_btn = browser.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div/div[3]/a')
        login_btn.click()
    except Exception as e:
        print(f"Erreur lors de la connexion à Facebook: {e}")

def search_hashtag(browser, hashtag):
    try:
        search = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='query']")))
        search.clear()
        search.send_keys(hashtag)
        login_btn = browser.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[3]/input')
        login_btn.click()
    except Exception as e:
        print(f"Erreur lors de la recherche du hashtag: {e}")
