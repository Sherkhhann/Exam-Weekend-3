# ### 5 Question
# Write a program that merges two dictionaries into one / Напишите программу, объединяющую два словаря в один
# ```
# Input: data_1, data_2 = {1: 1, 2: 4, 3: 9}, {4: 16, 5: 25, 6: 36}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# ```

data_1 = {}
data_2 = {}
i = 0
while i < 3:
	key_input = int(input("Enter key - >"))
	value_input = int(input("Enter value - >"))
	data_1[key_input] = value_input
	i += 1
j = 0
while j < 3:
	key_input = int(input("Enter key - >"))
	value_input = int(input("Enter value - >"))
	data_2[key_input] = value_input
	j += 1
data_1.update(data_2)

print(data_1)