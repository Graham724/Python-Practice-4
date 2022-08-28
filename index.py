#1.Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))

#2.Write a Python function called mult_list() to multiply all the numbers in a list.
import math
def mult_list(*args):
    return math.prod(list(args))

print(mult_list(1, 2, 3))

#3.Write a Python function called rev_string() to reverse a string.
def rev_string(my_str):
  return my_str[::-1]

print(rev_string("class"))

#4.Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num,min,max):
    if num >= min and num <= max:
        return True
    else:
        return False
    
print(num_within(15, 4, 25))

#5.Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal(6) 