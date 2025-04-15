clear()
size = 6

while True:
    totalPumpkins = 0
    for j in range(size):
        for i in range(size):
            if get_ground_type() == Grounds.Grassland:
                till()
            if get_entity_type() == Entities.Pumpkin:
                # count the pumpkins
                totalPumpkins += 1
            if get_water() == 0:
                use_item(Items.Water)
            plant(Entities.Pumpkin)
            move(North)

        move(East)
    
    if totalPumpkins == size*size:
        harvest()