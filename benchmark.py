from random import randrange
from selection_sort import selection_sort
from bubble_sort import bubble_sort

#Let's create a list

mylist = [randrange(1000) for _ in range(1000)]

#.....


#Save Execution time of Selection Sort

selection_sort_time = selection_sort(mylist.copy())

#Save Execution time of Bubble Sort

bubble_sort_time = bubble_sort(mylist.copy())

#Save Execution time of Default Sort

copy_list = mylist.copy()
default_sort_time = copy_list.sort()


#Save results on a file

result_file = open("results.csv", "a")
result_file.write(f"{len(mylist)}, {selection_sort_time}, {bubble_sort_time}, {default_sort_time}\n")
result_file.close()