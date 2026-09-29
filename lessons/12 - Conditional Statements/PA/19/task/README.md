# Задание 19. Аккаунт и баланс

Запросите логин (`Login: `) и пароль (`Password: `). Верные данные — `admin` и `root1234`; регистр важен. При ошибке выведите `Invalid credentials` и завершите программу. При успешном входе начальный баланс равен 1000.00. Очистите терминал и покажите:

```text
Login: admin
Balance: 1000.00

1 - Deposit
2 - Withdraw
```

Запросите пункт с подсказкой `Choice: ` и сразу очистите терминал. При выборе `1` запросите пополнение (`Amount: `), при `2` — снятие (`Amount: `). Сумма может содержать копейки. При нуле или отрицательной сумме выведите `Invalid amount`. При снятии больше баланса выведите `Insufficient funds`. При ошибках баланс не меняется. При успешном пополнении выведите `Deposit successful`, при снятии — `Withdrawal successful`. После любой попытки пополнения или снятия запросите любое значение с подсказкой `Press enter to continue...`. Для отсутствующего пункта выведите `Invalid choice`, не запрашивая сумму и продолжение.

В конце после успешного входа снова очистите терминал и выведите только логин и текущий баланс на двух строках с подписями `Login: ` и `Balance: `. Баланс всегда показывайте с двумя знаками после точки. Один запуск выполняет только одну операцию; повторять меню не нужно. После ошибки входа очищать терминал и показывать баланс не нужно.

В примере `[screen cleared]` — пояснение, его печатать не нужно.

## Примеры

После подсказок показан ввод пользователя.

```text
Login: admin
Password: root1234
[screen cleared]
Login: admin
Balance: 1000.00

1 - Deposit
2 - Withdraw
Choice: 1
[screen cleared]
Amount: 250.5
Deposit successful
Press enter to continue...
[screen cleared]
Login: admin
Balance: 1250.50
```

```text
Login: admin
Password: root1234
[screen cleared]
Login: admin
Balance: 1000.00

1 - Deposit
2 - Withdraw
Choice: 2
[screen cleared]
Amount: 250.5
Withdrawal successful
Press enter to continue...
[screen cleared]
Login: admin
Balance: 749.50
```
