# Variable Assignment
# variable can not start with number or special characters
print("Variable Assignment: ")
x = 2
print("x is {} ".format(x))

# String
print("String:")
my_str = 'my string'
my_str2 = "what's this?"
print(my_str)
print(my_str2)

# printing
num = 5
name = "Fan"
print('My number is: {one}, and my name is {two}'.format(one=num,two=name))
print('My number is: {}, and my name is {}'.format(num,name))

# Lists
my_list = ['a','b','c','d']
my_list.append('e')
print(my_list)
my_list[0] = 'new'
print(my_list)
nest_list = [1,2,3,[3,5,['target']]]
print(nest_list[3][2][0])

# Dictionaries
my_dic = {'k1':'val1','k2':'val2'}
print(my_dic['k1'])

# Tuple, tuple is immutable
my_tup = (1,2,3,4)
