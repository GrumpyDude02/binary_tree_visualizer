from Node import Node
from pygame.math import Vector2 as vc


class binary_tree:
    def __init__(self, data, x, y, dx):
        self.root = Node(data, vc(x, y), dx)
        self.nodes = [self.root]
        self.number_of_elements = 1

    def add_node(self, data):
        new = self.root.insert__(data)
        if new:
            self.nodes.append(new)
            self.number_of_elements += 1

    def tree_pos(self):
        self.root.SetPos(None, False)

    def draw_tree(self, screen, radius):
        for node in self.nodes:
            node.draw_node(screen, radius)
