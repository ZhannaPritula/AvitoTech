from pages.homepage import HomePage


def test_open_main(driver):
    homepage = HomePage(driver)
    homepage.open_main_page()
