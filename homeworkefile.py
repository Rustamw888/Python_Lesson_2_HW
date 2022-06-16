from selene import have
from selene.support.shared import browser


#
# @pytest.fixture(autouse=True)
# def before_after():
#     browser.open('https://google.com')\
#         .driver\
#         .set_window_size(1600, 800)
#     browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
#     yield
#     browser.close()
#     print("Домашняя работа завершена")

#
# def test_search_positive(set_up):
#     browser \
#         .element('[id="search"]') \
#         .should(have.text('Selene - User-oriented Web UI browser tests in Python'))
#
#
# def test_search_negative(set_up):
#     browser \
#         .element('[id="search"]') \
#         .should_not(have.text('не Selene - User-oriented Web UI browser tests in Python'))


def test_search_positive():
    browser \
        .element('[id="search"]') \
        .should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_negative():
    browser \
        .element('[id="search"]') \
        .should_not(have.text('не Selene - User-oriented Web UI browser tests in Python'))
