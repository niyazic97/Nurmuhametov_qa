import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def size():
    browser.open('https://google.com')
    browser.driver.set_window_size(1280, 1000)



def test_search(size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_fail_search(size):
    browser.element('[name="q"]').should(be.blank).type('asdmmsddklfas;dkfklalsdflksdafl').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    print('Поиск не дал результатов')