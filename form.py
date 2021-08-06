from selenium import webdriver

class Bot:
    """This class interacts with the google forms and fills the various questions"""
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/USER/development/chromedriver.exe")


    def get_form(self):
        self.driver.get("https://forms.gle/xhGbX82r3b1LodxM8")

    def fill_q1(self):
        q1 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        return q1

    def fill_q2(self):
        q2 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        return q2

    def fill_q3(self):
        q3 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        return q3

    def submit(self):
        submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
        return submit_btn

    def find_by_link(self):
        submit_another = self.driver.find_element_by_link_text("Submit another response")
        return submit_another


