#Emulación de un switch sin usar if

def operations(operation, a, b):
    return {
        'add': lambda: a + b,
        'sub': lambda: a - b,
        'mul': lambda: a * b,
        'div': lambda: a / b
    }.get(operation, lambda: None)
    
print(operations('add', 3, 5)())