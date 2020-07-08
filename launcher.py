import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont("Arial", 24)


def write(text, x, y, color="Coral",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(500 // 2, y))
    screen.blit(text, text_rect)
    return text

def menu():
    loop = 1
    while loop:
        # screen.blit(background, (0, 0))
        write("ARKAGAME", 200, 120, color="yellow")
        write("A Game by Giovanni Gatto", 200, 20, color="red")
        write("Follow me on youtube", 200, 140)
        write("and pythonprogramming.altervista.org", 200, 160)
        write("CHOOSE YOUR GAME", 200, 300, color="green")
        write("1 - Arkanoid Monocrome", 150, 340)
        write("2 - Arkanoid Policrome", 150, 360)
        write("3 - Arkanoid tiny", 150, 380)
        write("July 2020", 150, 480, color="gray")
        #screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_1:
                    import arkagame1
                if event.key == pygame.K_2:
                    import arkagame2
                if event.key == pygame.K_3:
                    import tiny_02

                if event.key == pygame.K_SPACE:
                    mainloop()
        pygame.display.update()

menu()

pygame.quit()
sys.exit()
