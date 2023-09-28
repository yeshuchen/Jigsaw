import pygame
import random
import time

pygame.init()

image = pygame.image.load("puzzle_image.jpg")

WIDTH, HEIGHT = image.get_size()

image = pygame.transform.scale(image, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Puzzle Game")
# Divide the image into 40 pieces
pieces = []
Pieces = []
for i in range(40):
    x = (i % 5) * (WIDTH // 5)
    y = (i // 5) * (HEIGHT // 8)
    rect = pygame.Rect(x, y, WIDTH // 5, HEIGHT // 8)
    piece = image.subsurface(rect)
    pieces.append([piece, i])
    Pieces.append([piece, i])

# Shuffle the pieces
# random.shuffle(pieces)
a114514=pieces[0]
pieces[0]=pieces[1]
pieces[1]=a114514
del a114514

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Set up the selected pieces
selected_piece_1 = None
selected_piece_2 = None

def check_win(pieces):
    return pieces == Pieces

win = False

print("欢迎来到这个简单的拼图游戏，在进行游戏前，请确保您阅读了游戏规则：https://github.com/yeshuchen/Jigsaw#readme")

clock.tick(120)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(pieces)):
                rect = pieces[i][0].get_rect()
                rect.x = (i % 5) * (WIDTH // 5)
                rect.y = (i // 5) * (HEIGHT // 8)
                if rect.collidepoint(pos):
                    if selected_piece_1 is None:
                        selected_piece_1 = i
                    elif selected_piece_2 is None:
                        selected_piece_2 = i

    # Draw the pieces
    screen.fill((255, 255, 255))
    for i in range(len(pieces)):
        rect = pieces[i][0].get_rect()
        rect.x = (i % 5) * (WIDTH // 5)
        rect.y = (i // 5) * (HEIGHT // 8)
        if selected_piece_1 == i:
            pygame.draw.rect(screen, (255, 0, 0), rect, 3)
        screen.blit(pieces[i][0], rect)

    # Swap the selected pieces
    if selected_piece_1 is not None and selected_piece_2 is not None:
        pieces[selected_piece_1], pieces[selected_piece_2] = pieces[selected_piece_2], pieces[selected_piece_1]
        selected_piece_1 = None
        selected_piece_2 = None
    # pygame.display.flip()
    # Check if the puzzle is complete
    if check_win(pieces) == True:
        win = True

    # Display "You Win!" message if the puzzle is complete
    if win:
        font = pygame.font.Font(None, 36)
        text_surface = font.render("You Win!", True, (255,0,0))
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        pygame.display.flip()
        screen.blit(text_surface, text_rect)
        running = False
    # Update the display
    pygame.display.flip()
    
    # Tick the clock
    clock.tick(60)
time.sleep(3)
pygame.quit()