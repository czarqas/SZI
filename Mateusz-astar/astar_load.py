import astar

start = astar.points[2][6]
goal = astar.points[11][11]

path = astar.astar(start,goal)

astar.print_path(path)
