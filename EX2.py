stack = ['A','B','C','E','F']
print("FILO : Before")
for i in range(5):
    print(stack[i])
stack.pop(0)
print("FILO : After")
for i in range(4):
    print(stack[i])
