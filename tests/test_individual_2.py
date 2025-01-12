#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from src.individual_2 import (Ellipse, Function, Hyperbola,
                              display_function_result,)


class TestFunctionClasses(unittest.TestCase):
    """Тесты для классов Ellipse и Hyperbola."""

    def test_ellipse_calculate_y_valid(self):
        """Проверка корректного вычисления y для эллипса при допустимом x."""
        ellipse = Ellipse(a=5, b=3)
        y = ellipse.calculate_y(3)
        self.assertAlmostEqual(y, 2.4, places=2)

    def test_ellipse_calculate_y_invalid(self):
        """Проверка выброса исключения при недопустимом x для эллипса."""
        ellipse = Ellipse(a=5, b=3)
        with self.assertRaises(ValueError):
            ellipse.calculate_y(6)  # x больше a

    def test_hyperbola_calculate_y_valid(self):
        """Проверка корректного вычисления y для гиперболы при допустимом x."""
        hyperbola = Hyperbola(a=4, b=2)
        y = hyperbola.calculate_y(5)
        self.assertAlmostEqual(y, 1.5, places=2)

    def test_hyperbola_calculate_y_invalid(self):
        """Проверка выброса исключения при недопустимом x для гиперболы."""
        hyperbola = Hyperbola(a=4, b=2)
        with self.assertRaises(ValueError):
            hyperbola.calculate_y(3)  # x меньше a

    def test_ellipse_display_result(self):
        """Проверка корректного вывода результата для эллипса."""
        ellipse = Ellipse(a=5, b=3)
        with patch("builtins.print") as mock_print:
            ellipse.display_result(3)
            mock_print.assert_called_once_with("Эллипс: при x = 3, y = ±2.40")

    def test_hyperbola_display_result(self):
        """Проверка корректного вывода результата для гиперболы."""
        hyperbola = Hyperbola(a=4, b=2)
        with patch("builtins.print") as mock_print:
            hyperbola.display_result(5)
            mock_print.assert_called_once_with("Гипербола: при x = 5, y = ±1.50")

    def test_virtual_call(self):
        """Проверка виртуального вызова через базовый класс Function."""
        ellipse = Ellipse(a=5, b=3)
        hyperbola = Hyperbola(a=4, b=2)

        with patch("builtins.print") as mock_print:
            display_function_result(ellipse, 3)
            mock_print.assert_any_call("Эллипс: при x = 3, y = ±2.40")

        with patch("builtins.print") as mock_print:
            display_function_result(hyperbola, 5)
            mock_print.assert_any_call("Гипербола: при x = 5, y = ±1.50")

    def test_abstract_class_instantiation(self):
        """Проверка невозможности создания экземпляра абстрактного класса Function."""
        with self.assertRaises(TypeError):
            Function()


if __name__ == "__main__":
    unittest.main()
