# ### 6 Question
# Write a Python program to drop empty items from a dictionary / Напишите программу на Python для удаления пустых элементов из словаря.
# ```
# Input: {'c1': 'Red', 'c2': 'Green', 'c3': None}
# Output: {'c1': 'Red', 'c2': 'Green'}
# ```

new_dict = {}
dict_new = {}
i = 0
while i < 3:
	key_input = input("Enter key - >")
	value_input = input("Enter value - >")
	new_dict[key_input] = value_input
	i += 1
