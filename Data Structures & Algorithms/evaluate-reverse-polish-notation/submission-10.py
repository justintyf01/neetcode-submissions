class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok_len = len(tokens)
        stack = []

        for i in range(tok_len):
            if tokens[i] in ('+', '-', '*', '/'):
                op = tokens[i]
                first = stack.pop()
                if op == "+":
                    stack.append(stack.pop() + first)
                if op == "*":
                    stack.append(stack.pop() * first)
                if op == "-":
                    stack.append(stack.pop() - first)
                if op == "/":
                    stack.append(int(stack.pop() / first))
            else:
                num = int(tokens[i])
                stack.append(num)
            
        return stack.pop()