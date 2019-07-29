x = "hello"
y = "hello"

print(x is y)

x = "hello!"
y = "hello!"

print(y is x)

x = 's' * 20 is 'ssssssssssssssssssss'
y = 's' * 21 is 'sssssssssssssssssssss'
print(x,y)
print("this")