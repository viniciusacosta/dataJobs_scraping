from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import pandas as pd
from unidecode import unidecode
import time


# Defining driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window()

# Create a new instance of the Chrome driver
url = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
driver.get(url)
wait = WebDriverWait(driver, 1)

# LinkedIn Login
username = driver.find_element(By.ID, "username")
username.send_keys("EMAIL HERE")
password = driver.find_element(By.ID, "password")
password.send_keys("PASSWORD HERE")
driver.find_element(By.CLASS_NAME, "login__form_action_container").click()
time.sleep(15)

# Defining Attributes
loc = "Brasil"
results = []
time.sleep(2)
i = 1
i = 1
p = 2
n = 1
vagas = ['cientista de dados','cientista de dados junior', 'analista de dados',  'analista de dados junior','engenheiro de dados', 'engenheiro de dados jr']

# Data Extraction
for vaga in vagas:
    time.sleep(2)
    i = 1
    p = 2
    n = 1

    print('scraping: %s' % vaga)
    driver.get(
        f"https://www.linkedin.com/jobs/search/?keywords={vaga}&location={loc}")
    time.sleep(3)

    while n <= 40:
        try:
            time.sleep(1)
            element = f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]'
            driver.find_element(By.XPATH, element + '/div[1]/a').click()
            
            title = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a').text
            title = unidecode(title)

            company = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[1]/div/div[1]/div[1]/div[2]/div[2]/a').text
            company = unidecode(company)

            location = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[3]/ul/li[1]').text
            location = unidecode(location)

            url = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a').get_attribute("href")
    
            description = driver.find_element(By.CLASS_NAME, f'jobs-description').text
            description = unidecode(description)

            #Criando um campo com a data de execução do Crawler
            crawled_at = datetime.now().strftime("%Y-%m-%d %H:%M")

            driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, element))
            driver.execute_script("window.scrollBy(0, -100);")

            results.append({"filter": vaga,
                            "crawled_at": crawled_at,
                            "title": title,
                            "url": url,  
                            "company": company,
                            "location": location,
                            "country": loc,
                            "description": str(description).replace(" ", "_").replace("\n", " ").replace(";", ".")})

            i += 1

        except:
            time.sleep(2)
            if p == 10:
                p = p - 3
            else:
                p = p

            try:
                driver.find_element(
                    By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[6]/ul/li[{p}]/button').click()
                n += 1
                p += 1
                i = 1

            except:
                try:
                    driver.find_element(
                        By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[5]/ul/li[{p}]/button').click()
                    n += 1
                    p += 1
                    i = 1

                except:
                    try:
                        
                        driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[5]/ul/li[{p}]/button').click()
                        n += 1
                        p += 1
                        i = 1
                    except:
                        print('ERROR')
                        break

# Saving DataFrame
df = pd.DataFrame(results)
df.to_csv('linkedin_scraping.csv', sep=";") 