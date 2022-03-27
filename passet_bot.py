import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class PassetBot:
    def __init__(self, start_url, first_name, last_name, email, phone, latest_acceptable_date):
        self.start_url = start_url
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.latest_acceptable_date = latest_acceptable_date
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)

    def _reset_session(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(2)

    def start_session(self):
        self._reset_session()
        self.driver.get(self.start_url)
        time.sleep(2)
        # click on "Boka tid"
        self.driver.find_element_by_name('StartNextButton').click()
        time.sleep(2)
        # click accept conditions
        self.driver.find_element_by_xpath('//*[@id="AcceptInformationStorage"]').click()
        # click "nästa steg"
        self.driver.find_element_by_xpath('//*[@id="Main"]/form/div[2]/input').click()
        time.sleep(2)
        # click "jag bor i sverige"
        self.driver.find_element_by_xpath('//*[@id="ServiceCategoryCustomers_0__ServiceCategoryId"]').click()
        # click "nästa steg"
        self.driver.find_element_by_name("Next").click()
        time.sleep(2)
        # click "första lediga tid"
        self.driver.find_element_by_xpath('//*[@id="Main"]/form[1]/div/div[6]/div/input[2]').click()
        time.sleep(5)

        available_date = self.driver.find_element_by_xpath('//*[@id="dateText"]').text.lower()
        acceptable_months = ['apr']
        last_date = 15
        # get both month and date
        date, month = available_date.split(' ')
        # print(month_date)
        # check date

        if any(m for m in acceptable_months if m in month) and date < last_date:
            print('date ok')
            # find timeslot
            self.driver.find_element_by_css_selector("div[class='pointer timecell text-center ']").click()
            # click "nästa steg"
            self.driver.find_element_by_name("Next").click()
            self._book_time()
        else:
            print('no acceptable dates, retrying in 5 mins')
            time.sleep(5 * 60)
            self.start_session()

    def _book_time(self):
