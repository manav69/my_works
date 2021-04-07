import pygame

pygame.init()
pygame.mixer.music.load("C:/Users/Manav/Downloads/avengers_infinitywar.mp3")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Naagin")
done = False
isblue = True
x = 30
y = 30
isjump = False
countjump = 10

while not done:
    clock.tick(60)  # or use pygame.time.delay(millisec) will block execution untill 1/60th seconds have passed
    screen.fill('black')  # fills the screen with black colour before making rectangles
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            isblue = not isblue

    pressed = pygame.key.get_pressed()
    if not isjump:
      if pressed[pygame.K_UP] and y >= 3: y -= 3
      if pressed[pygame.K_DOWN] and y < 440: y += 3
      if pressed[pygame.K_LEFT] and x >= 3: x -= 3
      if pressed[pygame.K_RIGHT] and x < 640: x += 3
      if pressed[pygame.K_s] :
          isjump = True
    else:
        if countjump >= -10:
            neg = 1
            if countjump < 0:
                neg = -1
            y -= (countjump ** 2) * 0.5 * neg
            countjump -= 1
        else:
            isjump = False
            countjump = 10

    if isblue:
        color = (0, 120, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.draw.circle(screen,"red",(350-x,250-y
                                     ),100)

    pygame.display.flip()
pygame.quit()
