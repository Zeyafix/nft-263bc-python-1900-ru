# Задание 20. Два способа удаления

Создайте программу `main.py`. Используйте исходные данные:

```python
prices = {"tea": 0, "cake": 7, "milk": 4}
```

Запросите два названия товара. Сначала удалите первый ключ через del, если он есть. Сообщите об удалении или отсутствии. Затем из того же словаря удалите второй ключ через pop(), если он ещё есть, и покажите возвращённое значение. Иначе сообщите об отсутствии. Ключи могут совпадать. В конце выведите оставшийся словарь в порядке записей.

## Пример 1

```text
Enter a key for del: cake
Enter a key for pop: tea

First key deleted
Removed value: 0

Remaining: {'milk': 4}
```

## Пример 2

```text
Enter a key for del: rice
Enter a key for pop: bread

First key not found
Second key not found

Remaining: {'tea': 0, 'cake': 7, 'milk': 4}
```
