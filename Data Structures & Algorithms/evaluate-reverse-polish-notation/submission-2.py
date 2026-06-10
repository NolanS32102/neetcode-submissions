class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(0, len(tokens)):
            if self.is_number(tokens[i]):
                stack.append(tokens[i])
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                val = self.calculate(left, right, tokens[i])
                stack.append(val)
        
        return int(stack.pop())
    

    def calculate(self, left: int, right: int, op: str) -> int:
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return int(left / right)
        else:
            print("Invalid operator")
            return -99999

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False