# Floor Division #
#
# In floor division, the result is floored to the nearest smaller integer. It is also known as integer division.
#
# For floor division, we must use the // operator:

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

# Modulo #
#
# A number’s modulo with another number can be found using the % operator:

print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

# Precedence #
#
# An arithmetic expression containing different operators will be computed on the basis of operator precedence.
#
# Whenever operators have equal precedence, the expression is computed from the left side:

# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication

# Parentheses #
#
# An expression which is enclosed inside parentheses will be computed first, regardless of operator precedence:

print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))

# Comparisons#
#
# The result of a comparison is always a bool.
#
# If the comparison is correct, the value of the bool will be True. Otherwise, its value will be False.
#
# The == and != operators compare the values of both operands. However, the identity operators, is and is not, check whether the two operands are the exact same object.
#
# Let’s look at a few examples:

num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects


# Assigning Values#
#
# Let’s go through a few examples to see how values are assigned to variables.
#
# Variables are mutable, so we can change their values whenever we want!

year = 2019
print(year)

year = 2020
print(year)

year = year + 1  # Using the existing value to create a new one
print(year)

# One thing to note is that when a variable, first, is assigned to another variable, second, its value is copied into second. Hence,
# if we later change the value of first, second will remain unaffected:

first = 20
second = first
first = 35  # Updating 'first'

print(first, second)  # 'second' remains unchanged

first = 20
second = first
first = 35  # Updating 'first'

print(first, second)  # 'second' remains unchanged

num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)

# Search #
#
# The in keyword can be used to check if a particular substring exists in another string. If the substring is found, the operation returns true.
#
# Here’s how it works:
random_string = "This is a random string"

print('of' in random_string)  # Check whether 'of' exists in randomString
print('random' in random_string)  # 'random' exists!

x = 20
y = 5
result = (x + True) / (4 - y * False)
