# def function_name(arguments): - создание функции
# lambda arg: - создание анонимной функции
# return - вернуть результат функции
# *args - любое количество элементов
# * - распаковка
# **kwargs - любое количество именованных элементов
# ** - распаковка с именем

# map(func, list) - применить функцию к каждому элементу списка
# filter(func, list) - отфильтровать элементы списка

# class Name(Parent): - создание класса
# def __init__(self, *args) - инициализация класса

# eval() - вычислить значение выражения


# class Animal:
#     def __init__(self, voice: str):
#         self.voice = voice
#         self.is_sleeping = True
#
#     def speak(self) -> str:
#         return self.voice
#
#     def sleep(self, s: bool):
#         self.is_sleeping = s
#
#
# class Cat(Animal):
#     def __init__(self, voice: str, size: int):
#         super().__init__(voice)
#         self.size = size
#
#     def is_big(self) -> str:
#         if self.size > 5:
#             return 'Big'
#         else:
#             return 'Small'
#


# ДЗ:

# 1. Напишите функцию, которая создаёт прогрессию. Вам будет дан первый член прогрессии, знаменатель прогрессии,
# вид прогрессии, и номер цифры, которую вам надо высчитать.
# progression(1, 3, '+', 4) => 10
# + - алгебраическая прогрессия
# progression(3, 2, '*', 5) => 48
# * - геометрическая прогрессия


# 2. Напишите функцию, которая принимает предложение и определяет, заикается ли человек. Человек заикается,
# если в предложении есть хотя бы одно слово, за которым идёт слово, содержащее в начале первое слово.
# stutter('Я люблю ре решать задачки') => true //ре - решать
# stutter('Мои любимые тны животные - собаки') => false //тны - НЕ начало слова животные


# 3. Создайте класс объекта обыкновенной дроби. Он поддерживает все базовые математические методы (+, -, *, /)
# с другими экземплярами объекта дроби, а также метод, который переводит обыкновенную дробь в десятичную дробь
# Например:
# fraction1 = Fraction(3, 5)
# fraction2 = Fraction(1, 3)
# fraction1.add(fraction2) = '14/15'
# fraction1.substract(fraction2) = '4/15'
# fraction1.multiply(fraction2) = '3/15'
# fraction1.divide(fraction2) = '1 4/5'
# fraction1.to_decimal() = 0.6
