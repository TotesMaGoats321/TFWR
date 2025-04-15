clear()
#Program that farms trees in an effiecent manner based on world size
size = get_world_size()
#print(size)

alternate = 1



while True:
    for i in range(size):
        for j in range(size):
            # We want to water only the trees

            if can_harvest():
                harvest()

            if (j + alternate) % 2 == 0:
                plant(Entities.Tree)

                if get_water() < 0.4:
                    use_item(Items.Water)

            else:
                plant(Entities.Bush)

            move(North)
        if i % 2 != 0:
            alternate = 1
        else:
            alternate = 0
        move(East)
