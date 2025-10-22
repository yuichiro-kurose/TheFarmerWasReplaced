def go_to(x, y):
	while get_pos_x() < x:
		move(East)
	while get_pos_x() > x:
		move(West)
	while get_pos_y() < y:
		move(North)
	while get_pos_y() > y:
		move(South)

def polyculture_farmer():
	home_x, home_y = get_pos_x(), get_pos_y()
	while True:
		if can_harvest():
			harvest()
			while get_water() <= 0.75:
				use_item(Items.Water)
			plant(Entities.Grass)
			plant_type, (x, y) = get_companion()
			go_to(x, y)
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			while get_water() <= 0.75:
				use_item(Items.Water)
			plant(plant_type)
			go_to(home_x, home_y)

def pumpkin_farmer():
	while True:
		while True:
			flag = True
			for x in range(6):
				for y in range(6):
					if get_ground_type() == Grounds.Grassland:
						till()
					while get_water() <= 0.75:
						use_item(Items.Water)
					if can_harvest() == False:
						flag = False
						plant(Entities.Pumpkin)
					if y < 5 and x % 2 == 0:
						move(North)
					if y < 5 and x % 2 == 1:
						move(South)
				if x < 5:
					move(East)
			for x in range(5):
				move(West)
			if flag:
				break
		harvest()

def cactus_farmer():
	while True:
		for x in range(6):
			for y in range(6):
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Cactus)
				if y < 5 and x % 2 == 0:
					move(North)
				if y < 5 and x % 2 == 1:
					move(South)
			if x < 5:
				move(East)
		for x in range(4):
			move(West)
		for y in range(6):
			while True:
				flag = True
				for x in range(4):
					if measure() > measure(East):
						flag = False
						swap(East)
					if x < 3:
						move(East)
				for x in range(4):
					if measure() < measure(West):
						flag = False
						swap(West)
					if x < 3:
						move(West)
				if flag:
					break
			if y < 5:
				move(North)
		move(West)
		move(South)
		for x in range(6):
			while True:
				flag = True
				for y in range(4):
					if measure() < measure(South):
						flag = False
						swap(South)
					if y < 3:
						move(South)
				for y in range(4):
					if measure() > measure(North):
						flag = False
						swap(North)
					if y < 3:
						move(North)
				if flag:
					break
			if x < 5:
				move(East)
		for x in range(5):
			move(West)
		for y in range(4):
			move(South)
		harvest()

def sunflower_farmer():
	while True:
		for x in range(6):
			for y in range(6):
				harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				while get_water() <= 0.75:
					use_item(Items.Water)
				plant(Entities.Sunflower)
				if y < 5 and x % 2 == 0:
					move(North)
				if y < 5 and x % 2 == 1:
					move(South)
			if x < 5:
				move(East)
		for x in range(5):
			move(West)

for x in range(4):
	for y in range(4):
		go_to(x * 4 + 15, y * 4 + 15)
		spawn_drone(polyculture_farmer)

go_to(0, 0)
spawn_drone(pumpkin_farmer)
go_to(6, 6)
spawn_drone(pumpkin_farmer)
go_to(0, 12)
spawn_drone(pumpkin_farmer)
go_to(6, 18)
spawn_drone(pumpkin_farmer)
go_to(0, 24)
spawn_drone(pumpkin_farmer)

go_to(6, 0)
spawn_drone(cactus_farmer)
go_to(0, 6)
spawn_drone(cactus_farmer)
go_to(6, 12)
spawn_drone(cactus_farmer)
go_to(0, 18)
spawn_drone(cactus_farmer)
go_to(6, 24)
spawn_drone(cactus_farmer)
go_to(12, 6)
spawn_drone(cactus_farmer)
go_to(18, 0)
spawn_drone(cactus_farmer)
go_to(24, 6)
spawn_drone(cactus_farmer)

go_to(12, 0)
spawn_drone(sunflower_farmer)
go_to(18, 6)
spawn_drone(sunflower_farmer)
go_to(24, 0)
sunflower_farmer()
