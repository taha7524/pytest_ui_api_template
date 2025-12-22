import pytest
import allure
from page.main_page import MainPage
from selenium import webdriver
from config import MAIN_URL, TITLE


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(MAIN_URL)
    return MainPage(driver, MAIN_URL)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(TITLE)


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск сериалов по названию")
@pytest.mark.parametrize("film_title",
                         ["Ищейка", "Тригер 2"])
def test_search_tv_series_by_title(main_page, film_title):
    with allure.step(f"Поиск сериалов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название сериала {film_title} \
                     содержится в результатах"):
        assert film_title in main_page.find_book_titles()
        assert len(main_page.find_book_titles())


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию из одного слова")
@pytest.mark.parametrize("film_title",
                         ["Девчата", "Фантомас"])
def test_search_movies_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильмов {film_title} \
                    содержится в результатах"):
        assert film_title in main_page.find_book_titles()
        assert len(main_page.find_book_titles())


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию из нескольких слов")
@pytest.mark.parametrize("film_title",
                         ["Кавказкая пленница",
                          "Весна на заречной улице",
                          'Они сражались за родину'])
def test_search_movies_long_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильмов {film_title} \
                     содержится в результатах"):
        assert film_title in main_page.find_book_titles()
        assert len(main_page.find_book_titles())


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск актеров")
@pytest.mark.parametrize("name",
                         ["Джек Николсон",
                          "Василий Лановой",
                          'Анна Банщикова'])
def test_search_persons_by_title(main_page, name):
    with allure.step(f"Поиск актеров по имени"
                     f" {name}"):
        main_page.search_items_by_phrase(name)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
