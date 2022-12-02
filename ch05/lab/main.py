import pygame
from collections import defaultdict

# pygame.init()
# window = pygame.display.set_mode()
# font = pygame.font.Font(None, 50)

# upper_limit = 20
# iters = {}
# max = 0
# max_so_far = 0

# n = 101
# count = 0

# for value in range(2, upper_limit + 1):
#   count = 0
#   n = value
#   while (n != 1):
#     if (n % 2) == 0:
#       n = n//2
#     else:
#       n = n * 3 + 1
#     count = count + 1
#     print(n)
#   iters[value] = count
  
  #pygame.draw.lines(window, [200,200,255], False, (x,y))
  #pygame.display.flip()

display = pygame.display.set_mode((400, 400))

def algorithm(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        print(n)
        count += 1
    return count  

def make_dictionary(upper_Limit):
  max_val = 0
  max_x = 0
  upper_limit = upper_Limit
  lower_limit = 2
  iters = {}
  true_iters = []
  
  
  iters = defaultdict(list)
  for i in range(lower_limit, upper_limit):
      if algorithm(i) > max_val:
          max_val = algorithm(i)
          max_x = i
      iters[(i)].append((algorithm(i)))
      true_iters.append((int(i), int(algorithm(i))))
  return iters, max_val, true_iters, max_x

if __name__ == "__main__":
    pygame.init()
    upper_limit = 20
    lower_limit = 2
    iters, max_val, real_iters, max_x = make_dictionary(upper_limit)
    max_so_far = 0
    scale = 17
    scale_iters = [(x * scale, y * scale) for x, y in real_iters]
    aqua = (127,255,212)
  
    font = pygame.font.Font(None, 30)
    pygame.draw.lines(display, aqua, False, scale_iters)
    new_display = pygame.transform.flip(display, False, True)
    display.blit(new_display, (0, 0))
  
    message = "The maximum value is at " + str((max_x, max_val))
  
    msg = font.render(message, True, aqua)
    display.blit(msg, (10, 10))
  
    pygame.display.update()

