# Задание 30. Отбор заявок

Создайте программу `main.py`.

Введите возрасты кандидатов в полных годах через пробел, каждый от 0. Пустая строка означает отсутствие заявок. Затем отдельно введите минимальный и максимальный допустимые возрасты. Границы от 0, минимум не больше максимума. Соберите отдельный список подходящих возрастов: обе границы включены. Сохраните порядок, повторы и исходные данные. Выведите исходный список с `Original:`, отобранный с `Selected:`.

## Пример

```text
Enter ages separated by spaces (empty for none): 13 18 50 18 51 30
Enter the minimum age: 18
Enter the maximum age: 50

Original: [13, 18, 50, 18, 51, 30]
Selected: [18, 50, 18, 30]
```

## Ещё один пример

```text
Enter ages separated by spaces (empty for none): 
Enter the minimum age: 0
Enter the maximum age: 100

Original: []
Selected: []
```
