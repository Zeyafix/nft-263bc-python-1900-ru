# Задание 25. Доступные форматы

Создайте программу `main.py`. Используйте исходные данные:

```python
formats = frozenset(("txt", "csv", "json"))
```

Запросите имена файлов одной строкой через пробел. Каждое имя содержит ровно одну точку, непустое название и непустое расширение из английских букв в нижнем регистре, например notes.txt. Пустая строка означает отсутствие файлов. Для каждого файла в исходном порядке покажите имя и True/False: разрешено ли расширение. Повторы файлов сохраняйте. Затем покажите все поддерживаемые форматы одной коллекцией в любом порядке. Набор форматов не изменяйте.

## Пример 1

```text
Enter file names: notes.txt image.png data.csv notes.txt

File: notes.txt True
File: image.png False
File: data.csv True
File: notes.txt True
Supported formats: ['csv', 'json', 'txt']
```

## Пример 2

```text
Enter file names: 

Supported formats: ['csv', 'json', 'txt']
```
