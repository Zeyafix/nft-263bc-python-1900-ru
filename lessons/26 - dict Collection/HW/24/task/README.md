# Задание 24. Подписчики двух каналов

Создайте программу `main.py`. 

Запросите имена подписчиков первого канала одной строкой через пробел, затем второго. Пустая строка означает отсутствие подписчиков. Имена — английские слова. Регистр значим, повторы в строке возможны, но один человек учитывается один раз. Покажите True/False: есть ли общие подписчики. Затем покажите три коллекции: подписчики обоих каналов, только первого, только второго. Внутри групп порядок свободный.

## Пример 1

```text
Enter first channel subscribers: Emma Liam Emma
Enter second channel subscribers: Liam Olivia

Have common subscribers: True
Both: ['Liam']
Only first: ['Emma']
Only second: ['Olivia']
```

## Пример 2

```text
Enter first channel subscribers: Emma
Enter second channel subscribers: Liam

Have common subscribers: False
Both: []
Only first: ['Emma']
Only second: ['Liam']
```
