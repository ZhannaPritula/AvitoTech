from pages.homepage import HomePage


def test_change_carousel(driver):
    homepage = HomePage(driver)
    homepage.open_main_page()
    homepage.change_screen(3)
