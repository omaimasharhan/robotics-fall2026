"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct
from collections import deque




def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """

    start = ctx.start
    goal = ctx.goal

    frontier = deque([start])
    parent = {start: None}
    visited = {start}

    if start == goal:
        return [start]

    while frontier:
        current = frontier.popleft()

        if current == goal:
            return reconstruct(parent, goal)

        for nxt in ctx.expand(current, len(frontier) + 1):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)

    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """

    start = ctx.start
    goal = ctx.goal

    frontier = [start]
    parent = {start: None}
    visited = {start}

    if start == goal:
        return [start]

    while frontier:
        current = frontier.pop()

        if current == goal:
            return reconstruct(parent, goal)

        neighbors = ctx.expand(current, len(frontier) + 1)

        for nxt in reversed(neighbors):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)

    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """

    start = ctx.start
    goal = ctx.goal

    if start == goal:
        return [start]

    max_depth = len(ctx.grid) * len(ctx.grid[0]) - 1

    for depth_limit in range(max_depth + 1):
        frontier = [(start, 0, (start,))]
        
        while frontier:
            current, depth, path = frontier.pop()

            if current == goal:
                return list(path)

            if depth >= depth_limit:
                continue

            neighbors = ctx.expand(current, len(frontier) + 1)
            path_set = set(path)

            for nxt in reversed(neighbors):
                if nxt not in path_set:
                    frontier.append(
                        (nxt, depth + 1, path + (nxt,))
                    )

    return []


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """

    start = ctx.start
    goal = ctx.goal

    if start == goal:
        return [start]

    frontier = []
    counter = 0

    heappush(
        frontier,
        (ctx.heuristic(start), counter, 0, start)
    )

    parent = {start: None}
    best_g = {start: 0}

    while frontier:

        priority, _, current_g, current = heappop(frontier)

        if current_g != best_g[current]:
            continue

        if current == goal:
            return reconstruct(parent, goal)

        for nxt in ctx.expand(current, len(frontier) + 1):

            new_g = current_g + 1

            if nxt not in best_g or new_g < best_g[nxt]:

                best_g[nxt] = new_g
                parent[nxt] = current

                counter += 1
                priority = new_g + ctx.heuristic(nxt)

                heappush(
                    frontier,
                    (priority, counter, new_g, nxt)
                )

    return []










   


