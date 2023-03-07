class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyboard = {}
        keyboard['2'] = ['a','b','c']
        keyboard['3'] = ['d','e','f']
        keyboard['4'] = ['g','h','i']
        keyboard['5'] = ['j','k','l']
        keyboard['6'] = ['m','n','o']
        keyboard['7'] = ['p','q','r','s']
        keyboard['8'] = ['t','u','v']
        keyboard['9'] = ['w','x','y','z']
        self.total = []
        def backtrack(cur, ind, digits):
            if ind >= len(digits):
                self.total.append(cur)
                return
            num = digits[ind]
            for c in keyboard[num]:
                temp = cur + c
                backtrack(temp, ind+1, digits)
            return
        backtrack("", 0, digits)
        return self.total
            
