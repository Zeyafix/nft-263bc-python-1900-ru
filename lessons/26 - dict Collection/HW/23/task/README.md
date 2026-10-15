# Задание 23. Регистрация на турнир

Создайте программу `main.py`. 

В начале участников нет. Повторяйте запрос команды: add, cancel, check, list или stop. После add, cancel и check запросите имя (одно непустое английское слово, регистр значим). add регистрирует имя, а повторная регистрация не создаёт дубликат. cancel отменяет регистрацию, если она есть. Сообщайте об успехе, повторе или отсутствии. check выводит True/False. list показывает всех участников одной коллекцией в любом порядке, включая пустую. stop завершает программу. После list и stop имя не запрашивается. Вводятся только перечисленные команды.

## Пример 1

```text
Enter a command (add/cancel/check/list/stop): add
Enter a name: Emma
Registered

Enter a command (add/cancel/check/list/stop): add
Enter a name: Emma
Already registered

Enter a command (add/cancel/check/list/stop): check
Enter a name: Emma
Registered: True

Enter a command (add/cancel/check/list/stop): list
Members: ['Emma']

Enter a command (add/cancel/check/list/stop): cancel
Enter a name: Emma
Registration cancelled

Enter a command (add/cancel/check/list/stop): check
Enter a name: Emma
Registered: False

Enter a command (add/cancel/check/list/stop): list
Members: []

Enter a command (add/cancel/check/list/stop): stop
```

## Пример 2

```text
Enter a command (add/cancel/check/list/stop): list
Members: []

Enter a command (add/cancel/check/list/stop): cancel
Enter a name: Liam
Member not found

Enter a command (add/cancel/check/list/stop): stop
```
