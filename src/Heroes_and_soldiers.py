#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


# В некой игре-стратегии есть солдаты и герои.
# У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде.
# У солдат есть метод «иду за героем»,
# который в качестве аргумента принимает объект типа «герой».
# У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды.
# В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран.
# У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним.
# Выведите на экран идентификационные номера этих двух юнитов.


class Unit:
    """
    Базовый класс для всех юнитов игры.
    """

    def __init__(self, unique_id, species):
        """
        Конструктор класса Юнит.

        :param unique_id: ID юнита, должен быть уникальным и для солдат и для героев.
        :param species: Принадлежность юнита команде (имя команды).
        """
        self.unique_id = unique_id
        self.team = species


class Hero(Unit):
    """
    Класс Герой, который наследует класс Unit(Юнит), так как сам тоже является юнитом.
    """

    def __init__(self, unique_id, species):
        """
        Конструктор класса герой.

        :param unique_id: ID героя.
        :param species: Принадлежность героя команде (имя команды).
        """

        super().__init__(unique_id, species)
        self.level = 1  # Начальный уровень героя

    def increase_level(self):
        """
        Метод, отвечающий за повышения уровня героя.
        """

        self.level += 1
        print(f"Герой {self.unique_id}, принадлежащий расе {self.team} повышается до {self.level} уровня.")


class Soldier(Unit):
    """
    Класс Солдат, стандартный юнит игры, поэтому тоже наследует класс Unit(Юнит).
    Конструктор класса полностью наследуется из класса Unit.
    """

    def follow_the_hero(self, hero):
        """
        Метод, отвечающий за следование зе героем.

        :param hero: Герой, за которым нужно следовать.
        """

        print(f"Солдат {self.unique_id} идет за героем {hero.unique_id} расы {hero.team}.")


if __name__ == "__main__":
    # Создаем героев для двух команд
    hero1 = Hero(unique_id=1, species="Альянс")
    hero2 = Hero(unique_id=2, species="Нежить")

    # Списки солдат для команд
    team_alliance_soldiers = []
    team_undead_soldiers = []

    # Генерация солдат
    for i in range(1, 201):  # пусть будет 200 солдат (по 100 единиц для каждой команды в идеале)
        team = random.choice(["Альянс", "Нежить"])
        soldier = Soldier(unique_id=i, species=team)
        if team == "Альянс":
            team_alliance_soldiers.append(soldier)
        else:
            team_undead_soldiers.append(soldier)

    # Вывод численности солдат команд
    print(f"Раса Альянс, численность: {len(team_alliance_soldiers)} солдат.")
    print(f"Раса Нежить, численность: {len(team_undead_soldiers)} солдат.")

    # Определение команды с более длинным списком
    if len(team_alliance_soldiers) > len(team_undead_soldiers):
        hero1.increase_level()
    elif len(team_undead_soldiers) > len(team_alliance_soldiers):
        hero2.increase_level()
    else:
        print("Количество солдат обеих рас одинаково, уровни героев не увеличиваются.")

    # Отправляем одного из солдат первого героя следовать за ним
    if team_alliance_soldiers:  # Проверяем, есть ли солдаты у расы Альянс
        soldier = team_alliance_soldiers[0]
        soldier.follow_the_hero(hero1)
        print(
            f"Идентификаторы: Солдат с id={soldier.unique_id}, "
            f"идет за героем с id={hero1.unique_id} расы {hero1.team}."
        )
    else:
        print("У расы Альянс нет солдат для выполнения команды.")
