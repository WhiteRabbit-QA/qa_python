import pytest


class TestBooksCollector:

    # передать книгу с названием в 40 символов == в словаре 1 книга
    def test_add_new_book_add_book_length_40(self, books_coll):
        books_coll.add_new_book('КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига')
        assert len(books_coll.books_genre) == 1

    # передать книгу с названием в 0 и 41 символ == словарь не изменился
    @pytest.mark.parametrize(
        'wrong_len_name',
        [
            'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКниг41',
            ''
        ]
    )
    def test_add_new_book_add_wrong_book(self, books_coll, wrong_len_name):
        books_coll.add_new_book(wrong_len_name)
        assert books_coll.books_genre == {}

    # передать книгу, которая уже есть в словаре == словарь не изменился
    def test_add_new_book_add_book_wich_added(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.add_new_book('Понедельник начинается в субботу')
        assert len(one_book_in_dict_without_genre.books_genre) == 1

    # передать книгу из словаря, с жанром из списка жанров == жанр установлен
    def test_set_book_genre_genre_in_list(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.set_book_genre('Понедельник начинается в субботу', one_book_in_dict_without_genre.genre[0])
        assert one_book_in_dict_without_genre.books_genre['Понедельник начинается в субботу'] == 'Фантастика'

    # передать книгу из словаря с жанром, которого нет в списке жанров == жанр не установлен
    def test_set_book_genre_genre_not_in_list(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.set_book_genre('Понедельник начинается в субботу', 'Приключения')
        assert one_book_in_dict_without_genre.books_genre['Понедельник начинается в субботу'] == ''

    # передать книгу с жанром из словаря == жанр переданной книги совпадает с ее жанром в словаре
    def test_get_book_genre_return_correct_genre(self, one_book_in_dict_with_genre):
        assert one_book_in_dict_with_genre.get_book_genre('Понедельник начинается в субботу') == 'Фантастика'

    # передать жанр == выведется книга с этим жанром
    def test_get_books_with_specific_genre_send_real_genre_of_book(self, one_book_in_dict_with_genre):
        assert one_book_in_dict_with_genre.get_books_with_specific_genre('Фантастика') == ['Понедельник начинается в субботу']

    # передать жанр == не будет книги из словаря без жанра, не будет книги из словаря с другим жанром
    def test_get_books_with_specific_genre_send_another_genre(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.add_new_book('Приключения Буратино')
        one_book_in_dict_without_genre.set_book_genre('Приключения Буратино', 'Мультфильмы')
        assert one_book_in_dict_without_genre.get_books_with_specific_genre('Детективы') == []

    # запросить словарь == получен текущий словарь
    def test_get_books_genre_book_dict_with_added_book(self, books_coll):
        books_coll.add_new_book('Книга 1')
        books_coll.add_new_book('Книга 2')
        assert books_coll.get_books_genre() == {'Книга 1': '', 'Книга 2': ''}

    # передать жанр НЕ из списка ограничений == выведется книга с этим жанром
    def test_get_books_for_children_genre_not_in_list_genre_age_rating(self, one_book_in_dict_with_genre):
        assert one_book_in_dict_with_genre.get_books_for_children() == ['Понедельник начинается в субботу']

    # передать жанр из списка ограничений == выведется пустой список
    def test_get_books_for_children_genre_in_list_genre_age_rating(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.set_book_genre('Понедельник начинается в субботу', one_book_in_dict_without_genre.genre_age_rating[0])
        assert one_book_in_dict_without_genre.get_books_for_children() == []

    # передать книгу из словаря == книга добавлена в избранное
    def test_add_book_in_favorites_add_book_in_books_genre(self, one_book_in_dict_without_genre):
        one_book_in_dict_without_genre.add_book_in_favorites('Понедельник начинается в субботу')
        assert one_book_in_dict_without_genre.favorites == ['Понедельник начинается в субботу']

    # передать книгу НЕ из словаря == количество книг в избранном не изменится
    # передать книгу которая уже есть в избранном == количество книг в избранном не изменится
    @pytest.mark.parametrize('wrong_book', ['Приключения Буратино', 'Понедельник начинается в субботу'])
    def test_add_book_in_favorites_add_wrong_book(self, one_book_in_favorite, wrong_book):
        one_book_in_favorite.add_book_in_favorites(wrong_book)
        assert len(one_book_in_favorite.favorites) == 1

    # передать книгу из избранного == книга удалена из избранного
    def test_delete_book_from_favorites_book_in_favorites(self, one_book_in_favorite):
        one_book_in_favorite.delete_book_from_favorites('Понедельник начинается в субботу')
        assert one_book_in_favorite.favorites == []

    # передать книгу НЕ из избранного == список избранного не изменился
    def test_delete_book_from_favorites_book_not_in_favorites(self, one_book_in_favorite):
        one_book_in_favorite.delete_book_from_favorites('Приключения Буратино')
        assert one_book_in_favorite.favorites == ['Понедельник начинается в субботу']

    # запросить список избранного == выведется актуальный список
    def test_get_list_of_favorites_books_list_with_one_book(self, one_book_in_favorite):
        assert one_book_in_favorite.get_list_of_favorites_books() == ['Понедельник начинается в субботу']
