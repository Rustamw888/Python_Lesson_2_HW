import pytest
from selene import be
from selene.support.shared import browser


# @pytest.fixture
# def set_up():
#     browser.open('https://google.com')\
#         .driver\
#         .set_window_size(1600, 800)
#     browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
#     yield
#     browser.close()
#     print("Домашняя работа завершена")

# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(autouse=True)
def set_up():
    browser.open('https://google.com')\
        .driver\
        .set_window_size(1600, 800)
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    yield
    browser.close()
    print("Домашняя работа завершена")
