
def evaluate_postfix(expr: str) -> int:
    stack = []
    try:
        for elm in expr:
            if elm.isdigit():
                stack.append(elm)
            else:
                second, first = stack.pop(), stack.pop()
                if first is None or second is None:
                    return None
                stack.append(str(eval(first + elm + second)))
        if len(stack) == 1:
            return stack.pop()
        return None
    except TypeError:
        return "Invalid expression"

print(evaluate_postfix("921*-8-4+"))