import pytest


@pytest.fixture()
def before_each(request):
    print("Called before each test " + request.node.name)


@pytest.fixture(scope='session', autouse=True)
def init_browser(request):
    print("Called before all test " + request.node.name)


@pytest.fixture()
def message():
    return "this is message"


@pytest.fixture()
def firefox():
    return " "


@pytest.fixture()
def chrome():
    return " "


@pytest.fixture()
def chrome_mobile():
    return " "


@pytest.fixture()
def client():
    client = 123
    print("Подготовили клиента")
    yield client
    print("А теперь удаляем клиента")

# декоратор
# @pytest.fixture()
# def client():
#     yield
#     print("Удаляем клиента")


def test_mobile_page(chrome_mobile):
    pass


def test_first(before_each):
    assert 1 == 1


def test_second(before_each):
    assert 1 == 2, "Единица не равна двойке"


def test(message):
    print(message)
    assert "message" in message


def test_client(client):
    assert client == 123
