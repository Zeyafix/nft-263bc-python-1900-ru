# Задание 15. Чтение вложенных данных

Создайте программу `main.py`.

Исходные данные:

```python
rows = [[11, 12, 13], [21], [], [31, 32]]
```

Здесь строка — вложенный список чисел. Строки имеют разную длину, одна из них пустая. Введите количество запросов (от 0), затем для каждого запроса отдельно индекс строки и индекс элемента. Индексы без дробной части, могут быть отрицательными. Если оба индекса допустимы, выведите выбранное число; иначе — `Invalid position`. Проверяйте позицию относительно выбранной строки.

## Пример

```text
Enter the number of queries: 4

Enter a row index: 0
Enter an element index: 2
13

Enter a row index: 1
Enter an element index: 0
21

Enter a row index: 2
Enter an element index: 0
Invalid position

Enter a row index: -1
Enter an element index: -1
32
```

## Ещё один пример

```text
Enter the number of queries: 4
Enter a row index: 1
Enter an element index: 1
Invalid position
Enter a row index: 4
Enter an element index: 0
Invalid position
Enter a row index: -5
Enter an element index: 0
Invalid position
Enter a row index: 0
Enter an element index: -4
Invalid position
```
