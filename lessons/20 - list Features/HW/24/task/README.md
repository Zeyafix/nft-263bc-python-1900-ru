# Задание 24. Отмена покупки

Создайте программу `main.py`.

Исходные данные:

```python
cart = ["bread", "milk", "bread", "apples", "bread"]
```

Введите название товара. Сравнивайте названия целиком с учётом регистра. Если товар есть в корзине, уберите его первое вхождение и выведите `Purchase cancelled`; остальные одинаковые товары остаются. Если товара нет, выведите `Item not found`. Затем выведите корзину.

## Пример

```text
Enter the item to cancel: bread

Purchase cancelled
['milk', 'bread', 'apples', 'bread']
```
