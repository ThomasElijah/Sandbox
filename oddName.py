"""
Elijah
"""

name = input("Enter your name")
while len(name) < 1:
    name = input("Invalid\nEnter your name")
for i in range(0, len(name), 2):
    print(name[i], "")
print()


