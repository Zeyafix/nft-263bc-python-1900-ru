# Задание 25. Разрешённые команды

Создайте программу `main.py`. Используйте исходные данные:

```python
commands = frozenset({"open", "save", "quit"})
```

Запросите одну непустую команду на английском. Покажите True, если она разрешена, иначе False. Затем выведите все допустимые команды по одной на строке в любом порядке. Сравнение учитывает регистр и полное имя: "Open" и "pen" не совпадают с "open".

## Пример 1

```text
Enter a command: save

Command is allowed: True

Available commands:
open
quit
save
```

## Пример 2

```text
Enter a command: delete

Command is allowed: False

Available commands:
open
quit
save
```
