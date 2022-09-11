import pygame
pygame.init()
surface = pygame.display.set_mode((1600,900))
box = pygame.Surface((10, 10))
box_rect = box.get_rect(center = (100,100))

col = 'white'
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    box.fill(col)

    if pygame.key.get_pressed()[pygame.K_UP]:
        speed += 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        speed -= 1
    if pygame.key.get_pressed()[pygame.K_w]:
        box_rect.top -= speed
    if pygame.key.get_pressed()[pygame.K_a]:
        box_rect.left -= speed
    if pygame.key.get_pressed()[pygame.K_s]:
        box_rect.bottom += speed
    if pygame.key.get_pressed()[pygame.K_d]:
        box_rect.right += speed

    if speed <= 1:
        speed = 1
    if box_rect.right > 1600:
        box_rect.left = 1
    if box_rect.left < 1:
        box_rect.right = 1600
    if box_rect.top < 1:
        box_rect.bottom = 900
    if box_rect.bottom > 900:
        box_rect.top = 1

    if pygame.key.get_pressed()[pygame.K_0]:
        col = 'white'
    if pygame.key.get_pressed()[pygame.K_1]:
        col = 'red'
    if pygame.key.get_pressed()[pygame.K_2]:
        col = 'orange'
    if pygame.key.get_pressed()[pygame.K_3]:
        col = 'yellow'
    if pygame.key.get_pressed()[pygame.K_4]:
        col = 'green'
    if pygame.key.get_pressed()[pygame.K_5]:
        col = 'blue'
    if pygame.key.get_pressed()[pygame.K_6]:
        col = 'purple'

    if not pygame.key.get_pressed()[pygame.K_SPACE]:
        surface.blit(box,box_rect)

    if pygame.key.get_pressed()[pygame.K_x]:
        surface.fill('black')

    pygame.display.update()
    pygame.time.Clock().tick(speed*144)