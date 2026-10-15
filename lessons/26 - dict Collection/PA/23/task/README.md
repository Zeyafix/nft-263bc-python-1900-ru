# Задание 23. Участники кружка

Создайте программу `main.py`. Используйте исходные данные:

```python
members = {"Mia", "Noah", "Ava"}
```

Запросите три непустых английских имени: вступающего, проверяемого и выходящего участника. Сначала добавьте вступающего, затем покажите True или False — присутствует ли проверяемый после добавления. Затем уберите выходящего и выведите оставшихся по одному на строке в любом порядке. Повторное вступление не создаёт второго участника, а выход отсутствующего ничего не меняет. Регистр имён учитывается.

## Пример 1

```text
Enter the joining member: Zoe
Enter the member to check: Zoe
Enter the leaving member: Noah

Member is present: True

Remaining members:
Ava
Mia
Zoe
```

## Пример 2

```text
Enter the joining member: Zoe
Enter the member to check: Zoe
Enter the leaving member: Zoe

Member is present: True

Remaining members:
Ava
Mia
Noah
```
