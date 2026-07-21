import pytest

# @pytest.mark.smoke
# def test_smoke_case():
#     assert True
#
# @pytest.mark.regression
# def test_regression_case():
#     assert True



#эта маркировка класса применится ко всем его методам
# @pytest.mark.smoke
# class TestSuite:
#     def test_case1(self):
#         assert True
#
#     def test_case2(self):
#         assert True
#
# #Тут к методам класса применятся и маркировка класса и отдельная маркировка метода
# @pytest.mark.regression
# class TestUserAuthentication:
#     @pytest.mark.smoke
#     def test_login(self):
#         assert True
#
#     @pytest.mark.slow
#     def test_password_reset(self):
#         assert True
#
#     def test_logout(self):
#         assert True
#
# # @pytest.mark.regression
# # @pytest.mark.critical
# # @pytest.mark.smoke #у одного теста может быть хоть сколько маркировок
# # def test_critical_login():
# #     assert True
#
# @pytest.mark.api
# class TestUserInterface:
#     @pytest.mark.smoke
#     @pytest.mark.critical
#     def test_login(self):
#         ...
#
#     @pytest.mark.regression
#     def test_forgot_password(self):
#         ...
#     @pytest.mark.smoke
#     def test_signup(self):
#         ...