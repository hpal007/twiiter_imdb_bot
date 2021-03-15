from selenium import webdriver
from time import sleep

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
TWITTER_EMAIL = "YOUR TWITTER TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER TWITTER_PASSWORD"


class Top5ShowTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.top_5_show = {}
        self.string_object = ""

    def top_imdb_shows(self):
        self.driver.get("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv")
        sleep(2)
        titles = self.driver.find_elements_by_css_selector('.titleColumn a')
        titles_list = [show.text for show in titles]
        ratings = self.driver.find_elements_by_css_selector('.imdbRating strong')
        ratings_list = [point.text for point in ratings]
        self.top_5_show = {k: v for k, v in zip(titles_list[:5], ratings_list[:5])}
        list_object = [f'{show} \t|\t {rating}' for show, rating in self.top_5_show.items()]
        self.string_object = '\n'.join(list_object)
        print(self.string_object)

    def twitter_bot(self):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        sleep(0.1)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_button.click()
        sleep(2)
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet.send_keys(f"Top 5 shows of the month:\n\n{self.string_object}")
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
        tweet_button.click()


bot = Top5ShowTwitterBot(CHROME_DRIVER_PATH)
bot.top_imdb_shows()
bot.twitter_bot()
driver.quit()
