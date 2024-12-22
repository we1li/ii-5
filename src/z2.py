#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BinaryTreeNode:
    """
    Класс для представления узла бинарного дерева.
    """
    def __init__(self, value, left=None, right=None):
        """
        Инициализация узла дерева.
        :param value: Значение узла.
        :param left: Левый дочерний узел.
        :param right: Правый дочерний узел.
        """
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        """
        Добавляет левого и правого дочерних узлов.
        :param left: Левый дочерний узел.
        :param right: Правый дочерний узел.
        """
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Возвращает строковое представление узла.
        """
        return f"<{self.value}>"


def iterative_deepening_search(root, goal):
    """
    Реализация алгоритма итеративного углубления для поиска элемента в дереве.
    :param root: Корень дерева.
    :param goal: Целевое значение, которое нужно найти.
    :return: True, если целевое значение найдено, иначе False.
    """
    depth = 0
    while True:  # Постепенно увеличиваем глубину поиска
        print(f"Проверка на глубине: {depth}")
        found = depth_limited_search(root, goal, depth)
        if found:  # Если цель найдена, возвращаем результат
            return True
        depth += 1  # Увеличиваем глубину поиска


def depth_limited_search(node, goal, limit):
    """
    Поиск элемента с ограничением по глубине.
    :param node: Текущий узел.
    :param goal: Целевое значение.
    :param limit: Ограничение по глубине поиска.
    :return: True, если целевое значение найдено, иначе False.
    """
    if node is None:
        return False
    if node.value == goal:  # Если найдено целевое значение
        print(f"Найдено: {node.value}")
        return True
    if limit <= 0:  # Если достигли ограничения глубины
        return False

    # Рекурсивно ищем в левом и правом поддеревьях
    return (depth_limited_search(node.left, goal, limit - 1) or
            depth_limited_search(node.right, goal, limit - 1))


if __name__ == '__main__':
    # Создание дерева и установка значений
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    # Целевое значение
    goal = 4

    # Вызов функции итеративного углубления
    if iterative_deepening_search(root, goal):
        print("Целевое значение найдено.")
    else:
        print("Целевое значение не найдено.")
