# arkanoid
import pygame
from pygame import gfxdraw
import os
from random import choice, randrange

'''
To add a new type of game
- createbricks5()
- restart5()
in the while loop of the mainmenu
            elif event.key == pygame.K_5:
                game = 5
                restart5()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                screen.fill((0, 0, 0))
                mainloop()

in collision 1 line 135
                if game == 5:
                    bricks = create_bricks5()
in text

    if game == 4:
        scorefile = "score4.txt"

In the menu

write("4 - Arkanoid tiny 2", 150, 400)
'''

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (255, 255, 255)
COLORS = (BLACK, RED, GREEN, YELLOW, ORANGE, BLUE, GRAY)

class Brick:
    "One brick class"

    def __init__(self, x, y, w=50, h=20, color=GREEN):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        # This is for collision1
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        # when you update it will go to self.x and self.y
        # bar.x is constantly equal to the mouse position in the while loop
        pygame.draw.rect(screen, self.color, self.rect)



class Bar:
    "This is the bar class"

    def __init__(self, x, y, w=60, h=10):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, RED, self.rect)


velocity = 3
class Ball:
    "Draw Player 2"

    global velocity

    def __init__(self, x, y, size=10):
        self.x = x
        self.y = y
        self.color = RED
        self.counter = pygame.time.get_ticks()
        self.size = size

    def update(self):
        "The ball moves"
        global ball, velocity
        global ball_x, ball_y, game

        # sull'asse x Va verso sinistra
        
        if pygame.time.get_ticks() - self.counter >= velocity:
            self.counter = pygame.time.get_ticks()
            if ball_x == "left":
                # sottraggo perchè vado a sinistra
                ball.x -= velx
                # se arriva a 10 rimbalza
                if ball.x < 10:
                    pygame.mixer.Sound.play(s_wall)
                    ball_x = "right"
            # va in basso
            if ball_y == 'down':
                # allora aumenta y quando va in basso (parte da 0 in alto)
                ball.y += vel_y
            if ball_y == 'up':
                # quando va in alto tolgo
                ball.y -= vel_y
                # se arriva in cima rimbalza in basso
                if ball.y < 50:
                    pygame.mixer.Sound.play(s_wall)
                    ball_y = 'down'
            # se va a destra aumenta x
            if ball_x == "right":
                ball.x += velx
                # a 480 rimbalza verso sinistra
                if ball.x > 490:
                    pygame.mixer.Sound.play(s_wall)
                    ball_x = "left"

        gfxdraw.filled_circle(screen, ball.x, ball.y, self.size // 2, self.color)
        # This is to check the collisions
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)




def collision1():
    global ball, bar, ball_y, ball_x, vely, velx, mousedir, bricks
    global diff, lives, stage, score, loop, game, randomstage, velocity
    if ball.rect.colliderect(bar):
        print("sulla barra: ", ball.x - bar.x)
        print("Diff=", diff)
        pygame.mixer.Sound.play(hitbar)
        # when the ball hit the bar, it goes up
        ball_y = "up"
        if (mousedir == "left" and ball_x == "right"):
            ball_x = "left"
        if (mousedir == "right" and ball_x == "left"):
            ball_x = "right"

    for n, brick in enumerate(bricks):
        if ball.rect.colliderect(brick):
            # screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), brick.rect)
            screen.blit(show_fps(color="Black"), (12, 10))
            score += 20
            screen.blit(show_fps(), (12, 10))
            pygame.mixer.Sound.play(hitbrick)
            # print("You hit a brick")
            if ball_y == "up":
                # the ball is lower than the brick of 20
                if ball.y == (brick.y + brick.h - vel_y):
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
            if ball.color != "red":
                bricks.pop(n)

            # STAGE FINITO
            if bricks == []:
                set_score()
                stage += 1
                score += 50
                screen.fill((0, 0, 0))
                ball.y = 300
                ball.x = 100
                velocity = 3
                pygame.mixer.Sound.play(s_ready)
                if randomstage == 1:
                    game = randrange(1,5)
                if game == 1:
                    bricks = create_bricks1()
                if game == 2:
                    bricks = create_bricks2()
                if game == 3:
                    bricks = create_bricks3()
                if game == 4:
                    bricks = create_bricks4()
                if game == 5:
                    game = randrange(1, 5)
                    if game == 1:
                        create_bricks1()
                    if game == 2:
                        create_bricks2()
                    if game == 3:
                        create_bricks3()
                        ball.size, bar.w = 6, 30
                    if game == 4:
                        ball.size, bar.w = 6, 30
                        create_bricks4()
                show_bricks()

    if ball.y > 510:
        ball.x, ball.y = 500, 300
        lives -= 1
        pygame.mixer.Sound.play(s_out)
        velocity = 4
        ball.color = GREEN
        if lives < 0:
            pygame.mixer.Sound.play(s_over)
            set_score()
            score = 0
            stage = 1
            ball_y = 'down'
            ball_x = 'left'
            back_to_menu()




