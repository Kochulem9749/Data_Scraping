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

Region="Oceania"

# Set the working directory to a specific path
os.chdir("D:/Edwin Kochulem/Masters_Program/Scripts_R_Python_store/Msc_Project_codes/Job_web_scraping/Excel_files/"+Region+"_region/")


driver=webdriver.Chrome(r"D:\Edwin Kochulem\Masters_Program\Scripts_R_Python_store\Msc_Project_codes\chromedriver_win32\chromedriver")

#"""

links={'URLs':[]}

driver.get("https://www.citypopulation.de/"+Region+".html")

time.sleep(1)
incategory = driver.find_elements_by_xpath("html[1]/body[1]/div[4]/div[1]/ul[1]/li/a")

for i in range(len(incategory)):
    item = incategory[i]
    a=item.get_property("href")
    links['URLs'].append(a)

    print(a)


Country_links_df = pd.DataFrame.from_dict(links)

Country_links_df.to_csv(Region+"_pop_de_links.csv")


#"""
in_country_df=pd.read_csv(Region+"_pop_de_links.csv")
urls2=in_country_df.loc[:,'URLs'].values.tolist()

City_list=[]

for index, link in enumerate(urls2):

    print(index)

    link2=str(link)+str('cities/')

    count_name=link[33:-1]

    try:
        driver.get(url=link2)
        print(link)
        #driver.implicitly_wait(1)



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

            head_texts1 = [item.strip('()') for item in head_texts]

            head_texts2 = [item for item in head_texts1 if item != '']

            print("The column heads are: {0} and the length is {1}".format(head_texts2,len(head_texts2)))

        City_table = driver.find_elements_by_xpath ("//*[@id= 'ts']/tbody/tr")
        # to get the row count len method
        print ("The count of cities are: {0}".format(len(City_table)))


        for row in City_table:

            # Find the cells within each row
            rdata = row.find_elements_by_tag_name('td')


            # Extract the text from each cell
            #data_texts = [data.text for data in rdata][1]

            data_texts_pop = [data.text for data in rdata]

            data_texts_pop2=pd.DataFrame([data_texts_pop])

            end_cut=len(head_texts2)+1

            Clean_df=data_texts_pop2.iloc[:,1:end_cut]
            Clean_df.columns=[head_texts2]

            city_name_df=Clean_df.iloc[:,0]

            Pop_df=Clean_df.iloc[:,-1:]

            country_list=[Country_tag] * 1
            country_list2=[count_name] * 1

            country_df=pd.DataFrame(country_list)
            country_df.columns=['Country_name']

            country_df2=pd.DataFrame(country_list2)
            country_df2.columns=['Country_name2']

            city_name_df.columns=['city_name']
            Pop_df.columns=['Population']


            # Concatenating column-wise
            Merged_df = pd.concat([country_df,country_df2,city_name_df,Pop_df], axis=1)

            City_tabl_dict.append(Merged_df)

        data_df=pd.concat(City_tabl_dict)
        City_list.append(data_df)
        print(data_df)

    except NoSuchElementException:
        print("proceed")
        continue
    except StaleElementReferenceException:
        print("proceed")
        continue
    except TimeoutException:
        print("proceed")
        continue
    except:
        print("proceed")
        continue


#"""

Whole_data_df=pd.concat(City_list)


print(Whole_data_df)


Whole_data_df.to_excel(Region+'_Country_city_names_Population_de.xlsx',engine='openpyxl', index=False)

driver.close()










"""

            country_list=[Country_tag] * 1
            country_list2=[count_name] * 1

            country_df=pd.DataFrame(country_list)
            country_df.columns=['Country_name']

            country_df2=pd.DataFrame(country_list2)
            country_df2.columns=['Country_name2']

            ##row_df=pd.DataFrame([data_texts],columns=[head_texts])

            row_df=pd.DataFrame([data_texts])

            end_cut=len(head_texts2)+1

            #row_df1=row_df.iloc[:,1:end_cut]
            #row_df1.columns=[head_texts2]


            # Concatenating column-wise
            #Merged_df = pd.concat([country_df,country_df2,row_df1], axis=1)

            #print(Merged_df.columns)


            City_tabl_dict.append(row_df)

        data_df=pd.concat(City_tabl_dict)
        City_list.append(data_df)
"""