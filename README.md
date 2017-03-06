Задание:

Задачи по Python

1 Написать программу с использованием декораторов которая принимает целое число и затем несколько строк со следующей структурой: имя фамилия, возраст, пол. И возвращает список с
обращениями (Г-н, Г-жа) отсортированный по возрасту. Если возраст одинаковый —
сохраняется порядок ввода.

Пример:

ввод:

4

Иван Петров М 34

Сергей Терехов М 25

Александра Кац Ж 23

Семен Бурденко М 25

Вывод

Г-жа Александра Кац

Г-н Сергей Терехов

Г-н Семен Бурденко

Г-н Иван Петров

Ввод с клавиатуры либо с указанием файла содержащего текст.


2 Программа читает 2 массива. Первый массив — список строк Х. Второй массив — запросы У.
По каждому запросу У программа подсчитывает сколько раз эта строка встречается среди
элементов Х. По каждой У выводится количество в Х.

Формат ввода или файла:

1 строка — количество элементов Х.

Следующие Х строк — строки по одной

Следующая строка — количество запросов У

Следующие У строк — запросы по одному в строке

Пример:

Ввод:

6

икс

зэт

альфа

варо

икс

икс

3

икс

зэт

вап


Вывод:

3

1

0

Ввод с клавиатуры либо с указанием файла содержащего текст.


Для выполнения задания 3:

Установить odoo на свой компьютер. (любой вариант)

Изучить курс Building a module по адресу:
https://www.odoo.com/documentation/9.0/howtos/backend.html

3. Написать модуль Test который при установке создает:
- Меню Test и два подменю Tests и Test sessions.
- Создать 2 модели test и test session со следующими полями:
test – поля test name (string), test purpose (text), tester (поле ссылающееся на таблицу
res.partners связь Many2One),
test session – поля test (ссылка на модель test) start date, end date, duration(вычисляемое на
основе дат)
- Создать унаследованное отображение формы (form view) для модели res.Partner в
котором добавлено поле isTester недоступное для редактирования. Поле устанавливается
в значение истина если есть хоть один тест в котором участвует данный партнер.
- Создать унаследованные отображения списка и поиска для модели res.Partner в котором
добавить фильтр отображающий только тех партнеров у которых ожидаются тесты в
ближайшие 30 дней.