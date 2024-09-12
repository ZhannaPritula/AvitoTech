from selenium.webdriver.common.by import By


class GamePage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def assert_game_page_displayed(self, game_name):
        self.assert_title_displayed()
        self.assert_name_game_displayed(game_name)
        self.back_to_main_displayed()

    def assert_title_displayed(self):
        main_title = self.driver.find_element(By.TAG_NAME, "h1")
        assert main_title.text == "Game Page"

    def assert_name_game_displayed(self, game_name):
        main_title = self.driver.find_element(By.TAG_NAME, "h2")
        assert main_title.text == game_name

    def back_to_main_displayed(self):
        self.driver.find_element(By.XPATH, "//span[text()='Back to Main']")

    def back_to_main_click(self):
        self.driver.find_element(By.XPATH, "//span[text()='Back to Main']").click()
