import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1️⃣ 统计每种任务出现几次
        count = Counter(tasks)                   # 例如 {A:3, B:3}

        # 2️⃣ 把"次数"放进大顶堆(取负)
        maxHeap = [-c for c in count.values()]   # [-3, -3]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()   # 冷却区:每个元素是 (剩余次数, 可回堆的时间)

        # 3️⃣ 一个周期一个周期地模拟
        while maxHeap or queue:
            time += 1                             # 走过一个周期

            if maxHeap:                           # 堆里有任务可做
                cnt = heapq.heappop(maxHeap) + 1  # 取最多的,做一次(负数+1=用掉一次)
                if cnt != 0:                      # 还有剩余
                    queue.append((cnt, time + n)) # 进冷却,记下何时能回来
            # else 堆空 → 这周期空转,但 time 已经 +1

            if queue and queue[0][1] == time:     # 队首冷却到点了
                heapq.heappush(maxHeap, queue.popleft()[0])  # 取出剩余次数,放回堆

        return time