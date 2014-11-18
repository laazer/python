#! /usr/bin/python

import unittest

# checks if there is a combination of ropes in ropes
# that equal n
def ropes(n, ropes):
    if n in ropes: return True
    else:
        for i in range(len(filter((lambda x: x < n), ropes))):
            if n in ropes_helper(i, ropes): return True
        return False

# creates a set of every combination of n ropes
def ropes_helper(n, ropes):
    res = []
    l = len(ropes)
    for i in range(l - n):
        res = res + [sum(ropes[i:l-n])]
    return set(res)

# ------------------------------------
class Tree:
    def __init__(self, fruit, branch=[]):
        self.fruit = fruit
        self.branch = branch

    def __str__(self):
        return str(self.fruit)

    # returns if the tree is node
    def isNode(self):
        return len(self.branch) == 0

    # returns maximum number of fruit on the given tree
    def max_fruit(self):
        if self.isNode():
            return self.fruit
        else:
            return max(map(lambda x: (self.fruit + x.max_fruit()), self.branch))

    # returns if the ant will be full if it goes down the given tree
    def ant_fed(self, n):
        return n >= self.max_fruit()

# ------------------------------------------------

# testing class
class TestAll(unittest.TestCase):
    l1 = Tree(5)
    l2 = Tree(10, [l1, l1])
    l3 = Tree(11, [l2, l1, l2])
    l4 = Tree(2, [l3, l2, l2, l1, l3])

    def test_ant_fed(self):
        self.assertTrue(not(self.l1.ant_fed(3)))
        self.assertTrue(self.l1.ant_fed(6))
        self.assertTrue(not(self.l2.ant_fed(12)))
        self.assertTrue(self.l4.ant_fed(30))

    def test_ropes(self):
        tlist = [2, 5, 6, 6]
        ropes_test = lambda n: ropes(n, tlist)
        self.assertTrue(ropes_test(7))
        self.assertTrue(ropes_test(11))
        self.assertTrue(not(ropes_test(3)))
        self.assertTrue(ropes_test(12))
        self.assertTrue(ropes_test(17))
        self.assertTrue(ropes_test(19))
        self.assertTrue(not(ropes_test(15)))

if __name__ == '__main__':
    unittest.main()
