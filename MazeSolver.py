dir = [North, West, South, East]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = get_world_size()
wall = set()

def left_hand_method(d):
	if can_move(dir[(d + 1) % 4]):
		d = (d + 1) % 4
	else:
		if can_move(dir[d]):
			d = d
		else:
			if can_move(dir[(d - 1) % 4]):
				d = (d - 1) % 4
			else:
				d = (d + 2) % 4
	move(dir[d])
	return d

def build_wall():
	d = 0
	for _ in range(n * n * 3):
		x, y = (get_pos_x(), get_pos_y())
		for d2 in range(4):
			if can_move(dir[d2]) == False:
				nx, ny = (x + dx[d2], y + dy[d2])
				wall.add(((x, y), (nx, ny)))
				wall.add(((nx, ny), (x, y)))
		if can_move(dir[(d + 1) % 4]):
			d = (d + 1) % 4
		else:
			if can_move(dir[d]):
				d = d
			else:
				if can_move(dir[(d - 1) % 4]):
					d = (d - 1) % 4
				else:
					d = (d + 2) % 4
		move(dir[d])

def shortest_route():
	dist = {}
	for i in range(n):
		for j in range(n):
			dist[(i, j)] = -1
	sx, sy = (get_pos_x(), get_pos_y())
	dist[(sx, sy)] = 0
	que = []
	que.append((sx, sy))
	front = 0
	gx, gy = measure()
	while front < len(que):
		x, y = que[front]
		if (x, y) == (gx, gy):
			break
		front = front + 1
		for d in range(4):
			nx, ny = (x + dx[d], y + dy[d])
			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue
			if ((x, y), (nx, ny)) in wall:
				continue
			if dist[(nx, ny)] != -1:
				continue
			dist[(nx, ny)] = dist[(x, y)] + 1
			que.append((nx, ny))
	x, y = (gx, gy)
	route = []
	while dist[(x, y)] != 0:
		for d in range(4):
			nx, ny = (x + dx[d], y + dy[d])
			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue
			if ((x, y), (nx, ny)) in wall:
				continue
			if dist[(nx, ny)] == dist[(x, y)] - 1:
				route.append((d + 2) % 4)
				x, y = (nx, ny)
				break
	return route

def action(route):
	while len(route) > 0:
		d = route[len(route) - 1]
		move(dir[d])
		route.pop()
	
def build_maze():
	clear()
	plant(Entities.Bush)
	substance = get_world_size() * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	use_item(Items.Weird_Substance, substance)

build_maze()
build_wall()
for i in range(10):
	route = shortest_route()
	action(route)
	if i < 10 - 1:
		substance = get_world_size() * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
		use_item(Items.Weird_Substance, substance)
	else:
		harvest()
