import random
import time
from selenium import webdriver
import pandas as pd
from pandas import DataFrame

driver = webdriver.Firefox()

# do a depth first search for each site
base = 'https://www.autoevolution.com/'
driver.get("https://www.autoevolution.com/cars/")

def get_brands() -> list[str]:
    """ method for obtaining all car brands """
    brands = driver.find_elements(by="xpath",value="//div[@class='col2width fl bcol-white carman']//span")
    brandList = [brand.text for brand in brands]
    return brandList

def get_generations() -> list[list[str]]:
    # O(n^2+n+)
    brandList = get_brands()
    base: str = "https://www.autoevolution.com/"
    generationList = []
    for i in range(len(brandList)):
        brand = brandList[i]
        if brand.lower()=="delorean":
            brand = "dmc"
        if brand.lower()=="marussia":
            brand = "marussia-motors"
        if brand.lower()=="ssangyong":
            brand = "ssang-yong"
        if brand.lower()=="tesla":
            brand = "tesla-motors"
        
        brand_url = base+brand.lower().replace(" ","-")
        print(brand_url)
        
        driver.get(brand_url)
        generations = driver.find_elements(by="xpath",value="//div[@class='col2width bcol-white fl']//h4")
        generationList.append([generation.text for generation in generations])
        time.sleep(random.randrange(0,10)/10)
    return generationList
cache = [get_brands(),get_generations()]

def get_models() -> list[list[list[str]]]:
    # O(n^2+2n)
    modelList = []
    generationList = get_generations()
    for i in range(len(generationList)):
        for j in range(len(generationList[i])):
            generation_url = base+generationList[j]
            driver.get(generation_url)
            time.sleep(random.randrange(0,10)/10)
            models = driver.find_elements(by="xpath",value="//div[@class='container carmodel clearfix']//div[@class='years']//a")
            for model in models:
                modelList.append(model.text)
    return modelList

def load_sites():
    """ load all the cars and add them to a CSV file. the result is returned as a pandas dataframe """
    pass


try:
    print(get_models())
finally:
    driver.quit()