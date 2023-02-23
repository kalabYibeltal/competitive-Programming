class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.memo = defaultdict(lambda: "")
        return self.solve(expression)
        
    def solve(self, expression):
        if expression.isdigit():
            return [int(expression)]
        
        if self.memo[expression] != "":
            return self.memo[expression]
        
        res = []
        
        for i in range(len(expression)):
            if not expression[i].isdigit():
                left_exps = self.solve(expression[:i])
                right_exps = self.solve(expression[i+1:])
                
                for left in left_exps:
                    for right in right_exps:
                        res.append(eval(str(left) + expression[i] + str(right)))
                        
        self.memo[expression] = res
        return self.memo[expression]