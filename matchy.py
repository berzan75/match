import pygame
pygame.init()
s=pygame.display.set_mode((900,900))
s.fill((255,255,255))

pygame.display.update()

subway=pygame.image.load("subway.png")
temple_run=pygame.image.load("temple_run.png")
ludo=pygame.image.load("ludo.png")
candy_crush=pygame.image.load("candy_crush.jpg")
roblox=pygame.image.load("roblox.png")
roblox1=pygame.transform.scale(roblox,(60,60))
minecraft=pygame.image.load("minecraft.jpg")
minecraft1=pygame.transform.scale(minecraft,(60,60))
plants_vs_zombies=pygame.image.load("plants_vs_zombies.jpg")
plants_vs_zombies1=pygame.transform.scale(plants_vs_zombies, (60, 60))
brawl_stars=pygame.image.load("brawl_stars.jpg")
brawl_stars1=pygame.transform.scale(brawl_stars,(60,60))

s.blit(subway,(150, 100))
s.blit(temple_run,(150, 200))
s.blit(ludo, (150, 300))
s.blit(candy_crush, (150, 400))
s.blit(minecraft1,(150, 500))
s.blit(roblox1,(150, 600))
s.blit(brawl_stars1, (150, 700))
s.blit(plants_vs_zombies1, (150, 800))

font=pygame.font.SysFont("Times New Roman",30)

text=font.render("Ludo", True,(0,0,0))
text1=font.render("Subway Surfer",True, (0,0,0))
text2=font.render("Candy Crush",True, (0,0,0))
text3=font.render("Temple run",True ,(0,0,0))
text4=font.render("minecraft", True,(0,0,0))
text5=font.render("brawl stars",True, (0,0,0))
text6=font.render("plants vs zombies",True, (0,0,0))
text7=font.render("roblox",True ,(0,0,0))

s.blit(text, (350, 100))
s.blit(text1, (350, 200))
s.blit(text2, (350, 300))
s.blit(text3, (350, 400))
s.blit(text4, (350, 500))
s.blit(text5, (350, 600))
s.blit(text6, (350, 700))
s.blit(text7, (350, 800))

run=True

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
    if event.type == pygame.QUIT:
      
        pygame.quit()
        exit(0)
