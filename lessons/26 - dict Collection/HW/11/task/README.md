# Задание 11. Поиск ключа и значения

Создайте программу `main.py`. Используйте исходные данные:

```python
data = {"tea": 0, "coffee": 8, "juice": 8}
```

Запросите название товара, затем искомое количество (0 или больше, без дробной части). Отдельно проверьте наличие ключа через in и наличие количества через in data.values(). Выведите два ответа True/False в этом порядке. Нулевой остаток не означает отсутствие товара.

## Пример 1

```text
Enter a product: tea
Enter a quantity to find: 0

Key present: True
Value present: True
```

## Пример 2

```text
Enter a product: milk
Enter a quantity to find: 8

Key present: False
Value present: True
```
