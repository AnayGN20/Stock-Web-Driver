from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time


from password import USERNAME, PASSWORD, SLEEP_TIME, GROWW_PIN, NO_OF_WATCHLISTS
URL = "https://groww.in/"

for i in range(0,100):
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get(URL)
        break;
    
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
        time.sleep(1)
else:
    print("Failed to connect after 10 attempts.")
    exit
time.sleep(SLEEP_TIME)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div/div/button').click()
time.sleep(SLEEP_TIME)
driver.find_element(By.TAG_NAME, 'input').send_keys(USERNAME)
time.sleep(SLEEP_TIME)
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(SLEEP_TIME)

driver.find_element(By.ID, 'login_password1').send_keys(PASSWORD)
time.sleep(SLEEP_TIME)
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(SLEEP_TIME)



OTP_Blanks = []
for i in range(0, 6):
    OTP_Blanks.append(driver.find_element(By.XPATH,f'//*[@id="otpinput88parent"]/div[{i+1}]/input'))

print(len(OTP_Blanks))
OTP = 0
driver.minimize_window()
while True:
    OTP = input("Enter OTP : ")
    test = input("Are you sure?\n (Enter 'No' if OTP invalid)")
    if(test.lower() == 'no'):
        continue;
    OTP = list(OTP)
    break
driver.maximize_window()

for i in range(len(OTP_Blanks)):
    OTP_Blanks[i].send_keys(int(OTP[i]))
    # print("Entered input OTP")
    time.sleep(SLEEP_TIME)


OTP_Blanks = []
for i in range(0, 4):
    OTP_Blanks.append(driver.find_element(By.XPATH,f'//*[@id="otpinput88parent"]/div[{i+1}]/input'))

# print(len(OTP_Blanks))
OTP = GROWW_PIN
OTP = list(OTP)
  


for i in range(len(OTP_Blanks)):
    OTP_Blanks[i].send_keys(int(OTP[i]))
    time.sleep(SLEEP_TIME)

driver.find_element(By.XPATH, '//*[@id="dashMainDiv"]/div/div/div[2]/div/div[2]/div/div[1]/a').click()
time.sleep(SLEEP_TIME)
driver.find_element(By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div').click()
# input("---PRESS ENTER TO CONTINUE---")

watchlists = []
stocks = []
for i in range(0, NO_OF_WATCHLISTS):
    watchlists.append(driver.find_element(By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[{i+1}]/div/div'))
    watchlists[i].click()
    watchlists[i] = watchlists[i].text
    print(f"{watchlists[i]}")
    stock_temp = []
    time.sleep(SLEEP_TIME+10)
    for j in range(100):
        try:
            # input("Press Enter")
            temp = driver.find_element(By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[{j+1}]/div[2]/a/div')

            stock_temp.append(temp.text)
            print(stock_temp)
            time.sleep(SLEEP_TIME)
            # print(stocks[i][j].text)
        except Exception as e:
            print("Index out of bounds : ", e)
            break;
        
    else:
        print("Debugging Required (infinte Loop)")
    # print("WATCHLIST : ",watchlists)
    stocks.append(stock_temp)
    print("\n\nSTOCKS\n",stocks)




print(stocks)

# with open(file="Stocks.txt", mode='w') as f:
#     for i in range(len(stocks)):
        
#         f.write(f"\n---{watchlists[i]}---\n")
#         for j in range(len(stocks[i])):
#             f.write(f"{stocks[i][j]}\n")

#     f.close()

from Write_Excel import Excel
excel_filename = "Stocks.xlsx"
excel_sheetname = "Anay"
excel = Excel(stocks=stocks, watchlist=watchlists, filename=excel_filename, sheetname=excel_sheetname)

excel.write()




input("Enter EXIt")

