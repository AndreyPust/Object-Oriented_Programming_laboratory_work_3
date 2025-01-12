#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.individual_1 import Man, Student


class TestMan(unittest.TestCase):
    """Тесты для класса Man."""

    def test_initialization(self):
        """Проверка корректной инициализации объекта Man."""
        man = Man("Иван", 30, "мужской", 75)
        self.assertEqual(man.name, "Иван")
        self.assertEqual(man.age, 30)
        self.assertEqual(man.gender, "мужской")
        self.assertEqual(man.weight, 75)

    def test_rename(self):
        """Проверка метода смены имени."""
        man = Man("Иван", 30, "мужской", 75)
        man.rename("Алексей")
        self.assertEqual(man.name, "Алексей")

    def test_change_age_valid(self):
        """Проверка изменения возраста на корректное значение."""
        man = Man("Иван", 30, "мужской", 75)
        man.change_age(35)
        self.assertEqual(man.age, 35)

    def test_change_age_invalid(self):
        """Проверка изменения возраста на некорректное значение."""
        man = Man("Иван", 30, "мужской", 75)
        man.change_age(-5)
        self.assertEqual(man.age, 30)  # Возраст не должен измениться

    def test_change_weight_valid(self):
        """Проверка изменения веса на корректное значение."""
        man = Man("Иван", 30, "мужской", 75)
        man.change_weight(80)
        self.assertEqual(man.weight, 80)

    def test_change_weight_invalid(self):
        """Проверка изменения веса на некорректное значение."""
        man = Man("Иван", 30, "мужской", 75)
        man.change_weight(-10)
        self.assertEqual(man.weight, 75)  # Вес не должен измениться


class TestStudent(unittest.TestCase):
    """Тесты для класса Student."""

    def test_initialization(self):
        """Проверка корректной инициализации объекта Student."""
        student = Student("Ольга", 20, "женский", 55, 1)
        self.assertEqual(student.name, "Ольга")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.gender, "женский")
        self.assertEqual(student.weight, 55)
        self.assertEqual(student.year_of_study, 1)

    def test_change_year_of_study_valid(self):
        """Проверка изменения года обучения на корректное значение."""
        student = Student("Ольга", 20, "женский", 55, 1)
        student.change_year_of_study(3)
        self.assertEqual(student.year_of_study, 3)

    def test_change_year_of_study_invalid(self):
        """Проверка изменения года обучения на некорректное значение."""
        student = Student("Ольга", 20, "женский", 55, 1)
        student.change_year_of_study(-1)
        self.assertEqual(student.year_of_study, 1)  # Год обучения не должен измениться

    def test_increment_year_of_study(self):
        """Проверка увеличения года обучения на 1."""
        student = Student("Ольга", 20, "женский", 55, 1)
        student.increment_year_of_study()
        self.assertEqual(student.year_of_study, 2)


if __name__ == "__main__":
    unittest.main()
