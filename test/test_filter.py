from pages.homepage import HomePage


def test_filter_by_platform(driver):
    homepage = HomePage(driver)
    homepage.open_main_page()
    homepage.change_filter_by_platform("Browser")


def test_filter_by_category(driver):
    homepage = HomePage(driver)
    homepage.open_main_page()
    homepage.change_filter_by_category("moba")


def test_filter_by_sort(driver):
    homepage = HomePage(driver)
    homepage.open_main_page()
    homepage.change_filter_by_sort("Popularity")
