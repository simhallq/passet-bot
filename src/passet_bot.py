import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class PassetBot:
    def __init__(self, start_url, first_name, last_name, email, phone, latest_date, driver_path):
        self.start_url = start_url
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.latest_date = datetime.strptime(latest_date, '%Y-%m-%d')
        self.options = Options()
        self.driver = webdriver.Chrome(executable_path=driver_path, options=self.options)

    def start_session(self):
        self._reset_session()
        self.driver.get(self.start_url)
        self._wait()

        # click on "Boka ny tid"
        self.driver.find_element_by_name('StartNextButton').click()
        self._wait()

        # accept conditions and go to next
        self.driver.find_element_by_xpath('//*[@id="AcceptInformationStorage"]').click()
        self._next_step()
        self._wait()

        # click "jag bor i sverige" and go to next
        self.driver.find_element_by_xpath('//*[@id="ServiceCategoryCustomers_0__ServiceCategoryId"]').click()
        self._next_step()
        self._wait()

        # click "första lediga tid"
        self.driver.find_element_by_xpath('//*[@id="Main"]/form[1]/div/div[6]/div/input[2]').click()
        self._wait()

        # check date
        available_date = datetime.strptime(self.driver.find_element_by_id(
            'datepicker').get_property('value'), '%Y-%m-%d')
        if available_date < self.latest_date:
            print(f'slot available on {available_date}, booking...')
            self._book_time()
        else:
            print('no acceptable dates, retrying in 5 mins')
            time.sleep(5 * 60)
            self.start_session()

    def _next_step(self):
        """
        Click next button"""
        self.driver.find_element_by_name("Next").click()

    def _book_time(self):
        # find timeslot
        self.driver.find_element_by_css_selector("div[class='pointer timecell text-center ']").click()
        self._next_step()

    def _reset_session(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self._wait()

    def _wait(self, seconds=2):
        time.sleep(seconds)
