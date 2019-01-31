# Practice-Task
Тестовое задание для прохождения практики в "Транзас"

Описание файла main.py:
Файл main.py представляет собой само консольное приложение, без функции расчета размена монет.

Описание файла solve.py:
Файл solve.py представляет собой функцию, которая импортируется в файл main.py и производит основные рассчеты.
  Описание работы алгоритма:
  
    1. Находим все варианты размена начальной суммы S на монеты A и B и заносим их в список l (Путем прибавления по 
    одной монете A к переменной n (n изначально равно 0), и расчета монет B, до максимально возможного значения, 
    не превышающего S). Также, находя все варианты размена, мы запоминаем остаток каждого размена, и разность между 
    заданным числом X(условием рекомендуемой доли монет A от общего числа монет) и долей монет A от всех используемых 
    монет (в процентах). 
    (Строка 5-7 в файле solve.py).
    2. Находим минимальный остаток, получающийся при всех разменах 
    (Строка 8 в файле solve.py).
    3. Зная наименьший остаток, создаем список lc, в который заносим размены с таким остатком 
    (Строка 9 в файле solve.py).
    4. Затем, в получившемся списке lc находим минимально получившуюся разницу между числом X и долей монет A от 
    общего числа монет 
    (Строка 10 в файле solve.py).
    5. Находим размен с таким числом, и получаем из него первые два числа, это и будут искомые An и Bn, количество 
    монет A и B, необходимые для размена, соответственно. Возвращаем эти значения как результат функции 
    (Строки 11-14 в файле solve.py).
    
    
Все необходимые коментарии продублированы в соответствующих файлах.
