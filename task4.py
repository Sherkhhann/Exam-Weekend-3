# ### 4 Question
# Write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)  Напишите программу для создания и печати словаря, содержащего число (от 1 до n) в форме (x, x*x)

# ```
# Input: func_name(n=5)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```


def func_name (n):
	new_dict = {}
	i=1
	while i <= n:
		key_input = int(input("Enter key - >"))
		value_input = int(input("Enter value - >"))
		new_dict[key_input] = value_input * value_input
		i += 1
	return new_dict

print(func_name (5))