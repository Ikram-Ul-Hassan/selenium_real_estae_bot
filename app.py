import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Strucrured code


class PropertyScraper():
    def __init__(self,url,timeout = 20):
        self.url = url
        self.data = []
        self.driver = self._initilize_driver()
        self.wait = WebDriverWait(self.driver, timeout = timeout)

    def _initilize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        
        # Some additional options are missing here, assuming they are similar to the original code

        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        )

        driver = webdriver.Chrome(options = chrome_options)
        driver.maximize_window()
        return driver

    def _wait_for_page_fully_load(self):
        title = self.driver.title
        try:
            self.wait.until(
                lambda d: d.execute_script("readyToState") == "complete"
            )
        except:
            print(f"The page \"{title}\" is NOT fully loaded within given duration")
        else:
            print(f"The page {title} is fully loaded within given duration")


    def access_website(self):
        self.driver.get(self.url)
        self._wait_for_page_fully_load()

    def search_properties(self,text):
        # sending keys in search bar

        try:
            search_bar = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="keyword2"]')))
        except:
            print("Search bar can't locate in given time duration")
        else:
            search_bar.send_keys("Chennai")

        # Selecting Valid Option fro Search Bar

        try:
            valid_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]')))
        except:
            print("Valid Option Can't Clicked from Search bar in given time duration")
        else:
            valid_option.click()


        # Click on search button

        try:
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchform_search_btn"]')))
        except:
            print("Search button not be clickable in given time duration")
        else:
            search_button.click()
            self._wait_for_page_fully_load()

    def adjust_budget_slider(self, offset):
        # adjust budget slider

        try:
            slider = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="budgetLeftFilter_max_node"]')))

        except:
            print("Slide Bar is Not be Clickable")

        else:
            actions = ActionChains(self.driver)
            actions.click_and_hold(slider).move_by_offset(offset,0).release().perform()

    def apply_filters(self):
        # filtering results to show genuine listings

        # 1. just locate and click on "verified", "move to ready" filters
        verified = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/span[2]')))
        verified.click()
        time.sleep(3)

        ready_to_move = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/span[2]')))
        ready_to_move.click()
        time.sleep(3)


        # 2. run a while loop, to clicking on right button for uncover all filters

        while True:
            try:
                right_filter_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class,'iconS_Common_24 icon_upArrow cc__rightArrow')]")))
            except:
                print("\"right_filter_button\" is not more present")
                break
            else:
                right_filter_button.click()
                time.sleep(1)

        # 3. just locate and click on "with_photos", "with_videos" filters
        with_photos= self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/span[2]')))
        with_photos.click()
        time.sleep(3)

        with_videos= self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[7]/span[2]')))
        with_videos.click()
        time.sleep(3)

    def _extract_data(self,row,by,value):
        try:
            return row.find_element(by,value).text
        except:
            return np.nan

    def scrape_webpage(self):
        # scraping data
        rows = self.driver.find_elements(By.CLASS_NAME, "tupleNew__contentWrap")
        for row in rows:
            # names of properties
            name = self._extract_data(row, By.CLASS_NAME, "tupleNew__headingNrera")
            pass
            # Some code is missing here, assuming it is to extract location and price


            try:
                elements = row.find_elements(By.CLASS_NAME, "tupleNew__area1Type")
            except:
                area, bhk = [np.nan, np.nan]
            else:
                area, bhk = [ele.text for ele in elements]


            property = {
                "name":name,
                "location": location,
                "price": price,
                "area" : area,
                "bhk" : bhk
            }
                # print(property)
            self.data.append(property)


    def navigate_pages_and_extract_data(self):
        page_count = 0
        while True:
            pass
            ### Some code is missing here, assuming it is to navigate through pages and extract data

    def clean_and_export_data_in_excel(self, filename):

        df = (
            pd.DataFrame(self.data)
            .drop_duplicates()


            # Some code is missing here, assuming it is to clean the data


        )
        df.to_excel(f"{filename}.xlsx",index = False)


    def run(self,text, offset= -100, filename= "properties"):
        try:
            self.access_website()
            self.search_properties(text)
            self.adjust_budget_slider(offset)
            self.apply_filters()
            self.navigate_pages_and_extract_data()
            self.clean_and_export_data_in_excel(filename)

        finally:
            time.sleep(3)
            self.driver.quit()




scraper = PropertyScraper(url = "https://www.99acres.com")
scraper.run("chennai", -73, "chennai_properties")