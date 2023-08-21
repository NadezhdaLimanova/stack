from stack import Stack


def brackets(new_string:str):
    stack = Stack()
    closed_brackets = []
    for i in new_string:
        if i in '([{':
            stack.push(i)
        elif i in ')]}':
            closed_brackets.append(i)
            bracket = stack.pop()
            if open == '(' and i == ')':
                closed_brackets.remove(i)
                continue
            elif bracket == '[' and i == ']':
                closed_brackets.remove(i)
                continue
            elif bracket == '{' and i == '}':
                closed_brackets.remove(i)
                continue
    if stack.size() == 0 and len(closed_brackets) == 0:
        print("Сбалансированно")
    else:
        print('Несбалансированно')



if __name__ == "__main__":
    new_string = '[[{())}]'
    brackets(new_string)










