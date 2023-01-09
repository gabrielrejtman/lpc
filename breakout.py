import pygame
# creating the initial screen and defining some variables
pygame.init()
pygame.mixer.init()

WIDTH = 893
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

score = 0
balls = 1
ball_speed = 6

paddle_width = 50
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

brick_sound = pygame.mixer.Sound('bricksound.wav')
paddle_sound = pygame.mixer.Sound('paddlesound.wav')
wall_sound = pygame.mixer.Sound('wallsound.wav')

# creating a class for the Bricks (tool that allows us to create a code 'template' with instances)


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def paddle_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def paddle_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.speed = [ball_speed, ball_speed]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self):
        self.speed[0] = self.speed[0]
        self.speed[1] = -self.speed[1]


# paddle design and staying in the middle of the screen
paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65
# ball design
ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5

bricks_list = pygame.sprite.Group()
# brick dimensions and the gap between them
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    # defining the blocks of the first edges
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the rest of the red blocks
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
            if 1 < j < 4:
                if i == 0:
                    # defining the blocks of the orange edge
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the rest of the orange blocks
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the blocks of the green edge
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the rest of the green blocks
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the blocks of the yellow edge
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)
                    # defining the rest of the yellow blocks
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    bricks_list.add(brick)


bricks()

all_sprites_list.add(paddle)
all_sprites_list.add(ball)


def run_game(score, balls):
    step = 0

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # when left_arrow is pressed, go left
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.paddle_left(10)
        # when right arrow is pressed, go right
        if keys[pygame.K_RIGHT]:
            paddle.paddle_right(10)

        all_sprites_list.update()
        # in case it collides with the upper wall, it changes its direction and the sound effect plays
        if ball.rect.y < 40:
            ball.speed[1] = -ball.speed[1]
            wall_sound.play()
        # in case it collides with side wall, it changes its direction and the sound effect plays
        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.speed[0] = -ball.speed[0]
            wall_sound.play()
        # in case
        if ball.rect.x <= wall_width:
            ball.speed[0] = -ball.speed[0]
            wall_sound.play()
        # if the ball pass through the paddle, the user will lose it and another one will appear
        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.speed[1] = ball.speed[1]
            balls += 1
            # in case you lost all your 3 balls, the game is over
            if balls == 4:
                font = pygame.font.SysFont('Arial', 70, True, False)
                text = font.render("GAME OVER", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)  # wait for 2 second until it closes the game
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x += ball.speed[0]
            ball.rect.y -= ball.speed[1]
            ball.bounce()
            paddle_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball, bricks_list, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()  # when you break a block, it bounces back and plays the sound effect
            if len(brick_collision_list) > 0:
                step += 1
                # gradually increasing speed
                for i in range(0, 448, 28):
                    if step == i:
                        ball.speed[0] += 1
                        ball.speed[1] += 1
            if 380.5 > brick.rect.y > 338.5:
                score += 1
                brick.kill()
            elif 338.5 > brick.rect.y > 294:
                score += 3
                brick.kill()
            elif 294 > brick.rect.y > 254.5:
                score += 5
                brick.kill()
            else:
                score += 7
                brick.kill()
            # if no more bricks, the game is over
            if len(bricks_list) == 0:
                font = pygame.font.SysFont('Arial', 70, True, False)
                text = font.render("YOU WON", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                all_sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        screen.fill(BLACK)

        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
        pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2)
                                                                           - 1, HEIGHT], wall_width)
        # down below, the designs aspects that compose the game
        # blue rectangle in the white wall
        pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        # red blocks in the white wall
        pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5], [(wall_width / 2) - 1, 212.5 + 2
                                                                      * brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
        # orange blocks in the white wall
        pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
        # green blocks in the white wall
        pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
        # yellow blocks in the white wall
        pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
        # score and 'lives' on screen
        font = pygame.font.SysFont('Arial', 70, True, False)
        text = font.render(str(f"{score:03}"), True, WHITE)  # score format
        screen.blit(text, (80, 120))  # score position on screen
        text = font.render(str(balls), True, WHITE)
        screen.blit(text, (520, 41))  # 'lives' position on screen
        text = font.render('000', True, WHITE)
        screen.blit(text, (580, 120))
        text = font.render('1', True, WHITE)
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


run_game(score, balls)
