# Задание 22. Исправление маршрута

Создайте программу `main.py`. Используйте исходные данные:

```python
route = ("Harbor", "Old Town", "Museum", "Airport")
```

Запросите номер остановки от 1 до 4 и новое название (непустая строка на английском, возможны пробелы). Через временный список замените выбранную остановку и получите новый кортеж. Покажите исходный и исправленный маршруты целиком. Остальные остановки и их порядок сохраняются.

## Пример 1

```text
Enter a stop number: 1
Enter a new stop name: Central Park

Original route: ('Harbor', 'Old Town', 'Museum', 'Airport')
Updated route: ('Central Park', 'Old Town', 'Museum', 'Airport')
```

## Пример 2

```text
Enter a stop number: 4
Enter a new stop name: Station

Original route: ('Harbor', 'Old Town', 'Museum', 'Airport')
Updated route: ('Harbor', 'Old Town', 'Museum', 'Station')
```
