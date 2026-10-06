# Задание 13. Очистка краёв

Запросите текст, затем непустой набор удаляемых символов. Сравните `strip()`, `lstrip()` и `rstrip()` без аргумента и с введённым набором. Все шесть операций применяются независимо к исходному тексту. Выведите результаты в квадратных скобках с подписями `Strip`, `Left`, `Right`, `Custom strip`, `Custom left`, `Custom right`. Набор задаёт отдельные символы, а не точный фрагмент. Пробелы внутри текста сохраняются; текст может быть пустым.

## Пример диалога

После подсказок показаны ответы пользователя.

```text
Text:   red blue  
Characters to remove at the edges:  

Strip: [red blue]
Left: [red blue  ]
Right: [  red blue]
Custom strip: [red blue]
Custom left: [red blue  ]
Custom right: [  red blue]
```
