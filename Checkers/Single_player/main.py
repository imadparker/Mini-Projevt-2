import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")



#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (52, 78, 84)

#load button images
start_img = pygame.image.load("images/button_single_player.png").convert_alpha()
quit_img = pygame.image.load("images/button_multi_player.png").convert_alpha()

#create button instances
start_button = button.Button(250, 200, start_img, 1)
quit_button = button.Button(250, 375, quit_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((206, 236, 243))

  if start_button.draw(screen):
        run = False
        menu_state = "main"
  if quit_button.draw(screen):
        run = False
        
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        game_paused = True
        if event.type == pygame.QUIT:
           run = False

  pygame.display.update()

pygame.quit()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()