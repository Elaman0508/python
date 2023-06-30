#1 код
# print((lambda x: (x + 3) * 5 / 2)(3))
# запуск этой лямбы-функции происходить с передачей 3 в качестве аргумента.

# 1. 15.0   *
# 2. 0
# 3. 30.0
# 4. SyntaxError



# 2код
# d



#3 код
# a = sorted([1, 2, 3])
# b = [1, 2, 3].sort()
# print(a == b)
# sort() возврашает None

# 1. True
# 2. False   *
# 3. Ошибка
# 4. None



# 4код 
# from collections.abc import Sized
# class Foo(object):
#     def __len__(self):
#         pass
# print(isinstance(Foo(), Sized))
# print(issubclass(Foo, Sized))

# 1. True True   *
# 2. True False
# 3. False False
# 4. Ошибка


#5 код
# from random import randint
# def func(x = randint(1, 10)):
#     return x
# print(func() == func())

# 1. True   *
# 2. False
# 3. Ошибка
# 4. SyntaxError




# 6 код 
# x = 7, 8, 9
# print(sorted(x) == x)
# sorted()возврашает список.Сравнения списка  скортежом вернет False

# True
# False    *
# Ошибка
# Error



# 7 код 

# x = 5.99
# print(int(x))
# int() всегда округляет в нижную сторону.

# 5    *
# 6
# Ошибка
# 5.99



# 8 код
# x = ([1,2],)
# x[0].append(3)
# print(x)
# Кортежи неизменяемы,а вот списки и другие коллекции внутри них волне могут редактировать

# ([1,2],)
# ([1,2,3],)   *
# Ошибку
# ([1,2])




# 9 код
# __debug__ = False
# if __debug__:
#     print('yes')
# else:
#     print('no')
# SyntaxError: cannot assign to __debug__

# yes
# no
# Ошибка   *
# False




#10 код
# class Foo:
#     n = 4
#     def __init__(self, n):
#         self.n = n // 2
# foo = Foo(6)
# print(foo.n)
# если есть атрибут n (self. n) то вызов вернет его если нет то вернет статическую переменную (n = 4)

# 3    *
# 4
# 6
# Ошибку


#11 код
a = -.0
b = .0
print(a == b)
# .0- вполне легальная запись для float

# True   *
# False
# Ошибку
# -.0


#12 код
s = {1, 2, 3}
print(s[1])
# {} - неиндексируеиый

# 1
# 2
# Ошибку    *
# {1,2,3}




#13
for i in range(1):
    continue
else:
    print(None)
 
#  continue никак не влияет на else в цикле

# None     *
# Ничего
# Ошибку
# 1


# 14
a = [1, 2]; b = [1, 2]
print(id(a) == id(b))
#несмотря на то что a и b - одинаковые, они изменяемые.Поэтому Python не будет приводить
# их к одному объекту как с кортежами иначе это приведет к кучу багов.

# True
# False   *
# Ошибку
# [1,2]


# 15
def nothing():
    pass
print(nothing())
#Функция всегда что-то возвращает и по умолчанию это значение None

# pass
# None     *
# Ошибку
# Error



#16
def mult_2(data):
    return type(data)(i * 2 for i in  data)
print(type(mult_2([1, 2, 3])).__name__)
#type(x) возвращает не просто информацию о классе а и сам класс с помощью 
#которого мы можем создать новый экземпляр

# generator
# list       *
# Ошибку
# Data



#17
print(issubclass(bool, int))
# bool это подкласс int.

# True    *
# False
# Ошибку 
# boll


#18 
first = [[1, 2, 3], [1, 2, 3]]
second = first.copy()
first[0][0] = 10
print(second[0])
#copy выполнаяет  лишь поверхностное

# [1,2,3]
# [10,2,3]    *
# Ошибку
# [0][0]



#19
width = 10
precision = 2
value = 12.111
x = f"{value:.{precision}f}"
print(x)
# мы можем вставлять значения для форматирования текста.В данном случае х = '{value:.2f}'. Это ограничит вывод
#чилса до двух знаков после запятой

# 12.111
# 12.11     *
# 12
# Ошибка



#20
from bisect import insort
x = [1, 4]
insort(x, 3)
insort(x, 2)
print(x)
# insort (list, value) - функция вставляющая в список с сохранением  порядка использует бинарный поиск чтобы найти мето вставки

# [1, 4]
# [1,2,3,4]   *
# [1,4,2,3]
# ошибка



#21
class Foo:
    @classmethod
    def create(cls):
        print(cls.__name__)
class Bar(Foo):
    pass
Bar.create()

# Foo
# Bar  *
# Ошибку
# None