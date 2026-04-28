class MinStack:
    def __init__(self):
        self.stack = []      # 主栈,存所有元素
        self.min_stack = []  # 辅助栈,栈顶永远是当前最小值

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果 min_stack 为空,或者 val <= 当前最小值,就压入
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # 如果弹出的正好是当前最小值,min_stack 也要同步弹出
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]