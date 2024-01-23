# qa_python
В файле test.py реализовано 15 тестов. Из них 2 с параметризацией.
В файле conftest.py реализованы 3 фикстуры для создания предусловий перед выполнением тестов

**Тесты для метода add_new_book:**

* test_add_new_book_add_book_length_40 - передать книгу с названием в 40 символов (ОР: в словаре находится 1 книга)
* test_add_new_book_add_wrong_book (с параметризацией) - передать книгу, которая уже есть в словаре; передать книгу с названием в 41 символ (ОР: словарь не изменился)

**Тесты для метода set_book_genre:**

* test_set_book_genre_genre_in_list - передать книгу из словаря, с жанром из списка жанров (ОР: жанр установлен)
test_set_book_genre_genre_not_in_list - передать книгу из словаря с жанром, которого нет в списке жанров (ОР: жанр не установлен)

**Тесты для метода get_book_genre:**

* test_get_book_genre_return_correct_genre - передать книгу с жанром из словаря (ОР: жанр переданной книги совпадает с ее жанром в словаре)

**Тесты для метода get_books_with_specific_genre:**

* test_get_books_with_specific_genre_send_real_genre_of_book - передать жанр (ОР: выведется книга с этим жанром)
* test_get_books_with_specific_genre_send_another_genre - передать жанр (ОР: выведется пустой список, в котором не будет книги из словаря без жанра, не будет книги из словаря с другим жанром)

**Тесты для метода get_books_genre:**

* test_get_books_genre_book_dict_with_one_book - запросить словарь (ОР: получен текущий словарь)

**Тесты для метода get_books_for_children:**

* test_get_books_for_children_genre_not_in_list_genre_age_rating - передать жанр НЕ из списка ограничений (ОР: выведется книга с этим жанром)
* test_get_books_for_children_genre_in_list_genre_age_rating - передать жанр из списка ограничений (ОР: выведется пустой список)

**Тесты для метода add_book_in_favorites:**

* test_add_book_in_favorites_add_book_in_books_genre - передать книгу из словаря (ОР: книга добавлена в избранное)
* test_add_book_in_favorites_add_wrong_book (с параметризацией) - передать книгу НЕ из словаря; передать книгу которая уже есть в избранном (ОР: количество книг в избранном не изменится)

**Тесты для метода delete_book_from_favorites:**

* test_delete_book_from_favorites_book_in_favorites - передать книгу из избранного (ОР: книга удалена из избранного)
* test_delete_book_from_favorites_book_not_in_favorites - передать книгу НЕ из избранного (ОР: список избранного не изменился)

**Тесты для метода get_list_of_favorites_books:**

* test_get_list_of_favorites_books_list_with_one_book - запросить список избранного (ОР: выведется актуальный список)

Проверка свойств экземпляра класса происходит внутри тестов путем обращения к ним

**Фикстуры:**

    one_book_in_dict_without_range - создает экземпляр класса, добавляет книгу без жанра в словарь
    one_book_in_dict_with_range - создает экземпляр класса, добавляет книгу в словарь, устанавливает ей жанр
    one_book_in_favorite - создает экземпляр класса, добавляет книгу без жанра в словарь, добавляет книгу в избранное
