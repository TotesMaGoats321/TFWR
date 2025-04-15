clear()
#Define the size of the map
size = 6


def harvestGrass():
	if can_harvest():
		harvest()

def harvestWood():
	if can_harvest():
		harvest()
		plant(Entities.Bush)

def harvestCarrot():
	if can_harvest():
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if get_water() < 0.25:
			use_item(Items.Water)
		plant(Entities.Carrot)
		

# Define the main loop for the code
while True:
	for i in range(size):
		harvestGrass()
		move(North)
	move(East)

	for i in range(size):
		harvestWood()
		move(North)
	move(East)
		
	for i in range(size):
		harvestCarrot()
		move(North)
		
	move(East)