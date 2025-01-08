#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from abc import ABC, abstractmethod


# Создать абстрактный базовый класс Function (функция) с виртуальными методами вычисления
# значения функции y = f(x) в заданной точке x и вывода результата на экран.
# Определить производные классы Ellipse (эллипс), Hyperbola (гипербола)
# с собственными функциями вычисления y в зависимости от входного параметра x.
# Уравнение эллипса: x^2 / a^2 + y^2 / b^2 = 1;
# гиперболы: x^2 / a^2 – y^2 / b^2 = 1.
# (Вариант 25 (8)).


class Function(ABC):
    """Абстрактный базовый класс Function."""

    @abstractmethod
    def calculate_y(self, x):
        """
        Абстрактный метод для вычисления y = f(x).
        Он должен быть переопределен в производных классах.
        """
        pass

    @abstractmethod
    def display_result(self, x):
        """
        Абстрактный метод для вывода результата на экран.
        Он также должен быть переопределен в производных классах.
        """
        pass


class Ellipse(Function):
    """Класс для вычисления значения функции по уравнению эллипса."""

    def __init__(self, a, b):
        """
        Инициализация эллипса с полуосями a и b (коэффициенты).
        """
        self.a = a
        self.b = b

    def calculate_y(self, x):
        """
        Вычисление y на основе уравнения эллипса:
        x^2 / a^2 + y^2 / b^2 = 1.
        Метод, который переопределяет метод из абстрактного класса.
        """

        if abs(x) > self.a:
            raise ValueError("Значение x выходит за границы эллипса (|x| <= a).")
        return self.b * math.sqrt(1 - (x**2) / (self.a**2))

    def display_result(self, x):
        """Вывод результата на экран, переопределение метода вывода абстрактного класса."""
        try:
            y = self.calculate_y(x)
            print(f"Эллипс: при x = {x}, y = ±{y:.2f}")
        except ValueError as e:
            print(f"Ошибка: {e}")


class Hyperbola(Function):
    """Класс для вычисления значения функции по уравнению гиперболы."""

    def __init__(self, a, b):
        """
        Инициализация гиперболы с полуосями a и b.
        """
        self.a = a
        self.b = b

    def calculate_y(self, x):
        """
        Вычисление y на основе уравнения гиперболы:
        x^2 / a^2 - y^2 / b^2 = 1.
        Метод, который переопределяет метод из абстрактного класса.
        """
        if abs(x) < self.a:
            raise ValueError("Значение x должно быть больше или равно a (|x| >= a).")
        return self.b * math.sqrt((x**2) / (self.a**2) - 1)

    def display_result(self, x):
        """Вывод результата на экран."""
        try:
            y = self.calculate_y(x)
            print(f"Гипербола: при x = {x}, y = ±{y:.2f}")
        except ValueError as e:
            print(f"Ошибка: {e}")


def display_function_result(function_obj, x):
    """
    Функция для демонстрации виртуального вызова.
    Получает объект базового класса Function по ссылке
    и вызывает его методы.
    """
    function_obj.display_result(x)


if __name__ == "__main__":
    # Создаем объекты классов и устанавлюваем в качестве атрибутов значения коэффициентов
    ellipse = Ellipse(a=5, b=3)
    hyperbola = Hyperbola(a=4, b=2)

    # Вызов методов напрямую (невиртуально)
    print("Прямой вызов методов:")
    ellipse.display_result(3)
    hyperbola.display_result(5)

    # Виртуальный вызов методов (через функцию display_function_result)
    print("\nВиртуальный вызов через базовый класс:")
    display_function_result(ellipse, 3)
    display_function_result(hyperbola, 5)

    # Примеры ошибок
    print("\nОбработка ошибок:")
    ellipse.display_result(6)  # Выход за границы эллипса
    hyperbola.display_result(3)  # Выход за границы гиперболы
    # abstract_function = Function()  # Попытка создать объект абстрактного класса Function, вызовет ошибку
