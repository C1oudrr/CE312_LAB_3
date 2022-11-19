stack = ['A','B','C','E','F']
print("Reverse : Before")
for i in range(5):
    print(stack[i])
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.append('F')
stack.append('E')
stack.append('C')
stack.append('B')
stack.append('A')

print("Reverse : After")
for i in range(5):
    print(stack[i])