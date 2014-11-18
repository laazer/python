#! /usr/bin/python

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

def test(n):
    tlist = [2, 5, 6, 6]
    ropes_test = lambda n: ropes(n, tlist)
    for i in range(n):
        print(str(i) + ": " + str(ropes_test(i)))

print "DR. ROPES"
test(20)
print "\n"
# ------------------------------------
class Tree:
    def __init__(self, fruit, branch=[]):
        self.fruit = fruit
        self.branch = branch

    def __str__(self):
        return str(self.fruit)

# returns if the tree is node
def isNode(tree):
    return len(tree.branch) == 0

# returns maximum number of fruit on the given tree
def max_fruit(tree):
    if isNode(tree):
        return tree.fruit
    else:
        return max(map(lambda x: (tree.fruit + max_fruit(x)), tree.branch))

# returns if the ant will be full if it goes down the given tree
def ant_fed(n, tree):
    return n >= max_fruit(tree)

l1 = Tree(5)
l2 = Tree(10, [l1, l1])
l3 = Tree(11, [l2, l1, l2])
l4 = Tree(2, [l3, l2, l2, l1, l3])

print "CURIOUS ANT"

print not(ant_fed(3, l1));
print ant_fed(6, l1);
print not(ant_fed(12, l2));
print ant_fed(30, l4);
