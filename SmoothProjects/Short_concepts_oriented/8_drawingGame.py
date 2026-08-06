import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

font = pygame.font.SysFont(None, 50)

running = True
while running:
    screen.fill((255, 255, 255)) # White background
    
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 150, 100)) # Red rectangle
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 60) # Blue circle
    
    text = font.render("Hello, Pygame!", True, (0, 0, 0))
    screen.blit(text, (250, 500))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()