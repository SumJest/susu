## Задача №113662. Форум. Вывести путь

Дано количество сообщений на некотором форуме (**N** натуральное, не более **1000**).

Также таблица, в которой указано какие сообщения на каком уровне находятся.

В первой колонке таблицы написаны номера сообщений (натуральные числа, не превосходят **1 000 000**).

Во второй колонке напротив номера сообщения стоит либо 0, если сообщение является корнем (началом) некоторой темы, либо номер того сообщения, ответом на которое является текущее.

Пример. Следующие исходные данные:

```
4
1 0 
2 0
3 1
4 3
```

соответствуют такой структуре форума:

![](https://informatics.msk.ru/moodle_probpics/113659/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA.PNG)

Гарантируется что данные во втором столбце корректны (то есть в качестве «родительского» может быть указано только существующее сообщение, а также что структура не имеет циклов и что от любого сообщения есть путь к «корню» форума).  
Вывести весь «путь» от корня форума до сообщения номер **A** включительно, номера сообщений разделять знаком ‘#’ (решетка).

###### Входные данные
Сначала вводится натуральное число **N** (не превышает **1000**) – общее количество сообщений на форуме.

Затем вводится **N** строк таблицы, по **2** числа на строке – номер текущего сообщения и номер того сообщения, ответом на которое является текущее (или **0**).

В последней строке вводится число **A** - номер сообщения. Гарантируется, что сообщение с такими номером существует.

###### Выходные данные
Выведите строку, которая описывает полный путь от корня форума (включая начальное число **0**) до сообщения номер **A**.

###### Примеры

|входные данные |
| ------------ |
| 1 <br /> 1 0 <br /> 1  |
| **выходные данные** |
|  0#1  |

|входные данные |
| ------------ |
| 3 <br /> 1 0 <br /> 4 1 <br /> 10 1 <br />4 |
| **выходные данные** |
|  0#1#4  |