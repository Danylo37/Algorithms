from __future__ import annotations
from Practice8.abstracttree import AbstractTreeBonus
from Practice8.treenode import TreeNode
from Practice1.employee import Employee
from typing import Iterable


class BinarySearchTree(AbstractTreeBonus):
    __root: None | TreeNode
    __size: int

    def __init__(self, *args: Iterable[Employee] | Employee):
        self.__root = None
        self.__size = 0

        if args is not None:
            for arg in args:
                self.insert(arg)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        if self.__root is None:
            return "[]"
        return self.__tree(self.__root, 0, '')

    def __tree(self, node: TreeNode, tab: int, prefix) -> str:
        if node is None:
            return ''
        prev = self.__tree(node.left_child, tab + 2, 'l: ')
        nxt = self.__tree(node.right_child, tab + 2, 'r: ')
        return prev + ' ' * tab + prefix + str(node.value) + "\n" + nxt

    def insert(self, value: Employee) -> None:
        if self.__root is None:
            self.__root = TreeNode(value)
            self.__size += 1
        else:
            self.__insert(self.__root, value)

    def __insert(self, node: TreeNode, value: Employee):
        if value < node.value:
            if node.left_child is None:
                node.left_child = TreeNode(value)
                self.__size += 1
            else:
                self.__insert(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = TreeNode(value)
                self.__size += 1
            else:
                self.__insert(node.right_child, value)

    def find(self, value: Employee) -> bool:
        return True if self.__find(value, self.__root) else False

    def __find(self, value: Employee, node: TreeNode) -> TreeNode | None:
        if node is None:
            return None
        elif value < node.value:
            return self.__find(value, node.left_child)
        elif value > node.value:
            return self.__find(value, node.right_child)
        else:
            return node

    def remove(self, value: Employee) -> None:
        if self.find(value):
            self.__root = self.__remove(value, self.__root)
        else:
            raise ValueError("There is no such value")

    def __remove(self, value: Employee, node: TreeNode) -> TreeNode | None:
        if node is None:
            return None
        if value < node.value:
            node.left_child = self.__remove(value, node.left_child)
        elif value > node.value:
            node.right_child = self.__remove(value, node.right_child)
        else:
            if node.left_child is None and node.right_child is None:
                node = None
                self.__size -= 1
            elif node.left_child is None:
                node = node.right_child
                self.__size -= 1
            elif node.right_child is None:
                node = node.left_child
                self.__size -= 1
            else:
                min_node = self.__find_min_node(node.right_child)
                node.value = min_node.value
                node.right_child = self.__remove(min_node.value, node.right_child)
        return node

    @staticmethod
    def __find_min_node(node: TreeNode) -> TreeNode:
        while node.left_child:
            node = node.left_child
        return node

    def min(self) -> Employee:
        if self.__root is None:
            raise ValueError("Tree is empty")
        return self.__find_min_node(self.__root).value

    def clear(self) -> None:
        self.__root = None
        self.__size = 0

    def replace(self, old_value: Employee, new_value: Employee) -> None:
        if self.find(old_value):
            self.remove(old_value)
            self.insert(new_value)

    def __iter__(self):
        self.__current_node = None
        self.__stack = self.traversal()
        return self

    def __next__(self) -> Employee:
        i = 0
        while self.__stack:
            value = self.__stack.pop(i)
            i += 1
            return value
        raise StopIteration

    def extend(self, values: Iterable[Employee]) -> None:
        for value in values:
            self.insert(value)

    def count(self, value: Employee) -> int:
        count = 0
        for node_value in self:
            if node_value == value:
                count += 1
        return count

    def max(self) -> Employee:
        if self.__root is None:
            raise ValueError("Tree is empty")
        return self.__find_max_node(self.__root).value

    @staticmethod
    def __find_max_node(node: TreeNode) -> TreeNode:
        while node.right_child:
            node = node.right_child
        return node

    def __add__(self, other) -> AbstractTreeBonus | list:
        new_tree = BinarySearchTree()
        for value in self:
            new_tree.insert(value)
        for value in other:
            new_tree.insert(value)
        return new_tree

    def __mul__(self, other) -> AbstractTreeBonus | list:
        new_tree = BinarySearchTree()
        for _ in range(other):
            for value in self:
                new_tree.insert(value)
        return new_tree

    def traversal(self) -> list[Employee]:
        result = []
        self.__inorder_append(self.__root, result)
        return result

    def __inorder_append(self, node: TreeNode, result: list[Employee]) -> None:
        if node is not None:
            self.__inorder_append(node.left_child, result)
            result.append(node.value)
            self.__inorder_append(node.right_child, result)
