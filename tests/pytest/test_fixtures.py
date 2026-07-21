import pytest

@pytest.fixture(autouse=True) #Если автоиспользование = True, то фикстура будет запускаться каждый тест самостоятельно, не нужно прописывать ее в параметры функции
def send_analytics_data():    #(если не указал другой scope, то используется function) (в фикстуре user_client тож можно не указывать)
    print("[AUTOUSE] Отправляем данные на сервисы аналитики")


@pytest.fixture(scope="session")
def settings():
    print("[SETTINGS] Инициализируем настройки автотестов")


@pytest.fixture(scope="class") #scope class подразумевает что фикстура выполнится при первом вызове, далее закешируется и выполняться больше не будет
def user():                    #и так 1 раз на каждый класс и далее оно идет в таком порядке session > package > module > class > function
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")   #session выполнится раз за сессию т.е. при каждом запуске python -m pytest


@pytest.fixture(scope="function") #scope function означает область видимости, эта фикстура выполняется каждую функцию
def users_client(settings): #еще можно фикстуру передавать в фикстуру, на случай если в user-s_client нужны вычисляемые значения из settings
    print("[FUNCTION] Создаем API клиент на каждый автотест")  #settings 1 раз вычислит значение а потом будет передавать кэшированное значение, scope session у settings сохраняется и выполнится 1 раз, но НАОБОРОТ НЕЛЬЗЯ можно либо 1-го уровня, либо выше

class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self, settings, user, users_client):
        ...



class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...


@pytest.fixture
def user_data() -> dict:
    print("Создаем пользователя до теста (setup)") #Этот код выполняется до теста
    yield {"email": "test@example.com", "password": "123123"} # Возвращается поток для выполнения теста и возвращаются значения
    print("Удаляем пользователя после теста (teardown)") #Этот после теста, и фикстура не прекращает выполение пока не выполнится тест


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"


def test_user_password(user_data: dict):
    print(user_data)
    assert user_data["password"] == "123123"