def create_bricks1():
    "The bricks scheme for game 1 - double simmetry"
    blist = []
    templ = []
    for n in range(3):
        riga = [str(choice([0, 1])) for x in range(4)]
        riga2 = riga[::-1]
        riga = riga + riga2
        # print(riga)
        templ.append(riga)
    templ.append(templ[2])
    templ.append(templ[1])
    templ.append(templ[0])
    for riga in templ:
        blist.append("".join(riga))
    bricks = []
    h = 50
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


def create_bricks2():
    "The bricks scheme for game 2"
    blist = []
    for n in range(randrange(5,16)):
        riga = [str(choice([0, 1])) for x in range(4)]
        riga2 = riga[::-1]
        riga = riga + riga2
        # print(riga)
        blist.append("".join(riga))
    bricks = []
    h = 50
    w = 0
    for line in blist:
        rndclr = randrange(100, 255), randrange(100, 255), randrange(100, 255),
        for brick in line:
            if brick == "1":
                bricks.append(Brick(50 + w * 51, h, color=rndclr))
            w += 1
            if w == 8:
                w = 0
                h += 21
    return bricks


column = 10
def create_bricks3():
    "The bricks scheme"
    global column
    blist = []
    for n in range(randrange(10, 16)):
        riga = [str(choice([0, 1])) for x in range(column)]
        riga2 = riga[::-1]
        riga = riga + riga2
        # print(riga)
        blist.append("".join(riga))

    bricks = []
    h = 50
    w = 0
    for line in blist:
        rndclr = randrange(0, 100), randrange(50, 255), randrange(250, 255)
        for brick in line:
            if brick == "1":
                bricks.append(Brick(6 + w * 26, h, w=25, h=10, color=rndclr))
            w += 1
            if w == column * 2:
                w = 0
                h += 11
    return bricks


def create_bricks4():
    "The bricks scheme"
    global column
    blist = []
    templ = []
    for n in range(randrange(3,16)):
        riga = [str(choice([0, 1])) for x in range(column)]
        riga2 = riga[::-1]
        riga = riga + riga2
        templ.append(riga)
    templ.append(templ[2])
    templ.append(templ[1])
    templ.append(templ[0])
    for riga in templ:
        blist.append("".join(riga))
    bricks = []
    h = 50
    w = 0
    for line in blist:
        randomcolor = randrange(0, 255), randrange(0, 255), randrange(0, 255),
        for brick in line:
            if brick == "1":
                bricks.append(Brick(6 + w * 51, h, w=30, h=10, color=randomcolor))
            w += 1
            if w == column * 2:
                w = 0
                h += 21
    return bricks


def score_text():
    global game, randomstage

    if game == 1:
        scorefile = "score1.txt"
    if game == 2:
        scorefile = "score2.txt"
    if game == 3:
        scorefile = "score3.txt"
    if game == 4:
        scorefile = "score4.txt"
    if game == 5:
        scorefile = "score5.txt"

    return scorefile


def get_score():
    global scoremax, game

    scorefile = score_text()
    # Se il file esiste
    if scorefile in os.listdir():
        with open(scorefile, "r") as file:
            # Se non c'è scritto nulla, ci scrive 100
            if file.readlines() == []:
                with open(scorefile, "w") as filewrite:
                    filewrite.write("100")
                    scoremax = 100
            # Se ci sono dati, li legge e mi memorizza in score max
            else:
                with open(scorefile, "r") as file:
                    # print(file.readlines())
                    scoremax = int(file.readlines()[0])
    # Se non c'è il file, lo crea e ci scrive 100
    else:
        with open(scorefile, "w") as file:
            file.write("100")


