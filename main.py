from addition import *
from mymod import *
import sys

print("\nHere goes task 1")
task1 = [1, 2, 3, 4, 5]
multiply_func(*task1)


print("\nHere goes task 2")
print(sys.path)
sys.path.append("C:/Users/meekh/python")
print("\n", sys.path)


print("\nHere goes task 3")
count_lines("C:/Users/meekh/python/records.txt")
count_chars("C:/Users/meekh/python/records.txt")
test("C:/Users/meekh/python/records.txt")
