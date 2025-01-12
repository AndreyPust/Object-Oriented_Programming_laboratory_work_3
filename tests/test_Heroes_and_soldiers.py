#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from src.Heroes_and_soldiers import Hero, Soldier


class TestGameUnits(unittest.TestCase):
    """Тесты для классов Hero и Soldier."""

    def test_hero_initialization(self):
        """Проверка корректной инициализации героя."""
        hero = Hero(unique_id=1, species="Альянс")
        self.assertEqual(hero.unique_id, 1)
        self.assertEqual(hero.team, "Альянс")
        self.assertEqual(hero.level, 1)

    def test_soldier_initialization(self):
        """Проверка корректной инициализации солдата."""
        soldier = Soldier(unique_id=10, species="Нежить")
        self.assertEqual(soldier.unique_id, 10)
        self.assertEqual(soldier.team, "Нежить")

    def test_hero_increase_level(self):
        """Проверка увеличения уровня героя."""
        hero = Hero(unique_id=1, species="Альянс")
        hero.increase_level()
        self.assertEqual(hero.level, 2)

    @patch("builtins.print")
    def test_soldier_follow_the_hero(self, mock_print):
        """Проверка выполнения солдатом команды следовать за героем."""
        hero = Hero(unique_id=1, species="Альянс")
        soldier = Soldier(unique_id=2, species="Альянс")
        soldier.follow_the_hero(hero)
        mock_print.assert_called_with("Солдат 2 идет за героем 1 расы Альянс.")

    def test_team_allocation(self):
        """Проверка распределения солдат между командами."""
        soldiers = [Soldier(unique_id=i, species="Альянс" if i % 2 == 0 else "Нежить") for i in range(1, 11)]
        team_alliance = [s for s in soldiers if s.team == "Альянс"]
        team_undead = [s for s in soldiers if s.team == "Нежить"]

        self.assertEqual(len(team_alliance), 5)
        self.assertEqual(len(team_undead), 5)

    @patch("builtins.print")
    def test_hero_level_up_condition(self, mock_print):
        """Проверка увеличения уровня героя команды с большим числом солдат."""
        hero1 = Hero(unique_id=1, species="Альянс")
        hero2 = Hero(unique_id=2, species="Нежить")

        team_alliance = [Soldier(unique_id=i, species="Альянс") for i in range(10)]
        team_undead = [Soldier(unique_id=i, species="Нежить") for i in range(8)]

        if len(team_alliance) > len(team_undead):
            hero1.increase_level()
        elif len(team_undead) > len(team_alliance):
            hero2.increase_level()

        self.assertEqual(hero1.level, 2)
        self.assertEqual(hero2.level, 1)
        mock_print.assert_called_with("Герой 1, принадлежащий расе Альянс повышается до 2 уровня.")

    @patch("builtins.print")
    def test_no_soldiers_follow(self, mock_print):
        """Проверка поведения, если у команды нет солдат."""
        hero1 = Hero(unique_id=1, species="Альянс")
        team_alliance = []

        if team_alliance:
            soldier = team_alliance[0]
            soldier.follow_the_hero(hero1)
        else:
            print("У расы Альянс нет солдат для выполнения команды.")

        mock_print.assert_called_with("У расы Альянс нет солдат для выполнения команды.")


if __name__ == "__main__":
    unittest.main()
