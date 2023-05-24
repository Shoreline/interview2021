# https://leetcode.com/discuss/interview-question/1367130/Doordash-Phone-Interview

class Node:
    def __init__(self, key, value, is_active):
        self.key = key
        self.value = value
        self.isActive = is_active
        self.children = []

    # Only compare k, v and is_active. Ignore children.
    def equals(self, node: 'Node'):
        if node is None:
            return False

        return self.key == node.key and self.value == node.value and self.isActive == node.isActive


# Since the in the given Node class, children is a list. So for search efficiency we convert it into a key-node map.
def get_children_map(menu: 'Node'):
    m = {}
    if menu is None:
        return m

    for node in menu.children:
        m[node.key] = node

    return m


def get_modified_items(oldMenu, newMenu):
    if oldMenu is None and newMenu is None:
        return 0

    count = 0

    # First compare the given two nodes: new and old.
    if oldMenu is None or newMenu is None or not oldMenu.equals(newMenu):
        count += 1

    # Then recursively check children nodes
    children_old = get_children_map(oldMenu)
    children_new = get_children_map(newMenu)

    for k in children_old.keys():
        count += get_modified_items(children_old.get(k), children_new.get(k))

    for k in children_new.keys():
        if k not in children_old:   # check the remaining nodes not in old_menu's children list.
            count += get_modified_items(None, children_new.get(k))

    return count


a1 = Node("a", 1, True)
b1 = Node("b", 2, True)
c1 = Node("c", 3, True)
d1 = Node("d", 4, True)
e1 = Node("e", 5, True)
# f1 = Node("f", 6, True)
# g1 = Node("g", 7, True)
a1.children.append(b1)
a1.children.append(c1)
b1.children.append(d1)
b1.children.append(e1)
# c1.children.append(f1)
# c1.children.append(g1)

a2 = Node("a", 1, True)
b2 = Node("b", 2, True)
c2 = Node("c", 3, True)
d2 = Node("d", 4, True)
e2 = Node("e", 5, True)
# f2 = Node("f", 6, True)
# g2 = Node("g", 7, False)
a2.children.append(b2)
a2.children.append(c2)
b2.children.append(d2)
# b2.children.append(f2)
c2.children.append(e2)
# c2.children.append(g2)

# case 1 (without including commented code) - nodes changed are b and c; count = 2
# case 2 (after including commented code) - nodes changed are b, c, e, f and g; count = 5

print(get_modified_items(a1, a2))
