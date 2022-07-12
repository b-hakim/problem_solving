class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

"""
  //==========================================
  //               height
  //==========================================
  // height(T) returns the height of tree T.
  //
  // Requirement: If T is nonempty, then the
  // ht field has already been set correctly
  // T.
  //==========================================
"""
def height(tree):
    if tree is None:
        return 0
    return tree.height

"""
  //==========================================
  //               installHeight
  //==========================================
  // installHeight(T) sets T->ht to the
  // height of T.
  //
  // Requirements:
  //   (1) T is not empty.
  //   (2) The ht field has already been set
  //       correctly in every node of each
  //       subtree of T.
  //==========================================
"""
def install_height(tree):
    if tree is None:
        return
    tree.height = 1 + max(height(tree.left), height(tree.right))

"""
  //==========================================
  //              singleRotateLeft
  //==========================================
  // singleRotateLeft(T) performs a single
  // rotation from right to left at the
  // root of T.
  //==========================================
"""
def single_rotate_left(tree):
    # idea: the tree.right.left will be the right-child of the tree.left
    # then the tree.right will be the new-root
    # then the old-root will be the left of the new-root, hence the rotate left name
    new_root = tree.right
    tree.right = tree.right.left
    install_height(tree)

    new_root.left = tree
    install_height(new_root)
    return new_root
"""
  //==========================================
  //              singleRotateRight
  //==========================================
  // singleRotateRight(T) performs a single
  // rotation from left to right at the
  // root of T.
  //==========================================
"""
def single_rotate_right(tree):
    new_root = tree.left
    tree.left = tree.left.right
    install_height(tree)

    new_root.right = tree
    install_height(new_root)
    return new_root

"""
  //==========================================
  //              doubleRotateLeft
  //==========================================
  // doubleRotateLeft(T) performs a double
  // rotation from right to left at the
  // root of T.
  //==========================================
"""

def double_rotate_left(tree):
    tree.right = single_rotate_right(tree.right)
    tree = single_rotate_left(tree)
    return tree

"""
  //==========================================
  //              doubleRotateRight
  //==========================================
  // doubleRotateRight(T) performs a double
  // rotation from left to right at the
  // root of T.
  //==========================================
"""

def double_rotate_right(tree):
    tree.left = single_rotate_left(tree.left)
    tree = single_rotate_right(tree)
    return tree

"""
  //==========================================
  //              rotateLeft
  //==========================================
  // rotateLeft(T) performs a rotation from
  // from right to left at the root of T, 
  // choosing a single or double rotation.
  //==========================================
"""
def rotate_left(tree):
    hl = height(tree.right.left)
    hr = height(tree.right.right)

    if hl<hr:
        tree = single_rotate_left(tree)
    else:
        tree = double_rotate_left(tree)

    return tree

"""
  //==========================================
  //              rotateRight
  //==========================================
  // rotateRight(T) performs a rotation from
  // from left to right at the root of T, 
  // choosing a single or double rotation.
  //==========================================
"""
def rotate_right(tree):
    hl = height(tree.left.left)
    hr = height(tree.left.right)

    if hl>hr:
        tree = single_rotate_right(tree)
    else:
        tree = double_rotate_right(tree)

    return tree

"""
  //==========================================
  //              rebalance
  //==========================================
  // rebalance(T) does the following.
  //
  //   (1) Perform a rotation at T if required.
  //
  //   (2) Set the ht field of T correctly,
  //       regardless of whether or not a
  //       rotation is done.
  //
  // Requirement: T must not be empty.
  //==========================================
"""
def rebalance(tree):
    hl = height(tree.left)
    hr = height(tree.right)

    if hl > hr + 1:
        tree = rotate_right(tree)
    elif hl + 1 < hr:
        tree = rotate_left(tree)
    else:
        install_height(tree)


def insert(root, key):
    t = root

    if key < t.value:
        if t.left is None:
            t.left = treeNode(key)
        else:
            t = t.left
    else:
        if t.right is None:
            t.right = treeNode(key)
        else:
            t = t.right
            t = insert(t, key)
            rebalance(t)


class AVLTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = treeNode(key)
        else:
            self.root = insert(self.root, )
