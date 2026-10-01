# Задание 21. Регистрация и личный кабинет

Создайте учебную программу для одного аккаунта. При запуске аккаунта ещё нет.
Данные сохраняются только до завершения программы. Перед каждым выбором в главном меню показывайте:

```text
1. Log in
2. Register
0. Exit program
```

Запросите пункт с подсказкой `Choice: `.

При выборе пункта 1: запросите `Login: `, затем `Password: `. Если аккаунт существует и оба значения точно совпали, выведите `Login successful` и откройте личный кабинет. Иначе выведите `Invalid credentials` и вернитесь к главному меню.

При выборе пункта 2: если аккаунта ещё нет, запросите `New login: `, затем `New password: `, создайте аккаунт с балансом `0.00`, выведите `Registered` и вернитесь к главному меню.
Вход после регистрации не выполняется автоматически.
Если аккаунт уже есть, выведите `Already registered`, не запрашивая новых данных и не меняя существующие, затем вернитесь к главному меню.

При выборе пункта 0: выведите `Goodbye` и завершите программу.

Другой ответ: выведите `Unknown option` и повторите главное меню.

Логины и пароли непустые, состоят из латинских букв и цифр. Регистр важен.

Перед каждым выбором в личном кабинете выводите `Login: ` и логин аккаунта, на следующей строке `Balance: ` и текущий баланс, затем меню:

```text
1. Deposit
2. Withdraw
3. Log out
0. Exit program
```

Запросите действие с подсказкой `Action: `.

При выборе пункта 1: запросите сумму с подсказкой `Amount: `.
Положительная сумма пополняет баланс. Выведите `Deposited`.
При нуле или отрицательной сумме выведите `Invalid amount`, сохранив баланс.

При выборе пункта 2: запросите `Amount: `.
При нуле или отрицательной сумме выведите `Invalid amount`.
Если положительная сумма больше баланса, выведите `Insufficient funds`.
Иначе уменьшите баланс и выведите `Withdrawn`.
Снять весь баланс разрешено. Отказ не меняет баланс.

При выборе пункта 3: выведите `Logged out` и вернитесь к главному меню, сохранив аккаунт и баланс для следующего входа.

При выборе пункта 0: выведите `Goodbye` и завершите всю программу.

Другой ответ: выведите `Unknown option`, сохранив данные.

После пополнения, снятия или ошибки снова показывайте личный кабинет.
Суммы могут содержать копейки, например `10.50`.

## Пример

После подсказок показан ввод пользователя.

```text
1. Log in
2. Register
0. Exit program
Choice: 2

New login: teston
New password: abc123

Registered

1. Log in
2. Register
0. Exit program
Choice: 1

Login: teston
Password: abc123
Login successful

Login: teston
Balance: 0.00
1. Deposit
2. Withdraw
3. Log out
0. Exit program
Action: 1

Amount: 10.50
Deposited

Login: teston
Balance: 10.50
1. Deposit
2. Withdraw
3. Log out
0. Exit program
Action: 2

Amount: 3.25
Withdrawn

Login: teston
Balance: 7.25
1. Deposit
2. Withdraw
3. Log out
0. Exit program
Action: 3
Logged out

1. Log in
2. Register
0. Exit program
Choice: 1

Login: teston
Password: abc123
Login successful

Login: teston
Balance: 7.25
1. Deposit
2. Withdraw
3. Log out
0. Exit program
Action: 0

Goodbye
```
