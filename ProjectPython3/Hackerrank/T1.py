s = "qA2"

# Check if the string has any alphanumeric characters
print(any(c.isalnum() for c in s))
# Check if the string has any alphabetical characters
print(any(c.isalpha() for c in s))
# Check if the string has any digits
print(any(c.isdigit() for c in s))
# Check if the string has any lowercase characters
print(any(c.islower() for c in s))
# Check if the string has any uppercase characters
print(any(c.isupper() for c in s))

thickness = 5 # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


n, m = map(int, "9 27".split())

# Upper part
for i in range(0, n//2):
    pattern = '.|.'*(2*i+1)
    print(pattern.center(m, '-'))

# Middle line
print('WELCOME'.center(m, '-'))

# Lower part
for i in range(n//2-1, -1, -1):
    pattern = '.|.'*(2*i+1)
    print(pattern.center(m, '-'))
