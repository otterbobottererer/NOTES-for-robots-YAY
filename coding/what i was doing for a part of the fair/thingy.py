Stack = []
ACC = []

def pop():
    Stack.pop(-1)

def push(x):
    Stack.append(x)

def dot():
    print(Stack[-1])
    
def add():
    x = Stack[-1]
    pop()
    y = Stack[-1]
    pop()
    push(x + y)
    
def sub():
    x = Stack[-1]
    pop()
    y = Stack[-1]
    push(y - x)
    
def mul():
    x = Stack[-1]
    pop()
    y = Stack[-1]
    pop()
    push(x * y)
    
def div():
    x = Stack[-1]
    pop()
    y = Stack[-1]
    pop()
    push(y / x)
    
def swap():
    x = Stack[-1]
    pop()
    y = Stack[-1]
    pop()
    push(x)
    push(y)

def save():
    ACC.append(Stack[-1])
    pop()
    
def load():
    push(ACC[-1])
    ACC.pop(-1)

def op(opop):
    if opop == 1:
        load()
        add()
    if opop == 2:
        load()
        sub()
    if opop == 3:
        load()
        mul()
    if opop == 4:
        load()
        div()
        


    
    

    