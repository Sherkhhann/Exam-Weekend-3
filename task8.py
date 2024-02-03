# ### 8 Question
# Write a program to filter a dictionary based on values / Напишите программу для фильтрации словаря по значениям.
# ```
# Input: {'Apple': 10, 'Orange': 3, 'Banana': 14, 'Watermelon': 21, 'Lemon': 8}
# Output: {'Orange': 3,  'Lemon': 8,  'Apple': 10, ' 'Banana': 14, 'Watermelon': 21}

new_dict = {}
dict_new = {}
list_new = []
i = 0
while i<5:
	key_input = input("Enter key - >")
	value_input = int(input("Enter value - >"))
	new_dict[key_input] = value_input
	i += 1
for k, v in new_dict.items():
	dict_new[v] = k
list_new.append(dict_new)
b = list_new.sort()
print(b)