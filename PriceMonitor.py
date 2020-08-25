from selenium import webdriver
from time import sleep
from pynotifier import Notification


class PriceFinder:
    def __init__(self,url):
        sitename = url.split(".")[1]
        if sitename == "amazon":
            self.driver = webdriver.Chrome("C:\\Users\\Krishnandu Biswas\\PycharmProjects\\try_scrap\\chromedriver.exe")
        else:
#             chrome_options = webdriver.ChromeOptions()
#             chrome_options.headless = True
            self.driver = webdriver.Chrome()
        self.driver.get(url)
        print("\t\t Welcome to " + sitename)
        self.driver.set_page_load_timeout(10)
        self.product_price = self.findPrice(sitename)

    def findPrice(self, sitename):
        price_containers = {"amazon": "//span[contains(@id,'priceblock_ourprice')]", "flipkart": "//div[contains(@class,"
            "'_1vC4OE _3qQ9m1')]", "myntra": "//span[contains(@class,'pdp-price')]"}
        try:
            price = self.driver.find_element_by_xpath(price_containers.get(sitename)).text
            return price
        finally:
            self.driver.close()

    def monitor(self):
        self.driver.execute_script("window.location.reload(true);")
        currentPrice = self.find_price(self, self.driver.current_url)
        if self.product_price != currentPrice:
            self.product_price = currentPrice
            print(currentPrice)
            # notifier = Notification()
            # notifier.URGENCY_NORMAL.send()


if __name__ == '__main__':
    url = input("Enter URL to track: ")
    pf = PriceFinder(url)
    price = pf.product_price
    print("Your product price is: " + price)
    
#     monitor = input("Want to monitor the price? ")
#     if monitor.__contains__("y"):
#         interval = input("Give an interval between price check: ")
#         notification = input("Want notifications on any update? ")
#         while monitor.__contains__("y"):
#             pf.monitor()
#             sleep(interval)

    pf.driver.quit()
    