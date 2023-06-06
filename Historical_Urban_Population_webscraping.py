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
import numpy as np



import xlrd
import os

# Set the working directory to a specific path
os.chdir("D:/Edwin Kochulem/Masters_Program/Scripts_R_Python_store/Msc_Project_codes/Job_web_scraping/Excel_files/Oceania_region/")


driver=webdriver.Chrome(r"D:\Edwin Kochulem\Masters_Program\Scripts_R_Python_store\Msc_Project_codes\chromedriver_win32\chromedriver")

"""

links={'URLs':[]}
nl="Null"
driver.get('https://www.citypopulation.de/Oceania.html')

time.sleep(1)
incategory = driver.find_elements_by_xpath("html[1]/body[1]/div[4]/div[1]/ul[1]/li/a")

for i in range(len(incategory)):
    item = incategory[i]
    a=item.get_property("href")
    links['URLs'].append(a)

    print(a)


Country_links_df = pd.DataFrame.from_dict(links)

Country_links_df.to_csv("Oceania_pop_de_links.csv")


"""
in_country_df=pd.read_csv("Oceania_pop_de_links.csv")
urls2=in_country_df.loc[:,'URLs'].values.tolist()

for index, link in enumerate(urls2):

    print(index)

    link2=str(link)+str('cities/')

    count_name=link[33:-1]

    try:
        driver.get(url=link2)
        print(link)
        driver.implicitly_wait(2)



        try:
            Country_tag = driver.find_element_by_xpath("//p[@itemprop='description']").text
            print ("The country name is: {0}".format(Country_tag))
            print ("The country name is: {0}".format(count_name))

##        except:
##            Country_tag = driver.find_element_by_xpath("//span[@itemprop='name'])[3]").text
##            print ("The country name is: {0}".format(Country_tag))

        except NoSuchElementException:
            Country_tag = count_name
            print ("The country name is: {0}".format(Country_tag))
        except StaleElementReferenceException:
            Country_tag = count_name
            print ("The country name is: {0}".format(Country_tag))
        except TimeoutException:
            Country_tag = count_name
            print ("The country name is: {0}".format(Country_tag))

        except:
            Country_tag = count_name
            print ("The country name is: {0}".format(Country_tag))



        Table_head = driver.find_elements_by_xpath("//*[@id= 'ts']/thead/tr")

        City_tabl_dict = []

        # Iterate over the rows
        for row_head in Table_head:


            # Find the cells within each row
            heads = row_head.find_elements_by_tag_name('th')


            # Extract the text from each cell
            head_texts = [head.text for head in heads]

        City_table = driver.find_elements_by_xpath ("//*[@id= 'ts']/tbody/tr")
        # to get the row count len method
        print ("The count of cities are: {0}".format(len(City_table)))


        for row in City_table:

            # Find the cells within each row
            rdata = row.find_elements_by_tag_name('td')


            # Extract the text from each cell
            data_texts = [data.text for data in rdata]


            row_df=pd.DataFrame([data_texts],columns=[head_texts])

            #print(row_df)

            City_tabl_dict.append(row_df)


        data_df=pd.concat(City_tabl_dict)


        data_df.to_excel(Country_tag+'_Population_de.xlsx',engine='openpyxl', index=False)

        print(data_df)



    except NoSuchElementException:
        continue
    except StaleElementReferenceException:
        continue
    except TimeoutException:
        continue

    except:
        continue


#"""

driver.close()