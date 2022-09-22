# Start
import pygame, random, math
# import matplotlib
import matplotlib.pyplot as plt

figure, grafik = plt.subplots()  # Create a figure containing a single axes.

# FPS
FPS = 100
fpsClock = pygame.time.Clock()

# important variable(food and animal, that you can change)
how_much_food_to_append = 0.1
how_much_animal_to_append = 3
start_health = 79.9
how_much_health_to_append = 10

# variable and things like that
speed = []
#predators = []
around_speed = 0
around_speed_list = []
grafik_x_food = []
grafik_x_animal_blue = []
grafik_x_animal_red = []
grafik_y_time = []
pere = 0
grafik_y_time_was = 0
number_of_animal1 = 0
type_of_animal = []
#predators_speed = []
#predators_health = []
pygame.init()
save_FPS = FPS
#nearest_victim_to_predator = []
number_of_victim = 0
loop = True
window = pygame.display.set_mode((1400, 800), 0, 32)
player = pygame.Rect(400, 400, 20, 20)
number_of_animal = 0
how_much_blue_animal = 0
number_of_food = 0
how_much_animal = 0
nearest_victim_distance_for_now = 0
random_thing = 0
how_much_food_to_append_copy = how_much_food_to_append
how_much_food = 0
number_of_nearest_victim_for_now = 0
random_x = 0
random_y = 0
random_width = 0
random_height = 0
distance = 0
need_to_move = []
how_much_you_need_to_wait_food = 0
mat_for_now = None
gep_y = 0
gep_x = 0
nearest_food_distance_for_now = 1000000000000000000000
number_of_nearest_food_for_now = None
pygame.display.set_caption('Evolution')
player_step = 3
nearest_food_to_animal = []
bacteries = []
food = []
health = []

# append start animal and health
for animal in range(how_much_animal_to_append):
    how_much_animal += 1
    bacteries.append(pygame.Rect(random.randint(0, 1400), random.randint(0, 800), 20, 20))
    speed.append(2)
    health.append(start_health)

#predators.append(pygame.Rect(random.randint(0, 1400), random.randint(0, 800), 20, 20))
#predators_speed.append(2)
#predators_health.append(start_health)

# append start food
if how_much_food_to_append > 1 or how_much_food_to_append == 1:
    for mat in range(how_much_food_to_append):
        how_much_food += 1
        food.append(pygame.Rect(random.randint(20, 1380), random.randint(20, 780), 15, 15))
else:
    for mat in range(2):
        how_much_food += 1
        food.append(pygame.Rect(random.randint(20, 1380), random.randint(20, 780), 15, 15))

# Colors
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Upgrade Window
window.fill(WHITE)
pygame.display.update()


# functions
def find_the_nearest_food(number_of_animal=number_of_animal, number_of_food=number_of_food, distance=distance,
                          nearest_food_distance_for_now=nearest_food_distance_for_now,
                          number_of_nearest_food_for_now=number_of_nearest_food_for_now):
    for animal in bacteries:
        number_of_animal += 1
        nearest_food_distance_for_now = 1000000000000000000000
        number_of_food = 0
        number_of_nearest_food_for_now = None
        distance = 0

        for mat in food:
            number_of_food += 1

            # food and animal coords
            food_x = mat.centerx
            food_y = mat.centery
            animal_x = animal.centerx
            animal_y = animal.centery

            # find the distance between animal and food
            gep_y = animal_y - food_y
            gep_x = animal_x - food_x
            distance = math.sqrt((gep_y * gep_y + gep_x * gep_x))

            # if that distance was less that previous smallest distance, change the smallest distance
            if distance < nearest_food_distance_for_now or distance == nearest_food_distance_for_now:
                nearest_food_distance_for_now = distance
                number_of_nearest_food_for_now = number_of_food

            # trying to find the end, and if that was the end, append number of nearest food for now
            if number_of_food == how_much_food:
                nearest_food_to_animal.append(food[number_of_nearest_food_for_now - 1])

    return nearest_food_to_animal





