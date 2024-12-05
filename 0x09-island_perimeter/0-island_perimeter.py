#!/usr/bin/python3
"""
island perimeter
"""

def island_perimeter(grid):
    """
    define gride
    """
    visit = set()

    if not grid:
        return 0

    def dfs(q, w):
        """depth first search"""
        if (q, w) in visit:
            return 0
        if q >= len(grid) or\
                w >= len(grid[0]) or\
                q < 0 or w < 0 or\
                grid[q][w] == 0:
            return 1
        visit.add((q, w))
        result = dfs(q, w + 1)
        result += dfs(q, w - 1)
        result += dfs(q + 1, w)
        result += dfs(q - 1, w)
        return result

    for m in range(len(grid)):
        for n in range(len(grid[0])):
            # do a dfs for only land
            if grid[m][n]:
                return dfs(m, n)
    return 0
