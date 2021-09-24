##Author Kochulem (Rik Rik)
##Use Ruto xpath finder to locate elements in a webpage

import time
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

driver = webdriver.Firefox()

details={"country":[],"Total_population":[],"Population_Extreme_Poverty":[],"Rural_Population":[],"Urban_population":[],"Males":[],"Females":[],"Year":[]}
options1=range(1)
options2=range(1,85,1)
nl="Null"
driver.get('https://worldpoverty.io/map')
for i in options1:
    try:
        driver.implicitly_wait(15)
        d=driver.find_element_by_xpath("//div[@class='react-select__single-value css-1uccc91-singleValue']").click()
        xpath = "react-select-2-option-{}".format(i)
        driver.find_element_by_id(xpath).click()
        time.sleep(5)
        Slider_location = driver.find_element_by_xpath("//span[text()='2021']/following-sibling::button")

        # Instantiate ActionChains
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop_by_offset(Slider_location, +485.00, 0).perform()
        time.sleep(30)
    except NoSuchElementException:
        continue

    for x in options2:
        try:
            driver.implicitly_wait(15)
            d=driver.find_element_by_xpath("//div[@class='react-select__single-value css-1uccc91-singleValue']").click()
            xpath = "react-select-2-option-{}".format(x)
            driver.find_element_by_id(xpath).click()
            time.sleep(10)
            count=driver.find_element_by_xpath("//h2[@class='serif country-card-content-fundamentals-title']").text
            details["country"].append(count)
        except NoSuchElementException:
            details["country"].append(nl)
        except StaleElementReferenceException:
            details["country"].append(nl)
        except TimeoutException:
            continue
        try:
            pop=driver.find_element_by_xpath("//h5[@class='align-right bold']").text
            details["Total_population"].append(pop)
        except NoSuchElementException:
            details["Total_population"].append(nl)
        except StaleElementReferenceException:
            details["Total_population"].append(nl)
        except TimeoutException:
            continue
        try:
            Extr_poverty=driver.find_element_by_xpath("//h5[contains(@class,'align-right red')]").text
            details["Population_Extreme_Poverty"].append(Extr_poverty)
        except NoSuchElementException:
            details["Population_Extreme_Poverty"].append(nl)

        except StaleElementReferenceException:
            details["Population_Extreme_Poverty"].append(nl)
        except TimeoutException:
            continue

        try:
            Rural_pop=driver.find_element_by_xpath("(//table[@class='country-card-all-table']//td)[2]").text
            details["Rural_Population"].append(Rural_pop)
        except NoSuchElementException:
            details["Rural_Population"].append(nl)
        except StaleElementReferenceException:
            details["Rural_Population"].append(nl)
        except TimeoutException:
            continue
        try:
            Urban_pop=driver.find_element_by_xpath("//table[@class='country-card-all-table']/tbody[1]/tr[2]/td[2]").text
            details["Urban_population"].append(Urban_pop)
        except NoSuchElementException:
            details["Urban_population"].append(nl)
        except StaleElementReferenceException:
            details["Urban_population"].append(nl)
        except TimeoutException:
            continue
        try:
            Males_pop=driver.find_element_by_xpath("//table[@class='country-card-all-table']/tbody[1]/tr[3]/td[2]").text
            details["Males"].append(Males_pop)
        except NoSuchElementException:
            details["Males"].append(nl)
        except StaleElementReferenceException:
            details["Males"].append(nl)
        except TimeoutException:
            continue
        try:
            Females_pop=driver.find_element_by_xpath("//table[@class='country-card-all-table']/tbody[1]/tr[4]/td[2]/h4[1]").text
            details["Females"].append(Females_pop)
        except NoSuchElementException:
            details["Females"].append(nl)
        except StaleElementReferenceException:
            details["Females"].append(nl)
        except TimeoutException:
            continue
        try:
            destination=driver.find_element_by_xpath("//li[@class='slider-scale-year']//span").text
##            destination=driver.find_element_by_class_name("slider-indicator-button").text
            details["Year"].append(destination)
        except NoSuchElementException:
            details["Year"].append(nl)
        except StaleElementReferenceException:
            details["Year"].append(nl)
        except TimeoutException:
            continue
        print(x)
##print(details)
Poverty_details = pd.DataFrame.from_dict(details)
Poverty_details .to_csv("E:/Masters_Program/Scripts_R_Python_store/Msc_Project_codes/Sourced_Data/World_Poverty/Poverty_2030_final.csv")
driver.close()