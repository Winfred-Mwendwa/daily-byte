#using reverse() and join()
my_string = "Cat"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)

my_string = "The Daily Byte"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)

my_string = "civic"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)

# using a for loop- each character is preappended into the empty string, reversing their order
my_string = 'civic'
reversed_string = ''
for char in my_string:
    reversed_string = char + reversed_string
print(reversed_string) 

# using string indexing
#[start: stop: step-size] negative step size means you want to reverse the string
my_string = 'CAt'
print(my_string[::-1])

#using list comprehension
#new_list = [expression for x in iterable if condition == true/false]
#the expression is the result which you can manipulate once the condition is evaluated.

my_string = 'CAt'
reversed_string = ''.join([char.upper() for char in reversed(my_string) if 'A' in reversed(my_string)])
print(reversed_string)



