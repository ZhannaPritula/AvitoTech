import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        super().__init__()
        self.pagination_option_array = None
        self.pagination_number_array = None
        self.filter_by_sort = None
        self.filter_by_category = None
        self.filter_by_platform = None
        self.games_array = None
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
        self.assert_page_displayed()

    def assert_page_displayed(self):
        self.assert_title_displayed()
        self.assert_number_pagination_displayed()
        self.assert_option_pagination_displayed()
        self.assert_elements_games_displayed()
        self.assert_filter_displayed()

    def change_filter_by_platform(self, title_filter):
        self.change_filter(self.filter_by_platform, title_filter)

    def change_filter_by_category(self, title_filter):
        self.change_filter(self.filter_by_category, title_filter)

    def change_filter_by_sort(self, title_filter):
        self.change_filter(self.filter_by_sort, title_filter)

    def assert_title_displayed(self):
        main_title = self.driver.find_element(By.TAG_NAME, "h1")
        assert main_title.text == "Main Page"

    def assert_filter_displayed(self):
        filter_array = self.driver.find_elements(By.XPATH, "//span[text()='not chosen']")
        self.filter_by_platform = filter_array[0]
        self.filter_by_category = filter_array[1]
        self.filter_by_sort = filter_array[2]
        assert len(filter_array) > 0

    def assert_elements_games_displayed(self):
        self.games_array = self.driver.find_elements(By.CLASS_NAME, "ant-list-item")
        assert len(self.games_array) > 0

    def assert_number_pagination_displayed(self):
        self.pagination_number_array = self.driver.find_elements(By.CLASS_NAME, "ant-pagination-item")
        print(self.pagination_number_array[1].text)
        assert len(self.pagination_number_array) > 0

    def assert_option_pagination_displayed(self):
        self.pagination_option_array = self.driver.find_element(By.CLASS_NAME, "ant-pagination-options")
        assert self.pagination_option_array.is_displayed()

    def change_filter(self, filter_item, filter_search):
        filter_item.click()
        self.driver.find_element(By.XPATH, "//div[text()='" + str(filter_search) + "']").click()
        self.assert_elements_games_displayed()

    def change_screen(self, number):
        self.driver.find_element(By.XPATH, "//a[text()='" + str(number) + "']").click()
        time.sleep(3)

    def open_game_from_search(self, number):
        game_name = self.driver.find_element(By.XPATH,
                                             "//*[@id='root']/div/div[5]/div[2]/div/ul/li[" + str(
                                                 number + 1) + "]/div/div/div/div/div[1]/h1").text
        self.games_array[number].click()
        return game_name
