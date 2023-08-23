# write a python program to count the number of strings feom a given list of strings . the
# of strings . The string length is 2 or more and the first and last characters are the same .

# sample list : ['abc','xyz','aba','1221']
# Expected Result:2


list=['abc','1221','aba','xyz']
count=0
for i in list:
   if len(i)>=2:
    if i[0]==i[-1]:
      count+=1

print("Total count =",count)


""" write a python program to get a list,sorted in increasing order by the last element in each
tuple .
from a given list of non-empty tuples.

sample list: [(2,5),(1,2),(4,4),(2,3),(2,1)]
Expected Result: [(2,1),(1,2),(2,3),(4,4),(2,5)]

"""

""" write a python program to remove duplicates from a list."""







   
