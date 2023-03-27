Задания 30.3.1 и 30.5.1 от SkillFactory. Тестирование UI сайта http://petfriends.skillfactory.ru.

30.3.1

Написать тест, который проверяет, что на странице со списком питомцев пользователя http://petfriends.skillfactory.ru/my_pets:

- присутствуют все питомцы;
- хотя бы у половины питомцев есть фото;
- у всех питомцев есть имя, возраст и порода;
- у всех питомцев разные имена;
- в списке нет повторяющихся питомцев.

30.5.1

Тесты для страницы со списком питомцев всех пользователей https://petfriends.skillfactory.ru/all_pets:
- в тесте <проверки карточек питомцев> добавить неявные ожидания всех элементов питомца: фото, имя, возраст;
- в тесте <проверки таблицы питомцев> добавить явные ожидания элементов страницы.

__________________________________________________________________________________________________________________________________

В директории /tests располагаются файлы с тестами.

В файле conftest.py находятся 2 фикстуры:
- фикстура с драйвером и переходом на страницу авторизации;
- фикстура для перехода на страницу "Мои питомцы".

В файле settings.py находятся данные о почте и пароле.
