import pygame, sys, random
pygame.init()

clock = pygame.time.Clock()
S_WIDTH, S_HEIGHT = 400, 900
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

running = True
menu_active = True
game_active = False

class Player():
    def __init__(self, x):
        self.player_obj = pygame.Rect(0, 800, 100, 100)
        self.x = x
        self.player_speed = 5

    def update(self, x):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.player_speed

        if keys[pygame.K_d]:
            self.x += self.player_speed

        self.x = max(0, min(S_WIDTH - self.player_obj.width, self.x))
        self.player_obj.x = self.x

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.player_obj)

player = Player(0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False

    screen.fill((0, 0, 0))
    player.draw()
    player.update(player.x)
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")

pygame.quit()