# Задание 08. Разрешённые действия

Создайте программу `main.py`. Используйте исходные данные:

```python
queries = ("read", "delete", "share", "Read")
```

Создайте frozenset с действиями "read", "save", "share". Для каждого значения из queries выведите на одной строке само значение и результат проверки через `in`. Соблюдайте порядок queries.

## Пример 1

```text
Action: read True
Action: delete False
Action: share True
Action: Read False
```
