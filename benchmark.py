from random import randrange
from selection_sort import selection_sort
from bubble_sort import bubble_sort

#Let's create a list

mylist = [randrange(1000) for _ in range(10000)]

#.....


#Save Execution time of Selection Sort

selection_sort_time = selection_sort(mylist.copy())

#Save Execution time of Bubble Sort

bubble_sort_time = bubble_sort(mylist.copy())

#Save 