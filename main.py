import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("First Game Screen")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

rect_width, rect_height = 200, 100
rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = (320, 240)

font = pygame.font.SysFont(None, 36)
text = font.render("Hello, Pygame!", True, BLACK)
text_rect = text.get_rect(center=(320, 100))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, rect, 2)

    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()