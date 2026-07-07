from pickletools import read_stringnl

import pytest


@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert False

@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте все еще есть маркировка xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_external_services_is_unavailable():
    assert False

#@pytest.mark.xfail(reason="") запускает но ожидает провала теста, а потому прогон не падает в ci/cd пайплайне
#@pytest.mark.skip(reason="") пропускает (не запускает) тест
#@pytest.mark.skip(условие, reason="") пропускает при условии, требует reason

#когда что
#используй skip если тест вообще не должен запускаться (фича в разработке и он ничего не проверяет)
#xfail если мы ожидали падение, но которое может и не произойти (мы все таки проверяем функционал)
#(внешний сервис например недоступен, но не ронять же прогон из-за этого каждый раз, когда-то он будет доступен)