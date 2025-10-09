# ################ Example 1 ################
# Assigning values to variables individually

a = 10       # integer variable
b = 10.5     # float variable

print(a)     # prints 10
print(b)     # prints 10.5
print(a, b)  # prints 10 10.5

# ################ Example 2 ################
# Multiple variable assignment in one line

a, b, c = 10, 20, 'welcome'  # a=10, b=20, c='welcome'

print(a, b, c)  # prints: 10 20 welcome


############### Example #3 ###############

# a = 100
# b = 100
# c = 100

a = b = c = 100

print(a, b, c)

############### Example #4 ###############

x = 1
y = 2

print(x, y)   # Output: 1 2

y, x = x, y   # Swap values
print(x, y)   # Output: 2 1
