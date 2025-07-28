r"""
Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.

"""

#so level order traversal, then remove the sibling?

function findCousins(root, target):
    if root is None or root == target:
        return []

    queue = [(None, root)]   # each element is (parent, node)
    found = False
    target_parent = None

    while queue and not found:
        level_size = len(queue)
        next_level = []

        for i in 0 to level_size - 1:
            parent, node = queue.pop(0)

            if node == target:
                found = True
                target_parent = parent

            if node.left:
                next_level.append((node, node.left))
            if node.right:
                next_level.append((node, node.right))

        if found:
            # Now process next_level to get cousins
            cousins = []
            for parent, node in next_level:
                if parent != target_parent:
                    cousins.append(node)
            return cousins

        queue = next_level

    return []  # target not found or no cousins
