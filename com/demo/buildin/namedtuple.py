from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(isinstance(p, tuple))