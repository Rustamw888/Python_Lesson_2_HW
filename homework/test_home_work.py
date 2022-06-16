from selene import have
from selene.support.shared import browser
from homework.config import first_fixture_part1


def test_search_positive(first_fixture_part1):
    browser \
        .element('[id="search"]') \
        .should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_negative(first_fixture_part1):
    browser \
        .element('[id="search"]') \
        .should_not(have.text('не yashaka/selene: User-oriented Web UI browser tests in Python'))
