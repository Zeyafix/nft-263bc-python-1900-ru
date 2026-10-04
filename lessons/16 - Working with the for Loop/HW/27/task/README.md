# Задание 27. Продажи по отделам

Запросите количество отделов. Отделы пронумерованы от 1. Для каждого отдела сначала запросите количество проданных товаров, затем цену каждого проданного товара отдельно.

Выручка отдела — сумма цен всех его проданных товаров. После ввода товаров отдела сразу выведите `Department <номер>: <выручка>` с выручкой с двумя знаками после точки. Затем переходите к следующему отделу. Если товаров нет, выручка равна `0.00`.

В конце выведите `Top department: <номер>` — номер отдела с наибольшей выручкой. При равной выручке выберите отдел с меньшим номером. Если во всех отделах выручка нулевая, это отдел 1.

## Пример диалога

После подсказок показаны ответы пользователя.

```text
Department count: 3

Department 1, sold item count: 2
Item 1 price: 10
Item 2 price: 20
Department 1: 30.00

Department 2, sold item count: 0
Department 2: 0.00

Department 3, sold item count: 1
Item 1 price: 40
Department 3: 40.00

Top department: 3
```

## Ещё один пример

```text
Department count: 3

Department 1, sold item count: 1
Item 1 price: 5
Department 1: 5.00

Department 2, sold item count: 2
Item 1 price: 2
Item 2 price: 3
Department 2: 5.00

Department 3, sold item count: 1
Item 1 price: 4
Department 3: 4.00

Top department: 1
```
