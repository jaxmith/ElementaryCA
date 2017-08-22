import pygame

#CONSTANTS
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WIDTH = 1600
HEIGHT = 1000
PIXEL_HEIGHT = 1
PIXEL_WIDTH = 1
WINDOW_SIZE = [WIDTH, HEIGHT]
global ruleset

#grid generation
grid = []
for row in range(WIDTH // PIXEL_WIDTH):
    grid.append(0)

#initial state
grid[len(grid) // 2] = 1

#ruleset generation
ruleset = []
byte = input("Enter in a rule number (0-255): ")
text = "Rule " + byte
byte = bin(int(byte))
byte = byte[2:]     #cuts off "0b"

while len(byte) < 8:
    byte = "0" + byte
           
byte = byte[::-1]   #reverses string
for bit in byte:
    ruleset.append(int(bit))
    
print(ruleset)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Elementary Cellular Automata")
clock = pygame.time.Clock()
screen.fill(WHITE)
font = pygame.font.Font(None, 80)
text_render = font.render(text, 0, BLACK)
screen.blit(text_render, (10, 10))

#converts 3 positions into bits for binary ruleset
def rules(a, b, c):
    binary = str(a) + str(b) + str(c)
    binary = int(binary, 2)
    return ruleset[binary]
    
#main loop
done = False
y = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    x = 0
    for row in range(len(grid)):
            if grid[row] == 1:
                pygame.draw.rect(screen, BLACK, [x * PIXEL_WIDTH,
                                                 y * PIXEL_HEIGHT,
                                                 PIXEL_WIDTH,
                                                 PIXEL_HEIGHT])
            x += 1
    y += 1

    #if reached bottom, restart, else calculate next line
    if y > (HEIGHT // PIXEL_HEIGHT):
        pygame.time.wait(3000)
        grid = []
        for row in range(WIDTH // PIXEL_WIDTH):
            grid.append(0)
        grid[len(grid) // 2] = 1
        y = 0
        screen.fill(WHITE)
        screen.blit(text_render, (10, 10))
    else:
        nextgrid = []
        for row in range(len(grid)):
            nextgrid.append(0)
        
        for row in range(len(grid)):
            if row > 0 and row < len(grid)-1:
                left = grid[row-1]
                center = grid[row]
                right = grid[row+1]
                nextgrid[row] = rules(left, center, right)

        grid = nextgrid

    clock.tick(60)
    pygame.display.flip()


pygame.quit()
