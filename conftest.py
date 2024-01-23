import pytest


# предусловие - создать экземпляр класса, добавить книгу без жанра в словарь
@pytest.fixture
def one_book_in_dict_without_range(books_coll):
    books_coll.add_new_book('Понедельник начинается в субботу')
    return books_coll


# предусловие - создать экземпляр класса, добавить книгу в словарь, установить ей жанр
@pytest.fixture
def one_book_in_dict_with_range(one_book_in_dict_without_range):
    one_book_in_dict_without_range.set_book_genre('Понедельник начинается в субботу', 'Фантастика')
    return one_book_in_dict_without_range


# предусловие - создать экземпляр класса, добавить книгу без жанра в словарь, добавить книгу в избранное
@pytest.fixture
def one_book_in_favorite(one_book_in_dict_without_range):
    one_book_in_dict_without_range.add_book_in_favorites('Понедельник начинается в субботу')
    return one_book_in_dict_without_range
