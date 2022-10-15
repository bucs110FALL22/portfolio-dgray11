import pygame

pygame.init()
window = pygame.display.set_mode()
font = pygame.font.Font(None, 50)

upper_limit = 20
iters = {}
max = 0
max_so_far = 0

n = 101
count = 0

for value in range(2, upper_limit + 1):
  count = 0
  n = value
  while (n != 1):
    if (n % 2) == 0:
      n = n//2
    else:
      n = n * 3 + 1
    count = count + 1
    print(n)
  iters[value] = count
  #pygame.draw.lines(window, [200,200,255], False, (x,y))
  #pygame.display.flip()