# Main Loop
while loop:

    nearest_food_to_animal.clear()
    nearest_food_distance_for_now = 1000000000000000000000
    number_of_animal = 0
    number_of_food = -1

    # To go out
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            grafik.plot(grafik_y_time, grafik_x_animal_blue, color='blue')
            grafik.plot(grafik_y_time, grafik_x_food, color='green')
            grafik.plot(grafik_y_time, around_speed_list, color='yellow')
            plt.xlabel('Time(ticks)')
            plt.ylabel('How Much Blocks')
            grafik.plot()
            plt.show()
            pygame.quit()

    # Move player        
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_s] or pressed_keys[pygame.K_d] or pressed_keys[pygame.K_a]:
        if pressed_keys[pygame.K_w]:
            player.y -= player_step
        if pressed_keys[pygame.K_s]:
            player.y += player_step
        if pressed_keys[pygame.K_d]:
            player.x += player_step
        if pressed_keys[pygame.K_a]:
            player.x -= player_step
    else:
        if pressed_keys[pygame.K_UP]:
            player.y -= player_step
        if pressed_keys[pygame.K_DOWN]:
            player.y += player_step
        if pressed_keys[pygame.K_RIGHT]:
            player.x += player_step
        if pressed_keys[pygame.K_LEFT]:
            player.x -= player_step

    if pressed_keys[pygame.K_SPACE]:
        FPS = 0
    if pressed_keys[pygame.K_1]:
        FPS = 10
    if pressed_keys[pygame.K_2]:
        FPS = 20
    if pressed_keys[pygame.K_3]:
        FPS = 30
    if pressed_keys[pygame.K_4]:
        FPS = 40
    if pressed_keys[pygame.K_5]:
        FPS = 50
    if pressed_keys[pygame.K_6]:
        FPS = 60
    if pressed_keys[pygame.K_7]:
        FPS = 70
    if pressed_keys[pygame.K_8]:
        FPS = 80
    if pressed_keys[pygame.K_9]:
        FPS = 90
    if pressed_keys[pygame.K_PLUS]:
        how_much_animal += 1
        bacteries.append(pygame.Rect(random.randint(0, 1400), random.randint(0, 800), 20, 20))
        speed.append(2)
        health.append(start_health)
        type_of_animal.append(0)

    # Append food
    if how_much_food_to_append < 1 and how_much_food_to_append_copy == 1 or how_much_food_to_append_copy > 1:
        how_much_food += 1
        food.append(pygame.Rect(random.randint(20, 1380), random.randint(20, 780), 15, 15))
        how_much_food_to_append_copy = how_much_food_to_append

    if how_much_food_to_append_copy > 1 or how_much_food_to_append_copy == 1:
        for mat in range(how_much_food_to_append):
            how_much_food += 1
            food.append(pygame.Rect(random.randint(20, 1380), random.randint(20, 780), 15, 15))

    how_much_food_to_append_copy = how_much_food_to_append_copy * 2
    find_the_nearest_food()


    pygame.draw.rect(window, BLUE, player)

    for mat in food:
        if mat in nearest_food_to_animal:
            pygame.draw.rect(window, RED, mat)
        else:
            pygame.draw.rect(window, GREEN, mat)

    number_of_animal = 0

    # most things about animal - moving, minus health, touch the food, plus health  , new animals
    for animal in bacteries:
        # move the animal
        number_of_animal = bacteries.index(animal)
        if nearest_food_to_animal[number_of_animal].x < animal.x:
            animal.x -= speed[number_of_animal]
        if nearest_food_to_animal[number_of_animal].x > animal.x:
            animal.x += speed[number_of_animal]

        if nearest_food_to_animal[number_of_animal].y < animal.y:
            animal.y -= speed[number_of_animal]
        if nearest_food_to_animal[number_of_animal].y > animal.y:
            animal.y += speed[number_of_animal]
        number_of_animal = bacteries.index(animal)


    number_of_animal = 0

    # minus health and dead
    for animal in bacteries:

        health[number_of_animal] -= speed[number_of_animal]/10+0.1

        if health[number_of_animal] < 0 or health[number_of_animal] == 0:
            how_much_animal -= 1
            del bacteries[number_of_animal]
            del health[number_of_animal]
            del speed[number_of_animal]
        number_of_animal += 1

    number_of_animal = 0
    for animal in bacteries:
        random_thin = random.randint(0, 100)
        # new animal
        if random_thin > 20:
            if health[number_of_animal] > 110 or health[number_of_animal] == 110:
                how_much_animal += 1
                health[number_of_animal] = start_health
                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    random_x = animal.x + 15
                else:
                    random_x = animal.x - 15

                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    random_y = animal.y + 15
                else:
                    random_y = animal.y - 15

                bacteries.append(pygame.Rect(random_x, random_y, animal.width, animal.height))
                health.append(start_health)

                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    speed.append(speed[number_of_animal] - 1)
                if random_thing == 1:
                    speed.append(speed[number_of_animal] + 1)
            number_of_animal += 1

        if random_thin < 20:
            if health[number_of_animal] > 110 or health[number_of_animal] == 110:
                how_much_animal += 1
                health[number_of_animal] = start_health
                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    random_x = animal.x + 15
                else:
                    random_x = animal.x - 15

                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    random_y = animal.y + 15
                else:
                    random_y = animal.y - 15


                random_thing = random.randint(0, 1)
                if random_thing == 0:
                    speed.append(speed[number_of_animal] - 1)
                if random_thing == 1:
                    speed.append(speed[number_of_animal] + 1)
            number_of_animal += 1

        # Touch The Food and plus health
    number_of_animal = 0

    for mat in food:
        number_of_animal = 0
        if player.colliderect(mat) and mat in food:
            how_much_food -= 1
            food.remove(mat)
        for animal in bacteries:
            number_of_animal = bacteries.index(animal)
            if (animal.colliderect(mat) and mat in food):
                how_much_food -= 1
                food.remove(mat)
                health[number_of_animal] += how_much_health_to_append
                number_of_animal = bacteries.index(animal)

    # Draw animals
    number_of_animal = 0
    for animal in bacteries:
        pygame.draw.rect(window, [0, 0, (255 - speed[number_of_animal] * 15)], animal)


    # append info to grafik

    grafik_x_food.append(how_much_food / 10)

    grafik_x_animal_blue.append(how_much_animal)

    grafik_y_time_was = grafik_y_time_was + 1
    grafik_y_time.append(grafik_y_time_was)

    around_speed = sum(speed) / len(speed) * 10
    around_speed_list.append(around_speed)

    pygame.display.update()
    window.fill(WHITE)
    fpsClock.tick(FPS)

            
       
