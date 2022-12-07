from typing import List


class Node:
    def __init__(self, name: str, value, childs: list, parent) -> None:
        self.name = name
        self.value = value
        self.childs = childs
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name}({self.value}) -> {self.childs}"

    def add_child(self, child) -> None:
        self.childs.append(child)

    def has_child(self, name) -> bool:
        matches = [c for c in self.childs if c.name == name]
        return len(matches) > 0


def create_node(parent, name, value) -> Node:
    return Node(name, value, [], parent)


def get_all_values_by_name(node: Node, name) -> list:

    values = []
    if node.name == name:
        values.append(node.value)

    for c in node.childs:
        values += get_all_values_by_name(c, name)

    return values


def get_all_values_not_by_name(node: Node, name) -> list:

    values = []
    if node.name != name:
        values.append(node.value)

    for c in node.childs:
        values += get_all_values_by_name(c, name)

    return values
