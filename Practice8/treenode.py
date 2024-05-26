from __future__ import annotations
from Practice1.employee import Employee


class TreeNode:
    value: Employee
    left_child: None | TreeNode
    right_child: None | TreeNode

    def __init__(self, value, left_child: TreeNode | None = None, right_child: TreeNode | None = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self) -> str:
        return f"TreeNode(value:{self.value}, " \
               f"left:{self.left_child is not None}," \
               f" right:{self.left_child is not None})"
