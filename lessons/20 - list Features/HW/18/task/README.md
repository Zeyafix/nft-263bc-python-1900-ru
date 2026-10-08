# Задание 18. Остановки маршрута

Создайте программу `main.py`.

Исходные данные:

```python
stops = ["Station", "Park", "Museum", "Harbor", "Airport"]
```

Введите номер остановки без дробной части. Номера начинаются с 1. Для существующей остановки выведите её название с подписью `Stop:`, предыдущую с `Previous:` и следующую с `Next:`. Если соответствующего соседа нет, вместо его названия выведите `None`. Для несуществующего номера выведите только `Invalid stop`.

## Пример

```text
Enter a stop number: 3

Stop: Museum
Previous: Park
Next: Harbor
```

## Ещё один пример

```text
Enter a stop number: 1

Stop: Station
Previous: None
Next: Park
```
