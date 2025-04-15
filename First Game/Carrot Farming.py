clear()

def harvestCarrot():
	if can_harvest():
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if get_water() == 0:
			use_item(Items.Water)
		plant(Entities.Carrot)
		

while True:
	for i in range(6):
		harvestCarrot()
		move(North)
	move(East)