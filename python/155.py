class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min.append((val,len(self.stack)))
        else:
            low, index = self.min[-1]
            if val < low:
                self.min.append((val, len(self.stack)))
        self.stack.append(val)

        
    def pop(self) -> None:
        val = self.stack.pop()
        index = len(self.stack)

        if (val, index) == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][0]

def main():
    min_stack = MinStack()
    return 0

if __name__ == "__main__":
    main()