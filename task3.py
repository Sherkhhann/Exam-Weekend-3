# ### 3 Question
# Write a program to raise a natural number to a power of a given number recursively / Напишите программу, рекурсивно возводящую натуральное число в степень заданного числа
# ```
# Input: power(2, 3)
# Output: 8
# ```

def power_num(x, n):
	if n == 0:
		return 1
	if n % 2 == 0:
		return power_num(x, n // 2) * power_num(x, n // 2)
	else:
		return power_num(x, n-1)*x

a = int(input())
b = int(input())
print(power_num(a, b))