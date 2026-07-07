

def test_first_try():
    print("Hello World !!!")


def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    x, y = 5, 2
    assert (x - x) == y, "x - x is not equal to y"













# def test_user_login():
#     pass
#
#
# class TestUserAuthentication:
#     #Тестовые классы не должны иметь __init__ конструктора
#     #но можно добавлять статические значения (поля)
#
#     def test_create_user(self):
#         pass
#
#     def test_update_user(self):
#         pass
"""
памятка по урокам:
запускать автотесты через команду в терминале python -m pytest 
с помощью этой команды ты запускаешь ВСЕ автотесты, вот доп флаги
-s -чтобы выводились принты в консоль, pytest подефолту перекрывает поток sys.out
-v -для более подробной информации
-k "example" -для запуска конкретного или конкретных, если совпадает указанное слово
-m -запуск только маркированных автотестов 

еще можно запускать несколько выбранных автотестов:
python -m pytest -s -v -k "first or one" таким образом будут запущены 2 автотеста и first и one
можно исключить какой-нибудь:
"test and not two" и запустятся все кроме с именем two
"""


"""
Короче, названия модулей должно либо начинаться либо заканчиваться test
а классы, функции методы уже только начинаться
Названия класса тестов
TestUserAuthentication + (Test*)
SuiteUser -
UserTest - 
CheckUser - 
CheckUserTest -

названия автотестов
test_user_login + (test_)
check_user_login -
suite_user_login -
user_login_test -
"""