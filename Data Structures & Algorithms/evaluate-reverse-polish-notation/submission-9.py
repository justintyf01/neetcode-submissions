class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        tok_len = len(tokens)
        if tok_len < 2:
            return int(tokens[0])

        stack = []

        for i in range(tok_len):
            try:
                num = int(tokens[i])
                stack.append(num)
            except:
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
            
        return stack.pop()