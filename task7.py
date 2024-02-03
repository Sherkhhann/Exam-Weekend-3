# ### 7 Question
# Write a program to transform a dictionary into a list of tuples / Напишите программу преобразования словаря в список кортежей.
# ```
# Input: {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Output: [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]
# ```

new_dict = {}
new_list = []
i=0
while i<5:
	key_input = input("Enter key - >")
	value_input = int(input("Enter value - >"))
	new_dict[key_input] = value_input
	i += 1
for k in new_dict.items():
	new_list.append(k)
print(new_list)