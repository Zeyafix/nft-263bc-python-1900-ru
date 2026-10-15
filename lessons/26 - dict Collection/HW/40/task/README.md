# Задание 40. Выдача оборудования

Создайте программу `main.py`. 

Используйте словарь «инвентарный номер — имя получателя», вначале пустой. Обрабатывайте команды issue, return, list, stop до stop. После issue запросите номер, затем имя получателя. Номер — непустой код из английских букв и цифр, имя — одно английское слово, регистр значим. После return запросите только номер. Любой незанятый номер можно выдать. Занятый номер повторно не выдавайте и прежнего получателя сохраняйте. Возврат удаляет текущую выдачу, а возврат неизвестного номера ничего не меняет. Сообщайте об успехе, занятости или отсутствии выдачи. После issue, return и list показывайте все текущие выдачи одной коллекцией в порядке записей. Новая выдача добавляется в конец. После list и stop дополнительных данных не запрашивайте. Все команды допустимы.

## Пример 1

```text
Enter a command (issue/return/list/stop): issue
Enter an inventory number: C01
Enter a borrower name: Emma
Equipment issued
Current loans: {'C01': 'Emma'}

Enter a command (issue/return/list/stop): issue
Enter an inventory number: C01
Enter a borrower name: Liam
Equipment already issued
Current loans: {'C01': 'Emma'}

Enter a command (issue/return/list/stop): return
Enter an inventory number: C01
Equipment returned
Current loans: {}

Enter a command (issue/return/list/stop): issue
Enter an inventory number: C01
Enter a borrower name: Liam
Equipment issued
Current loans: {'C01': 'Liam'}

Enter a command (issue/return/list/stop): stop
```

## Пример 2

```text
Enter a command (issue/return/list/stop): list
Current loans: {}

Enter a command (issue/return/list/stop): return
Enter an inventory number: X99
Loan not found
Current loans: {}

Enter a command (issue/return/list/stop): stop
```
