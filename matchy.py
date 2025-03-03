import pygame

s=pygame.display.set_mode((600,600))
s.fill((255,255,255))

pygame.display.update()

subway=pygame.image.load("subway.png")
temple_run=pygame.image.load("temple_run.png")
ludo=pygame.image.load("ludo.png")
candy_crush=pygame.image.load("candy_crush.jpg")

s.blit(subway,(150, 100))
s.blit(temple_run,(150, 200))
s.blit(ludo, (150, 300))
s.blit(candy_crush, (150, 400))

font=pygame.font.SysFont("Times New Roman",30)

text=font.render("Ludo", True,(0,0,0))
text1=font.render("Subway Surfer",True, (0,0,0))
text2=font.render("Candy Crush",True, (0,0,0))
text3=font.render("Temple run",True ,(0,0,0))

s.blit(text, (350, 100))
s.blit(text1, (350, 200))
s.blit(text2, (350, 300))
s.blit(text3, (350, 400))


while True:
    event=pygame.event.poll()

    if event.type ==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(s, (0,0,0), (pos), 10,0)
        pygame.display.update()
    elif event.type== pygame.MOUSEBUTTONUP:
        pos1=pygame.mouse.get_pos()
        pygame.draw.line(s, (0,0,0), (pos), (pos1),5 )
        pygame.draw.circle(s, (0,0,0), (pos1), 10,0)
        pygame.display.update()