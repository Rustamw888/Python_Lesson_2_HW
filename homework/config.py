import pytest
from selene import be
from selene.support.shared import browser


@pytest.fixture
def first_fixture_part1():
    browser.open('https://google.com')\
        .driver\
        .set_window_size(1600, 800)
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    yield
    browser.close()
    print("Домашняя работа часть 1 - завершена!")


@pytest.fixture(scope='session')
def first_fixture_part2():
    browser.open('https://demoqa.com/automation-practice-form')\
        .driver\
        .set_window_size(1920, 1080)
    yield
    browser.close()
    print("Домашняя работа часть 2 - завершена!")
