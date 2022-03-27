import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class PassetBot:
    def __init__(self, start_url, first_name, last_name, email, phone, months_to_book, latest_date):
        self.start_url = start_url
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.months_to_book = months_to_book
        self.latest_acceptable_date = latest_acceptable_date
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)

    def _reset_session(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(2)

    def _wait(self, seconds=2):
        time.sleep(seconds)

    def start_session(self):
        self._reset_session()
        self.driver.get(self.start_url)
        self._wait()

        # click on "Boka tid"
        self.driver.find_element_by_name('StartNextButton').click()
        self._wait()

        # click accept conditions
        self.driver.find_element_by_xpath('//*[@id="AcceptInformationStorage"]').click()

        # click "nästa steg"
        self.driver.find_element_by_xpath('//*[@id="Main"]/form/div[2]/input').click()
        self._wait()
        # click "jag bor i sverige"
        self.driver.find_element_by_xpath('//*[@id="ServiceCategoryCustomers_0__ServiceCategoryId"]').click()

        # click "nästa steg"
        self._next_step()
        self._wait()

        # click "första lediga tid"
        self.driver.find_element_by_xpath('//*[@id="Main"]/form[1]/div/div[6]/div/input[2]').click()
        self._wait()

        # check date
        available_date = self.driver.find_element_by_xpath('//*[@id="dateText"]').text.lower()
        acceptable_months = ['apr']
        last_date = 15

        # get both month and date
        date, month = available_date.split(' ')
        # print(month_date)

        if any(m for m in acceptable_months if m in month) and date < last_date:
            print('date ok')
            # find timeslot
            self.driver.find_element_by_css_selector("div[class='pointer timecell text-center ']").click()
            # click "nästa steg"
            self._next_step()
            self._book_time()
        else:
            print('no acceptable dates, retrying in 5 mins')
            time.sleep(5 * 60)
            self.start_session()

    def _check_time(self):
        if any(m for m in acceptable_months if m in month) and date < last_date:
            return True
        else:
            return False

    def _next_step(self):
        # click "nästa steg"
        self.driver.find_element_by_name("Next").click()

    def _book_time(self):
        # click "första lediga tid"
        # find timeslot
        self.driver.find_element_by_css_selector("div[class='pointer timecell text-center ']").click()
        # click "nästa steg"
        self.driver.find_element_by_name("Next").click()
