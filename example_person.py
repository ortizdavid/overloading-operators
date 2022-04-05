from src.person import Person

p1 = Person('Jose', 19, 1.67)
p2 = Person('Maria', 14, 1.55)
p3 = Person('Ana', 25, 1.85)
p4 = Person('Jose', 19, 1.67)
people = [p1, p2, p3, p4]

print('\n-----------------------')
print('Operations between People...')
print(f'{p1} > {p2} --->', (p1 > p2))
print(f'{p1} == {p4} --->', (p1 == p4))
print(f'{p3} < {p2} --->', (p3 < p2))
print(f'{p2} != {p2} --->', (p2 != p4))
print(f'{p1} + {p2} + {p4} ---> ', (p1 + p2 + p3))

print('\n-----------------------')
print('Showing People...')
for p in people:
    p.show()

print('\n-----------------------')
print('Sorting People...')
people.sort()
for p in people:
    p.show()
