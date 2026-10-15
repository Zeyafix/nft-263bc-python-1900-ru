# Задание 26. Телефонная книга

Создайте программу `main.py`. Используйте исходные данные:

```python
contacts = {"Emma": "00123", "Liam": "00456"}
```

Обрабатывайте команды find, add, update, delete, list, stop до stop. После первых четырёх запросите имя (одно непустое английское слово, регистр значим). После add и update запросите телефон: от 3 до 15 цифр, ведущие нули сохраняются. find показывает номер или сообщение об отсутствии. add добавляет только новое имя. update меняет только существующе. delete удаляет только существующее. Сообщайте результат каждого действия. list показывает всю книгу одной коллекцией в порядке записей, новые имена — в конце. После list и stop дополнительных данных не запрашивайте. Все команды допустимы.

## Пример 1

```text
Enter a command (find/add/update/delete/list/stop): find
Enter a name: Emma
Phone: 00123

Enter a command (find/add/update/delete/list/stop): add
Enter a name: Olivia
Enter a phone number: 00789
Contact added

Enter a command (find/add/update/delete/list/stop): update
Enter a name: Liam
Enter a phone number: 00012
Contact updated

Enter a command (find/add/update/delete/list/stop): delete
Enter a name: Emma
Contact deleted

Enter a command (find/add/update/delete/list/stop): list
Contacts: {'Liam': '00012', 'Olivia': '00789'}

Enter a command (find/add/update/delete/list/stop): stop
```

## Пример 2

```text
Enter a command (find/add/update/delete/list/stop): add
Enter a name: Emma
Enter a phone number: 999
Contact already exists

Enter a command (find/add/update/delete/list/stop): update
Enter a name: Noah
Enter a phone number: 888
Contact not found

Enter a command (find/add/update/delete/list/stop): find
Enter a name: Noah
Contact not found

Enter a command (find/add/update/delete/list/stop): delete
Enter a name: Noah
Contact not found

Enter a command (find/add/update/delete/list/stop): list
Contacts: {'Emma': '00123', 'Liam': '00456'}

Enter a command (find/add/update/delete/list/stop): stop
```
