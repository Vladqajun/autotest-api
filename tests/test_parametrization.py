import pytest
from _pytest.fixtures import SubRequest
def test_number1():
    assert 1 > 0

def test_number2():
    assert 2 > 0

def test_number3():
    assert 3 > 0

def test_number4():
    assert -1 > 0

@pytest.mark.parametrize("number", [1, 2, 3, -1, 5])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stage.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stage.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running test on host: {host}")

#параметризация теста и фикстуры
#разница в том что ты параметризируешь только тест, а при параметризации фикстуры каждый тест запустится N раз
#область видимости также при parametrize будет только функция, а при pytest.fixture(params=...) можно указать любую
#проще писать для множества тестов, написал 1 раз и используешь

class TestOperations:
    def test_user_with_operations(self):
        print(f"User with operations: ")

    def test_user_without_operations(self):
        print(f"User with no operations: ")

users = {
    "+7000000001": "User with money on bank account",
    "+7000000002": "User with no money on bank account",
    "+7000000003": "User with operations on bank account"
}

@pytest.mark.parametrize( #(аргумент, возможные его значения, алиасы(id) этих значений)
    "phone_number", #количественно id и значения должны совпадать
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifier(phone_number: str):
    pass