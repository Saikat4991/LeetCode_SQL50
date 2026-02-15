class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                # Token is an operand (number), push it to the stack
                stack.append(int(token))
            else:
                # Token is an operator
                # Pop the last two operands (order is important for subtraction/division)
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                if token == "+":
                    result = left_operand + right_operand
                elif token == "-":
                    result = left_operand - right_operand
                elif token == "*":
                    result = left_operand * right_operand
                else:
                    # Truncate division toward zero
                    result = int(left_operand / right_operand)
                    
                # Push the result back onto the stack
                stack.append(result)

        # The final result is the only element left on the stack
        return stack[0]
        