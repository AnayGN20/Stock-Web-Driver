from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

from password import PHONE_NUMBER, NO_OF_WATCHLISTS,  PASSWORD, SLEEP_TIME
import random

get_SLEEP_TIME = lambda :random.randrange(SLEEP_TIME, 20)
URL = "https://www.indstocks.com"

for i in range(0,100):
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get(URL)
        break;
    
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
        time.sleep(2)
else:
    print("Failed to connect after 10 attempts.")
    exit
time.sleep(get_SLEEP_TIME())
driver.find_element(By.XPATH, '//*[@id="site-header"]/div/div[2]/div/button[1]').click() #Login Button

time.sleep(get_SLEEP_TIME())
driver.find_element(By.NAME, 'mobile').send_keys(PHONE_NUMBER)
time.sleep(get_SLEEP_TIME())
driver.find_element(By.XPATH, '//*[@id="login_button_continue"]').click() #Sign up after number

time.sleep(get_SLEEP_TIME())


driver.minimize_window()
while True:
    OTP = int(input("\n\n\n\n----ENTER OTP : "))
    test = input("Are you sure?\n (Enter 'No' if OTP invalid)")
    if(test.lower() == 'no'):
        continue;
    break

driver.maximize_window()



driver.find_element(By.NAME, 'otp').send_keys(OTP)
time.sleep(get_SLEEP_TIME()+3)

driver.find_element(By.ID, 'login_button_verify_otp').click() #OTP Click button
time.sleep(get_SLEEP_TIME()+10)

driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div/div/ul/li[4]/a').click() #Watchlist button
time.sleep(get_SLEEP_TIME()+10)


watchlists = []
stocks = []

for i in range(1, NO_OF_WATCHLISTS+1):
    list_temp = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/button[{i}]')
    list_temp.click()
    watchlists.append(list_temp.text)
    stock_temp = []

    for j in range(1, 100):
        try:
            # input("Press Enter")
            temp_name = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/div[{j}]/div[1]/div/p[1]')

            stock_temp.append(temp_name.text)
            print(stock_temp)
            time.sleep(get_SLEEP_TIME())

        except Exception as e:
            print("Index out of bounds : ", e)
            break;

    else:
        print("Debugging Required (infinte Loop)")

    stocks.append(stock_temp)
    print("\n\nSTOCKS\n",stocks)


from Write_Excel import Excel
excel_filename = "Stocks.xlsx"
excel_sheetname = "Arham"
excel = Excel(stocks=stocks, watchlist=watchlists, filename=excel_filename, sheetname=excel_sheetname)

excel.write()





input("Enter EXIt")
