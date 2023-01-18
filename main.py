class Stack():

    def __init__(self, stack:str=''):
        self.stack = list(stack)

    def isEmpty(self):
        return False if len(self.stack) > 0 else True

    def push(self, item:str):
        self.stack += item

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def balance(some_stack = Stack):
    if some_stack.size() % 2 != 0:
        return print("Несбалансированно")
    else:
        new_stack = Stack([])
        while some_stack.size() > 0:
            if some_stack.peek() == "]" or some_stack.peek() == ")" or some_stack.peek() == "}":
                new_stack.push(some_stack.pop())
            else:
                matching = some_stack.pop() + new_stack.pop()
                if matching == '()' or matching == '[]' or matching == '{}':
                    continue
                else:
                    return print("Несбалансированно")
        if some_stack.size() == 0:
            return print("Сбалансированно")

if __name__ == '__main__':
    stack1 = balance(Stack('(((([{}]))))'))
    stack2 = balance(Stack('[([])((([[[]]])))]{()}'))
    stack3 = balance(Stack('{{[()]}}'))
    stack4 = balance(Stack('}{}'))
    stack5 = balance(Stack('{{[(])]}}'))
    stack6 = balance(Stack('[[{())}]'))
