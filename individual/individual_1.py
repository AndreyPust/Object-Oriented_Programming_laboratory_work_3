#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Man (человек), с полями: имя, возраст, пол и вес.
# Определить методы переназначения имени, изменения возраста и изменения веса.
# Создать производный класс Student, имеющий поле года обучения.
# Определить методы переназначения и увеличения года обучения.
# (Вариант 25 (5)).


class Man:
    def __init__(self, name, age, gender, weight):
        """
        Конструктор основного класса Man.

        :param name: имя человека;
        :param age: возраст человека;
        :param gender: пол человека;
        :param weight: вес человека.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def rename(self, new_name):
        """Изменяет имя человека."""
        self.name = new_name

    def change_age(self, new_age):
        """Изменяет возраст человека."""
        if new_age > 0:
            self.age = new_age
        else:
            print("Возраст должен быть положительным числом!")

    def change_weight(self, new_weight):
        """Изменяет вес человека."""
        if new_weight > 0:
            self.weight = new_weight
        else:
            print("Вес должен быть положительным числом!")


class Student(Man):
    def __init__(self, name, age, gender, weight, year_of_study):
        """
        Конструктор класса Student (наследует класс Man).

        :param name: имя;
        :param age: возраст;
        :param gender: пол;
        :param weight: вес;
        :param year_of_study: год обучения.
        """
        super().__init__(name, age, gender, weight)  # то, что унаследовали от Man
        self.year_of_study = year_of_study

    def change_year_of_study(self, new_year):
        """Изменяет год обучения студента."""
        if new_year > 0:
            self.year_of_study = new_year
        else:
            print("Год обучения должен быть положительным числом!")

    def increment_year_of_study(self):
        """Увеличивает год обучения на 1."""
        self.year_of_study += 1


if __name__ == "__main__":
    # Для примера создадим объект man
    man = Man("Иван", 30, "мужской", 75)
    print(f"Человек: {man.name}, {man.age} лет, {man.gender}, его вес: {man.weight} кг")

    man.rename("Алексей")  # Смена имени человека
    man.change_age(35)     # Смена возраста человека
    man.change_weight(80)  # Изменение веса человека
    print(f"Изменения: {man.name}, {man.age} лет, вес {man.weight} кг")

    # Для примера создадим объект класса Student
    student = Student("Ольга", 20, "женский", 55, 1)
    print(f"Студент: {student.name}, {student.age} лет, {student.gender}, вес {student.weight} кг, год обучения: "
          f"{student.year_of_study}")

    student.increment_year_of_study()
    print(f"Увеличение года обучения: Студент: {student.name}, {student.age} лет, {student.gender}, вес "
          f"{student.weight} кг, год обучения: {student.year_of_study}")

    student.change_year_of_study(4)
    print(f"Изменения года обучения: Студент: {student.name}, {student.age} лет, {student.gender}, вес "
          f"{student.weight} кг, год обучения: {student.year_of_study}")
