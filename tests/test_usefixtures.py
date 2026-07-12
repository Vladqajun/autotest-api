import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database") #pytest.mark.usefixtures строенная маркировка
class TestLibrary:                                                      #нужна чтобы не прописывать фикстуры в тестах
                                                                        #лучше использовать не возвращающие значения фикстуры
    def test_read_book_from_library(self):
        ...


    def test_delete_book_from_library(self):
        ...