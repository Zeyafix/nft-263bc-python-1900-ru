# Задание 33. Новая книга

Создайте программу `main.py`. Используйте исходные данные:

```python
catalog = {"Dune": "Frank Herbert", "Coraline": "Neil Gaiman"}
```

Запросите название книги, затем имя автора — непустой текст на английском, допускаются пробелы. Если такого названия ещё нет, добавьте запись и сообщите о добавлении. Если название уже есть, сообщите об этом и сохраните прежнего автора. В обоих случаях покажите весь каталог. Регистр учитывается, а старые записи и порядок сохраняются, новая запись идёт в конце.

## Пример 1

```text
Enter the book title: The Hobbit
Enter the author: J. R. R. Tolkien
Book added

Catalog: {'Dune': 'Frank Herbert', 'Coraline': 'Neil Gaiman', 'The Hobbit': 'J. R. R. Tolkien'}
```

## Пример 2

```text
Enter the book title: Dune
Enter the author: Other Author
Book already exists

Catalog: {'Dune': 'Frank Herbert', 'Coraline': 'Neil Gaiman'}
```
