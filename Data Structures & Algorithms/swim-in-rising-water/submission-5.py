from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 四个移动方向：右、左、下、上
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # 最小堆中的元素：
        # (到达当前位置所需要的最小水位, 行, 列)
        #
        # 起点本身的高度是 grid[0][0]
        # 所以至少要等水位达到 grid[0][0] 才能开始
        min_heap = [(grid[0][0], 0, 0)]

        # 防止重复处理同一个位置
        visited = set()

        while min_heap:
            # 每次优先处理所需水位最低的位置
            time, r, c = heapq.heappop(min_heap)

            # 如果这个位置已经处理过，就跳过
            if (r, c) in visited:
                continue

            visited.add((r, c))

            # 第一次从最小堆中取出终点时，
            # 当前 time 就是到达终点所需的最小时间
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                ):
                    # 到达相邻位置需要的水位：
                    #
                    # 1. 之前路径已经要求的水位 time
                    # 2. 新格子的高度 grid[nr][nc]
                    #
                    # 必须同时满足，所以取最大值
                    next_time = max(time, grid[nr][nc])

                    heapq.heappush(
                        min_heap,
                        (next_time, nr, nc)
                    )

        return -1