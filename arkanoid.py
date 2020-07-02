# pong!
import pygame
from pygame import gfxdraw
from time import sleep

class Brick:
    "Draw Player 2"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # This is for collisions
        self.rect = pygame.Rect(self.x, self.y, 50, 20)

    def update(self):
        # when you update it will go to self.x and self.y
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 50, 20))


class Bar:
    "Draw Player 2"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 60, 10))
        self.rect = pygame.Rect(self.x, self.y, 60, 10)


class Ball:
    "Draw Player 2"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED

    def update(self):
        "The ball moves"
        global ball
        global ball_x, ball_y

        # sull'asse x Va verso sinistra
        if ball_x == "left":
            # sottraggo perchè vado a sinistra
            ball.x -= velx
            # se arriva a 10 rimbalza
            if ball.x < 10:
                ball_x = "right"
        # va in basso
        if ball_y == 'down':
            # allora aumenta y quando va in basso (parte da 0 in alto)
            ball.y += vel_y
        if ball_y == 'up':
            # quando va in alto tolgo
            ball.y -= vel_y
            # se arriva in cima rimbalza in basso
            if ball.y < 10:
                ball_y = 'down'
        # se va a destra aumenta x
        if ball_x == "right":
            ball.x += velx
            # a 480 rimbalza verso sinistra
            if ball.x > 480:
                ball_x = "left"
        gfxdraw.filled_circle(screen, ball.x, ball.y, 6, self.color)
        # gfxdraw.filled_circle(screen, ball.x, ball.y, 5, YELLOW)
        self.rect = pygame.Rect(self.x, self.y, 6, 6)


def reverse():
    global ball_x, velx, vel_y
    ball_x = "right" if ball_x == "left" else "right"



def collision():
    global ball, bar, ball_y, ball_x, vely, velx, mousedir, bricks
    global diff, lives, stage
    if ball.rect.colliderect(bar):
        pygame.mixer.Sound.play(s_coin)
        ball_y = "up"
        velx = 2 if diff > 0 else 1
        print(f"you hit with diff: {diff} vel_x = {velx}")
        # se colpisce a sinistra o destra
        # lr = (mousedir == "left" or mousedir == "right")
        # print(lr)
        # if lr:
        #     velx = 1
        #     vel_y = 2
        #     ball.color = GREEN
        # else:
        #     velx = 1
        #     vel_y = 1
        #     ball.color = RED


    for n, brick in enumerate(bricks):
        if ball.rect.colliderect(brick):
            pygame.mixer.Sound.play(s_brick)
            print("You hit a brick")
            if ball_y == "up":
                # the ball is lower than the brick of 20
                if ball.y == (brick.y + 20 - vel_y) :
                    ball_y = "down"
                # if the balls hit the brick on a side
                else:
                    if ball_x == "left":
                        ball_x = "right"
                    else:
                        ball_x = "left"
            elif ball_y == "down":
                if ball.y <= brick.y - 1:
                    ball_y = "up"
                else:
                    if ball_x == "left":
                        ball_x = "right"
                    else:
                        ball_x = "left"
            bricks.pop(n)
            if bricks == []:
                if stage < len(blist):
                    stage += 1
                    pygame.mixer.Sound.play(s_ready)
                else:
                    stage = 0
                bricks = create_bricks(blist[stage])

    if ball.y > 500:
        ball.xb, ball.y = 500, 300
        lives -= 1
        pygame.mixer.Sound.play(s_out)
        if lives == 0:
            pygame.mixer.Sound.play(s_over)
            sleep(2)
            pygame.quit()


def exit(event, loop):

    if event.type == pygame.QUIT:
        loop = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            loop = 0
    return loop


def create_bricks(blist):
    "The bricks scheme"
    blist = blist.splitlines()[1:]
    bricks = []
    h = 30
    w = 0
    for line in blist:
        for brick in line:
            if brick == "1":
                bricks.append(Brick(20 + w * 60, h))
            w += 1
            if w == 8:
                w = 0
                h += 30
    return bricks


def show_bricks():
    for brick in bricks:
        brick.update()

stage = 0
lives = 3
blist = ["""
10101010
01010101
""",

"""
11111111
01111110
00111100
""",

#diamond
"""
00011000
00111100
00111100
00011000

""",
"""
11110000
00001111
00001111
11110000
""",

"""
11001101
11111111
01111111
01010111
11111111
""",
"""
1111111
0000000
1111111
0000000
1111111
"""
]
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ball_x = 'left'
ball_y = 'down'
scorep1 = 0
scorep2 = 0
# speed horizzontal
velx = 1
# speed vertical
vel_y = 1


######################
#     sound
#####################
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)
pygame.mixer.set_num_channels(32)
# ===================================
s_coin = pygame.mixer.Sound('sound\\coin.wav')
s_out = pygame.mixer.Sound('sound\\out.wav')
s_brick = pygame.mixer.Sound('sound\\brick.wav')
s_ready = pygame.mixer.Sound('sound\\GetReady1.wav')
s_over = pygame.mixer.Sound('sound\\GameOver1.wav')

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")
startx = 0
bar = Bar(10, 480)
ball = Ball(100, 300)
bricks = create_bricks(blist[0])
background = pygame.image.load("img\\background.png").convert()
pygame.mouse.set_visible(False)
mousedir = "stop"
diff = 0
def mainloop():
    global startx, mousedir, diff
    pygame.mixer.Sound.play(s_ready)
    loop = 1
    while loop:
        screen.blit(background, (0, 0))
        # screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            loop = exit(event, loop)
        # This is the position of the mouse on the x axe
        posx = pygame.mouse.get_pos()[0]
        if posx > 10 and posx < 430:
            # il surface si muove come il mouse
            bar.x = posx
        ball.update()
        bar.update()
        collision()
        if startx > posx:
            mousedir = "left"
        elif startx < posx:
            mousedir = "right"
        else:
            mousedir = "stop"
        diff = abs(startx - posx)
        startx = posx
        show_bricks()
        pygame.display.update()
        clock.tick(240)

mainloop()
pygame.quit()
