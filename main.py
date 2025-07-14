import pygame
import sys

pygame.init()
game_font = pygame.font.Font(None , 25)

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("T_REX_RUN")

trex_img = pygame.image.load("assets/trex_img.png")
trex_img = pygame.transform.scale(trex_img, (80, 80))
trex_rect = trex_img.get_rect(midbottom = (80, 300))

cactus_img = pygame.image.load("assets/cactus1.png")
cactus_img = pygame.transform.scale(cactus_img, (50, 70))
cactus_rect = cactus_img.get_rect(midbottom = (900, 300))

gravity = 0
trex_movement = 0
jump_power = -20 # nagetive meens upword face
ground_level = 300
cactus_speed = 6

score = 0

game_active = True
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
  if game_active:
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_SPACE and trex_rect.bottom >= ground_level:
       trex_movement = jump_power
  else:
   if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      game_active = True
      cactus_rect.left = 800
      trex_rect.midbottom = (80, ground_level)
      trex_movement = 0

 if  game_active:
  trex_movement += 0.8
  trex_rect.y += trex_movement

  if trex_rect.bottom >= ground_level:
    trex_rect.bottom = ground_level

  cactus_rect.x -= cactus_speed
  if cactus_rect.right < 0:
    cactus_rect.left = 800

  if trex_rect.colliderect(cactus_rect):
    game_active = False

  screen.fill((255, 255, 255))
  screen.blit(trex_img, trex_rect)
  screen.blit(cactus_img, cactus_rect)
 
 else:
   screen.fill((200, 200, 200))
   game_over_serface = game_font.render("Game Over" , True ,(255, 0, 0))
   game_over_rect = game_over_serface.get_rect(center=(400, 200))
   screen.blit(game_over_serface, game_over_rect)
   restart_serface = game_font.render("Press space for restart!", True, (255, 255,255))
   restart_rect = restart_serface.get_rect(center=(400, 225))
   screen.blit(restart_serface, restart_rect)

 pygame.display.update()
