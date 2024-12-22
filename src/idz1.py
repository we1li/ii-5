#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib


class TreeNode:
    """
    Класс для представления узла дерева файловой системы.
    """
    def __init__(self, path):
        self.path = path
        self.children = []

    def add_child(self, child):
        """
        Добавление дочернего узла.
        """
        self.children.append(child)

    def __repr__(self):
        return f"<{self.path}>"


def get_file_hash(file_path):
    """
    Вычисляет хэш содержимого файла для сравнения.
    :param file_path: Путь к файлу.
    :return: Хэш файла в виде строки.
    """
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Чтение файла по 8 KB
                hasher.update(chunk)
        return hasher.hexdigest()
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        return None


def iterative_deepening_file_search(root, depth_limit):
    """
    Поиск дублирующихся файлов в файловом дереве с использованием итеративного углубления.
    :param root: Корневой узел дерева.
    :param depth_limit: Максимальная глубина поиска.
    :return: Список пар путей дублирующихся файлов.
    """
    for depth in range(depth_limit + 1):
        print(f"Проверка на глубине: {depth}")
        duplicates = depth_limited_search(root, {}, depth)
        if duplicates:
            return duplicates
    return []


def depth_limited_search(node, file_hashes, depth):
    """
    Ограниченный по глубине поиск дублирующихся файлов.
    :param node: Текущий узел дерева.
    :param file_hashes: Словарь для хранения хэшей файлов и их путей.
    :param depth: Оставшаяся глубина поиска.
    :return: Список пар путей дублирующихся файлов.
    """
    if depth < 0:
        return []

    duplicates = []
    if os.path.isfile(node.path):  # Проверяем, является ли узел файлом
        file_hash = get_file_hash(node.path)
        if file_hash:
            if file_hash in file_hashes:
                duplicates.append((file_hashes[file_hash], node.path))
            else:
                file_hashes[file_hash] = node.path
    else:  # Если узел - каталог, рекурсивно обходим дочерние узлы
        for child in node.children:
            duplicates.extend(depth_limited_search(child, file_hashes, depth - 1))

    return duplicates


def build_file_tree(root_path):
    """
    Построение дерева файловой системы.
    :param root_path: Корневой путь.
    :return: Корневой узел дерева файловой системы.
    """
    root = TreeNode(root_path)
    try:
        for entry in os.scandir(root_path):
            if entry.is_dir(follow_symlinks=False):
                root.add_child(build_file_tree(entry.path))
            elif entry.is_file(follow_symlinks=False):
                root.add_child(TreeNode(entry.path))
    except PermissionError:
        pass  # Игнорируем каталоги без прав доступа
    return root


if __name__ == '__main__':
    # Задаем корневой каталог и глубину поиска
    root_directory = "/content/test"
    max_depth = 10

    # Строим дерево файловой системы
    root_node = build_file_tree(root_directory)

    # Запускаем поиск дубликатов
    duplicates = iterative_deepening_file_search(root_node, max_depth)

    # Вывод результатов
    if duplicates:
        print("Найдены дублирующиеся файлы:")
        for file1, file2 in duplicates:
            print(f"{file1} <-> {file2}")
    else:
        print("Дублирующихся файлов не найдено.")
