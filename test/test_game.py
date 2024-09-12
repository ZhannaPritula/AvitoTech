from pages.gamepage import GamePage
from pages.homepage import HomePage


def test_open_game_list(driver):
    homepage = HomePage(driver)
    gamepage = GamePage(driver)
    homepage.open_main_page()
    game_name = homepage.open_game_from_search(2)
    gamepage.assert_game_page_displayed(game_name)


def test_back_to_main(driver):
    homepage = HomePage(driver)
    gamepage = GamePage(driver)
    homepage.open_main_page()
    game_name = homepage.open_game_from_search(2)
    gamepage.assert_game_page_displayed(game_name)
    gamepage.back_to_main_click()
    homepage.assert_page_displayed()
