stack = ['A','B','C','D','E','F']
print("FILO : Before")
for i in range(6):
    print(stack[i])
stack.pop()
print("FILO : After")
for i in range(5):
    print(stack[i])
