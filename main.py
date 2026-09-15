import random  # noqa: I001
import sys

import pygame


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звездное поле 3D")
clock = pygame.time.Clock()

NUM_STARS = 300
MAX_Z = 1000
SPEED = 5
STAR_COLOR = (255, 255, 255)


# x, y, z, color, radius
stars = []
for _ in range(NUM_STARS):
    stars.append(
        [
            random.randint(-WIDTH, WIDTH),
            random.randint(-HEIGHT, HEIGHT),
            random.randint(1, MAX_Z),
            STAR_COLOR,
            random.randint(1, 3),
        ]
    )


def main():
    global SPEED
    while True:
        screen.fill((0, 0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        dx = (mouse_x - WIDTH // 2) * 0.05
        dy = (mouse_y - HEIGHT // 2) * 0.05

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            SPEED += 0.5
        if keys[pygame.K_DOWN]:
            SPEED -= 0.5

        for star in stars:
            star[2] -= SPEED

            star[0] -= dx * (SPEED * 0.2)
            star[1] -= dy * (SPEED * 0.2)

            if star[2] <= 0:
                star[0] = random.randint(-WIDTH, WIDTH)
                star[1] = random.randint(-HEIGHT, HEIGHT)
                star[2] = MAX_Z
                star[4] = random.randint(1, 3)

            fov = 400
            screen_x = int(fov * star[0] / star[2]) + WIDTH // 2
            screen_y = int(fov * star[1] / star[2]) + HEIGHT // 2

            radius = int((star[4] * fov) / star[2])

            if 0 <= screen_x < WIDTH and 0 <= screen_y < HEIGHT:
                pygame.draw.circle(screen, STAR_COLOR,
                                   (screen_x, screen_y), radius)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
