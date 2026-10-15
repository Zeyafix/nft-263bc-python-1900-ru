# Задание 06. Проверка пересечения

Создайте программу `main.py`. Используйте исходные данные:

```python
first = {"chess", "art", "music"}
second = {"music", "art", "dance"}
third = {"sport", "coding"}
```

Проверьте только две пары множеств в таком порядке:

1. `first` и `second`.
2. `first` и `third`.

Для каждой из этих двух пар сначала с помощью `isdisjoint()` определите, есть ли общие элементы: выведите `True`, если есть, иначе `False`. Затем получите пересечение через `&` и покажите его одной коллекцией в любом порядке.

## Пример 1

```text
First and second overlap: True
Common: ['art', 'music']

First and third overlap: False
Common: []
```
