import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

log = "pelass@o2.pl"
pwd = "Dynamo666!"

class MediaExpertLog(unittest.TestCase):

    def setUp(self):
        # warunki wstępne
        self.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.mediaexpert.pl/')

    def test_log_mediaexpert(self):

        # logowanie użytkownika za pomocą poprawnych danych, zarejestowanych w systemie
        driver = self.driver

        Moje_konto_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#account_info_small > div > a.top_linksLogin.js-gtmEvent_click')))
        Moje_konto_btn.click()

        adres_email = driver.find_element_by_xpath('//*[@id="loginEmail"]')
        adres_email.send_keys(log)

        haslo = driver.find_element_by_xpath('//*[@id="loginPassword"]')
        haslo.send_keys(pwd)

        zaloguj_sie = driver.find_element_by_xpath('//*[@id="zaloguj_mnie"]')
        zaloguj_sie.click()

    tytul = driver.title
    print(tytul)
    assert 'Twoje zamówienia - Media Expert' == tytul
    print('Logowanie poprawne')

    def tearDown(self):
        self.driver.quit()

        sleep(3)