def set_score():
    global score, randomstage

    scorefile = score_text()
    with open(scorefile, "r") as file:
        scoremax = int(file.readlines()[0])
    if score > scoremax:
        with open(scorefile, "w") as file:
            file.write(str(score))


def restart_common():
    "Common restart"
    global score, lives, stage

    stage = 1
    score = 0
    lives = 3
    screen.fill((0, 0, 0))
    ball.x, ball.y = 250, 300
    ball.update()
    bar.update()
    ball.size = 10
    bar.w = 60


def restart1():
    global bricks
    "MONOCHROME VERSION"
    restart_common()
    bricks = create_bricks1()
    pygame.display.set_caption("MonoArcha")


def restart2():
    global bricks
    "POLYCHROME VERSION"
    restart_common()
    bricks = create_bricks2()
    show_bricks()
    pygame.display.set_caption("PolyArcha")


def restart3():
    global bricks
    "TINY VERSION 1"
    pygame.display.set_caption("Tiny 1")
    restart_common()
    ball.size = 6
    bar.w = 30
    bricks = create_bricks3()
    show_bricks()


def restart4():
    global bricks
    "TINY VERSION 2"
    pygame.display.set_caption("Tiny 2")
    restart_common()
    ball.size = 6
    bar.w = 30
    bricks = create_bricks4()
    show_bricks()


# ============================= SHOW BRICKS ================ #
def show_bricks():
    pygame.draw.line(screen, "red", (0, 10), (500, 10), 2)
    pygame.draw.line(screen, "red", (0, 40), (500, 40), 2)
    for brick in bricks:
        brick.update()
    screen.blit(barrier, (0, 0))
    screen.blit(barrier, (495, 0))
# ========================================================== #

def show_fps(color="Coral"):
    global score, scoremax, stage, randrange, font2
    if randrange:
        rnd = "Mode: Rnd"
    else:
        rnd = ""
    fps = f"Max: {scoremax} Lives: {lives} Stage: {stage} Score: {score}"
    fps_text = font2.render(fps, 1, pygame.Color(color))

    return fps_text


