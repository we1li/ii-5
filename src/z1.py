#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск элемента в дереве с использованием алгоритма итеративного углубления

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        # Инициализация узла дерева
        self.value = value   # Значение узла
        self.left = left     # Левый потомок
        self.right = right   # Правый потомок

    def add_children(self, left, right):
        # Добавление левого и правого потомков
        self.left = left
        self.right = right

    def __repr__(self):
        # Представление узла дерева (для удобства вывода)
        return f"<{self.value}>"

def depth_limited_search(node, goal, limit):
    # Функция поиска в глубину с ограничением по глубине
    if limit < 0:
        # Если предел глубины меньше нуля, возвращаем "cutoff" (ограничение)
        return "cutoff"
    if node is None:
        # Если узел пустой, возвращаем None
        return None
    if node.value == goal:
        # Если текущий узел содержит искомое значение, возвращаем True
        return True

    # Рекурсивный вызов для левого поддерева с уменьшением глубины
    left_result = depth_limited_search(node.left, goal, limit - 1)
    if left_result is True:
        # Если результат поиска в левом поддереве положительный, возвращаем True
        return True
    elif left_result == "cutoff":
        # Если было достигнуто ограничение глубины в левом поддереве, сохраняем "cutoff"
        cutoff = "cutoff"
    else:
        cutoff = None

    # Рекурсивный вызов для правого поддерева с уменьшением глубины
    right_result = depth_limited_search(node.right, goal, limit - 1)
    if right_result is True:
        # Если результат поиска в правом поддереве положительный, возвращаем True
        return True
    elif right_result == "cutoff":
        # Если было достигнуто ограничение глубины в правом поддереве, сохраняем "cutoff"
        cutoff = "cutoff"

    # Если ни одно из поддеревьев не дало положительный результат, возвращаем "cutoff" или None
    return cutoff

def iterative_deepening_search(root, goal):
    # Функция итеративного углубления
    max_depth = 10  # Максимальная глубина для поиска
    for limit in range(max_depth):
        # Проходим по всем уровням глубины от 0 до max_depth - 1
        result = depth_limited_search(root, goal, limit)
        if result is True:
            # Если решение найдено, возвращаем True
            return True
        elif result is None:
            # Если на текущем уровне не найдено решения, завершаем поиск
            break
    # Если решение не найдено после всех итераций, возвращаем False
    return False

if __name__ == "__main__":
    # Построение дерева
    root = BinaryTreeNode(1)  # Корень дерева
    left_child = BinaryTreeNode(2)  # Левый потомок
    right_child = BinaryTreeNode(3)  # Правый потомок
    root.add_children(left_child, right_child)  # Присваиваем потомков корню
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))  # Добавляем потомков правому узлу

    # Целевое значение для поиска
    goal = 4

    # Проверка существования узла с заданным значением
    exists = iterative_deepening_search(root, goal)
    print(exists)  # Выводим результат: True, если найдено, False если нет
