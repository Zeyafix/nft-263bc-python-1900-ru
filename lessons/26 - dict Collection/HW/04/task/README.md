# Задание 04. Изменение набора

Создайте программу `main.py`. Используйте исходные данные:

```python
colors = {"red", "blue"}
```

Добавьте в set новый элемент "yellow", затем уже имеющийся "red". Покажите набор после добавлений. Запросите цвет для удаления: непустое английское слово в нижнем регистре. Сначала проверьте наличие, затем удалите цвет, если он есть. Сообщите, был ли он удалён, и покажите итоговый набор. Элементы показывайте одной коллекцией в любом порядке. Дубликатов быть не должно.

## Пример 1

```text
After additions: ['blue', 'red', 'yellow']

Enter a color to remove: red
Color removed

Remaining colors: ['blue', 'yellow']
```

## Пример 2

```text
After additions: ['blue', 'red', 'yellow']

Enter a color to remove: black
Color not found

Remaining colors: ['blue', 'red', 'yellow']
```
