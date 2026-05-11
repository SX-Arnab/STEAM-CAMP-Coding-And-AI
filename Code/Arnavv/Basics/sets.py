set = {1, 2, 3, 3, 4}
# print(set) # removes 3 cuz its repeating and sets are well defined and cant contain  similar elements
set.add(5)
set.remove(2)
# print(set) # Yes, it present


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

sub = set1-set2
print(sub)