def write(text, x, y, color="Coral",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(500 // 2, y))
    screen.blit(text, text_rect)
    return text


def back_to_menu():
    set_score()
    screen.fill((0, 0, 0))
    mainmenu()

# =================================================================

def mainloop():
    global startx, mousedir, diff, game, velocity

    pygame.mixer.Sound.play(s_ready)
    show_bricks()
    # screen.fill((0, 0, 0))
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    get_score()
    # increase velocity after a while
    times = pygame.time.get_ticks()
    loop2 = 1
    velocity = 4
    screen.blit(show_fps(color="CORAL"), (12, 10))
    while loop2:
        # check if the time has passed to increase velocity
        if score % 1000 == 0:
            velocity = 3
            times = pygame.time.get_ticks()
            ball.color = GREEN
        if velocity > 0:
            if pygame.time.get_ticks() - times > 20000:
                velocity -= 1
                if velocity == 2:
                    ball.color = YELLOW
                if velocity == 1:
                    ball.color = GRAY
                times = pygame.time.get_ticks()

        pygame.draw.rect(screen, (0, 0, 0), (bar.x, bar.y, bar.w, bar.h))
        gfxdraw.filled_circle(screen, ball.x, ball.y, ball.size // 2, (0, 0, 0))
        # keys = pygame.key.get_pressed()
        posx = pygame.mouse.get_pos()[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                set_score()
                loop2 = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    set_score()
                    # pygame.event.set_grab(False)
                    loop2 = 0
                if event.key == pygame.K_m:
                    back_to_menu()
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_ESCAPE:
                    loop2 = 0
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game = 1
                    restart1()
                elif event.key == pygame.K_2:
                    game = 2
                    restart2()
                elif event.key == pygame.K_3:
                    game = 3
                    restart3()
                elif event.key == pygame.K_4:
                    game = 4
                    restart4()
                elif event.key == pygame.K_5:
                    randomstage = 1
                    game = 5
                    game2 = randrange(1, 5)
                    if game2 == 1:
                        restart1()
                    if game2 == 2:
                        restart2()
                    if game2 == 3:
                        restart3()
                    if game2 == 4:
                        restart4()
                # Next game
                # elif event.key == pygame.K_6:
                #     game = 6
                #     restart6()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                    screen.fill((0, 0, 0))
                    mainloop()
        # This is the position of the mouse on the x axe

        if pygame.mouse.get_pos()[1] > 400:
            bar.y = pygame.mouse.get_pos()[1]

        if posx > 10 and posx < 430 + 60 - bar.w:
            # il surface si muove come il mouse
            bar.x = posx
        diff = startx - posx
        mousedir = check_mouse_dir(diff)
        startx = posx
        ball.update()

        bar.update()
        collision1()
        pygame.display.update()
        clock.tick(360)
    #pygame.quit()


def check_mouse_dir(diff):
    if diff < 0:
        mousedir = "right"
    elif diff > 0:
        mousedir = "left"
    else:
        mousedir = ""
    return mousedir






randomstage = 0
def mainmenu():
    "The menu to choose among different games"
    
    global game, randomstage
    
    
    screen.fill((0, 0, 0))
    write("ARKAGAME", 200, 50, color="yellow")
    write("A Game by Giovanni Gatto", 200, 120, color="red")
    write("Follow me on youtube", 200, 140)
    write("and pythonprogramming.altervista.org", 200, 160)
    write("CHOOSE YOUR GAME", 200, 300, color="green")
    write("1 - Arkanoid Monochrome", 150, 340)
    write("2 - Arkanoid Polichrome", 150, 360)
    write("3 - Arkanoid tiny", 150, 380)
    write("4 - Arkanoid tiny 2", 150, 400)
    write("5 - RANDONOID", 150, 420)
    # write("4 - Arkanoid tiny 2", 150, 400)
    write("July 2020", 150, 480, color="gray")
    loop = 1
    while loop:
        # screen.blit(background, (0, 0))
        # keys = pygame.key.get_pressed()
        #ui = pygame.event.wait()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game = 1
                    restart1()
                elif event.key == pygame.K_2:
                    game = 2
                    restart2()
                elif event.key == pygame.K_3:
                    game = 3
                    restart3()
                elif event.key == pygame.K_4:
                    game = 4
                    restart4()
                elif event.key == pygame.K_5:
                    randomstage = 1
                    game = 5
                    game2 = randrange(1, 5)
                    if game2 == 1:
                        restart1()
                    if game2 == 2:
                        restart2()
                    if game2 == 3:
                        restart3()
                    if game2 == 4:
                        restart4()
                # Next game
                # elif event.key == pygame.K_6:
                #     game = 6
                #     restart6()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                    screen.fill((0, 0, 0))
                    mainloop()
                if event.key == pygame.K_ESCAPE:
                    loop = 0
            # Put this in line with for event ...
            pygame.display.update()
    pygame.quit()

# costants

lives = 3

ball_x = 'left'
ball_y = 'down'
# speed horizzontal
velx = 1
# speed vertical
vel_y = 1
######################
#     sound          #
######################
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)
pygame.mixer.set_num_channels(32)
# =========================== ([ sounds ]) ============
hitbar = pygame.mixer.Sound('sound\\hitbar2.wav')
s_out = pygame.mixer.Sound('sound\\outspeech.wav')
hitbrick = pygame.mixer.Sound('sound\\hitbrick.wav')
s_ready = pygame.mixer.Sound('sound\\ready.wav')
s_over = pygame.mixer.Sound('sound\\over.wav')
s_wall = pygame.mixer.Sound('sound\\wall.wav')

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("ArkaGame 5.0 by pythonprogramming.altervista.org")

clock = pygame.time.Clock()
startx = 0

background = pygame.image.load("img\\background.png").convert()
barrier = pygame.image.load("img\\barrier.png").convert()

mousedir = "stop"
diff = 0
score = 0
font2 = pygame.font.SysFont("Arial", 20)

scoremax = 0

font = pygame.font.SysFont("Arial", 24)
bar = Bar(10, 480)
ball = Ball(100, 300)


mainmenu()
# mainloop()