import random
import time
from selenium import webdriver
import pandas as pd
from pandas import DataFrame

driver = webdriver.Firefox()

# do a depth first search for each site
base = 'https://www.autoevolution.com/cars/'
driver.get("https://www.autoevolution.com/cars/")

def get_brands():
    """ method for obtaining all car brands """
    brands = driver.find_elements(by="xpath",value="//div[@class='col2width fl bcol-white carman']//span")
    try:
        brandList = dict()
        for brand in brands:
            brandList[brand.text] = []
        
        for brand in brandList:
            brandURL: str = base.replace("cars",brand)
            try:
                driver.get(brandURL)
                time.sleep(random.randrange(0,1,0.1))
            except:
                print("We had a problem getting the URL")
        return brandList
    except MemoryError:
        return MemoryError.with_traceback()

def backtrack():
    
    pass

def load_sites():
    """ load all the cars and add them to a CSV file """
    pass
    
print(get_brands())
driver.quit()