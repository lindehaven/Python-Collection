"""B I R D I E

Author:
  Lars Lindehaven

Based on:
  Dodger

Changes from Dodger:
  Game name is now B I R D I E instead of Dodger.
  There are in total 10 different changes made:
   1. Background music courtesy of www.bensound.com
   2. Splashing sound when raindrops are hit
   3. Background image with rain clouds
   7. Player has PLAYER_LIVES lives
   5. Player character is an animated bird and that should avoid raindrops
   8. A higher level is reached when score reaches LEVEL_SCORE for current level
   9. Difficulty increases with higher levels
  13. Large code blocks are refactored into functions
  14. Top score is read from and written to the TOP_SCORE_FILE file
  19. Welcome screen with a cute chicken.
  Changes are marked with four hash marks (####) in the code.

TODO:
  Get rid of all the pylint warnings.
  Get rid of all the 'global' variables in functions.
  Add unit tests.
"""

import pickle, pygame, random, sys
from pygame.locals import *

NAME_OF_THE_GAME = 'B I R D I E' ####
TOP_SCORE_FILE = 'topscore.p' ####
BACKGROUND_SOUND = 'background.mp3' ####
LOST_LIFE_SOUND = 'lostlife.wav' ####
GAME_OVER_SOUND = 'gameover.wav'
GAME_IMAGE = 'chicken.png' ####
PLAYER_IMAGE_0 = 'birdie0.png' ####
PLAYER_IMAGE_1 = 'birdie1.png' ####
CLOUDS_IMAGE = 'clouds.jpg' ####
RAINDROP_IMAGE = 'raindrop.png' ####

FRAMES_PER_SECOND = 40
LEVEL_SCORE = 500 ####
WINDOW_WIDTH = 499
WINDOW_HEIGHT = 499
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)
WHITE_COLOR = (255, 255, 255)
RAINDROP_WIDTH_MIN = 10
RAINDROP_WIDTH_MAX = 20
RAINDROP_HEIGHT_FACTOR = 1.625 ####
RAINDROP_MIN_SPEED = 4
RAINDROP_MAX_SPEED = 8
RAINDROP_ADD_RATE = 8
PLAYER_MOVE_RATE = 5
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 42
PLAYER_LIVES = 3 ####


def init_game(): ####
    global game_clock
    global window_surface
    global font
    global score
    global top_score
    pygame.init()
    game_clock = pygame.time.Clock()
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(NAME_OF_THE_GAME)
    pygame.mouse.set_visible(False)
    font = pygame.font.SysFont('comicsansms', 32) ####
    score = 0
    top_score = 0


def init_images(): ####
    global game_image
    global game_rectangle
    global player_images
    global player_rectangles
    global clouds_image
    global clouds_rectangle
    global raindrop_image
    game_image = pygame.image.load(GAME_IMAGE) ####
    game_rectangle = game_image.get_rect() ####
    player_images = [] ####
    player_rectangles = [] ####
    player_images.append(pygame.transform.scale(
                                        pygame.image.load(PLAYER_IMAGE_0),
                                        (PLAYER_WIDTH, PLAYER_HEIGHT))
                                                ) ####
    player_rectangles.append(player_images[-1].get_rect()) ####
    player_images.append(pygame.transform.scale(
                                        pygame.image.load(PLAYER_IMAGE_1),
                                        (PLAYER_WIDTH, PLAYER_HEIGHT))
                                                ) ####
    player_rectangles.append(player_images[-1].get_rect()) ####
    clouds_image = pygame.image.load(CLOUDS_IMAGE) ####
    clouds_rectangle = clouds_image.get_rect() ####
    raindrop_image = pygame.image.load(RAINDROP_IMAGE)


def init_audio():
    global lost_life_sound
    global game_over_sound
    lost_life_sound = pygame.mixer.Sound(LOST_LIFE_SOUND) ####
    game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
    pygame.mixer.music.load(BACKGROUND_SOUND)
    pygame.mixer.music.set_volume(0.1) ####
    pygame.mixer.music.play(-1, 0.0)


def start_game():
    global lives
    global player
    global score
    global raindrops
    global player_rectangles
    global move_left
    global move_right
    global move_up
    global move_down
    global reverse_cheat
    global slow_cheat
    global raindrop_add_counter
    lives = PLAYER_LIVES
    player = 0
    score = 0
    level = 0
    raindrops = []
    for player_rect in player_rectangles:
        player_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)
    move_left = move_right = move_up = move_down = False
    reverse_cheat = slow_cheat = False
    raindrop_add_counter = 0
    pygame.mixer.music.play(-1, 0.0)


def end_game(): ####
    pygame.time.wait(1000) ####
    pygame.mixer.music.stop()
    game_over_sound.play()
    display_end_screen()
    game_over_sound.stop()


def display_start_screen(): ####
    window_surface.fill(WHITE_COLOR)
    window_surface.blit(game_image, game_rectangle)
    display_text('Press a key to start', font, YELLOW_COLOR, window_surface,
                 (WINDOW_WIDTH / 2) - 150, WINDOW_HEIGHT - 170)
    display_text('Music: www.bensound.com', font, BLACK_COLOR, window_surface,
                 (WINDOW_WIDTH / 2) - 190, WINDOW_HEIGHT - 40)
    pygame.display.update()
    wait_for_player_to_press_key()


def display_end_screen(): ####
    display_text('GAME OVER', font, RED_COLOR, window_surface,
                 (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 2))
    display_text('Press a key to play', font, RED_COLOR, window_surface,
                 (WINDOW_WIDTH / 3) - 50, (WINDOW_HEIGHT / 2) + 50)
    pygame.display.update()
    wait_for_player_to_press_key()


def display_game_stats(): ####
    display_text('High: %s' % (top_score), font, WHITE_COLOR,
                 window_surface, 10, 0)
    display_text('Score: %s' % (score), font, WHITE_COLOR,
                 window_surface, 10, 40)
    display_text('Level: %s' % (level), font, WHITE_COLOR,
                 window_surface, WINDOW_WIDTH - 180, 0) ####
    display_text('Lives: %s' % (lives), font, WHITE_COLOR,
                 window_surface, WINDOW_WIDTH - 180, 40) ####

def display_clouds(): ####
    window_surface.blit(clouds_image, clouds_rectangle)


def display_player(player_image, player_rectangle): ####
    window_surface.blit(player_image, player_rectangle)


def display_raindrops(raindrops): ####
    for raindrop in raindrops:
        window_surface.blit(raindrop['surf'], raindrop['rect'])


def display_text(text, font, color, surface, x, y): ####
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def read_top_score(): ####
    global top_score
    top_score = pickle.load(open(TOP_SCORE_FILE, 'rb')) ####


def write_top_score(): ####
    global top_score
    if score > top_score:
        top_score = score
        pickle.dump(top_score, open(TOP_SCORE_FILE, 'wb')) ####


def handle_points_and_difficulty():
    global score
    global level
    global raindrop_add_rate
    global player
    score += 1
    level = 1 + score // LEVEL_SCORE ####
    raindrop_add_rate = RAINDROP_ADD_RATE - level // RAINDROP_ADD_RATE ####
    player = (player + 1) % len(player_images) ####


def handle_pygame_event(player_rectangle): ####
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            key_was_pressed(event)
        elif event.type == KEYUP:
            key_was_released(event)
        elif event.type == MOUSEMOTION:
            for player_rect in player_rectangles:
                player_rect.move_ip(event.pos[0] - player_rect.centerx,
                                    event.pos[1] - player_rect.centery)


def wait_for_player_to_press_key(): ####
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def key_was_pressed(event): ####
    global score
    global slow_cheat
    global move_left
    global move_right
    global move_down
    global move_up
    if event.key == ord('z'):
        score -= 2
        reverse_cheat = True
    elif event.key == ord('x'):
        score -= 2
        slow_cheat = True
    elif event.key == K_LEFT or event.key == ord('a'):
        move_right = False
        move_left = True
    elif event.key == K_RIGHT or event.key == ord('d'):
        move_left = False
        move_right = True
    elif event.key == K_UP or event.key == ord('w'):
        move_down = False
        move_up = True
    elif event.key == K_DOWN or event.key == ord('s'):
        move_up = False
        move_down = True


def key_was_released(event): ####
    global score
    global reverse_cheat
    global slow_cheat
    global move_left
    global move_right
    global move_down
    global move_up
    if event.key == ord('z'):
        reverse_cheat = False
    elif event.key == ord('x'):
        slow_cheat = False
    elif event.key == K_ESCAPE:
        terminate()
    elif event.key == K_LEFT or event.key == ord('a'):
        move_left = False
    elif event.key == K_RIGHT or event.key == ord('d'):
        move_right = False
    elif event.key == K_UP or event.key == ord('w'):
        move_up = False
    elif event.key == K_DOWN or event.key == ord('s'):
        move_down = False


def move_player(player_rectangle): ####
    if move_left and player_rectangle.left > 0:
        player_rectangle.move_ip(-1 * PLAYER_MOVE_RATE, 0)
    elif move_right and player_rectangle.right < WINDOW_WIDTH:
        player_rectangle.move_ip(PLAYER_MOVE_RATE, 0)
    elif move_up and player_rectangle.top > 0:
        player_rectangle.move_ip(0, -1 * PLAYER_MOVE_RATE)
    elif move_down and player_rectangle.bottom < WINDOW_HEIGHT:
        player_rectangle.move_ip(0, PLAYER_MOVE_RATE)
    pygame.mouse.set_pos(player_rectangle.centerx, player_rectangle.centery)


def add_raindrops_inside_window(raindrops): ####
    global raindrop_add_counter
    if not reverse_cheat and not slow_cheat:
        raindrop_add_counter += 1
    if raindrop_add_counter > raindrop_add_rate:
        raindrop_add_counter = 0
        raindrop_width = random.randint(RAINDROP_WIDTH_MIN, RAINDROP_WIDTH_MAX)
        raindrop_height = int(raindrop_width * RAINDROP_HEIGHT_FACTOR)
        new_raindrop = {
            'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH-raindrop_width),
                                0 - raindrop_height,
                                raindrop_width, raindrop_height),
            'speed': random.randint(RAINDROP_MIN_SPEED, RAINDROP_MAX_SPEED),
            'surf': pygame.transform.scale(raindrop_image,
                                           (raindrop_width, raindrop_height)),
        }
        raindrops.append(new_raindrop)


def move_raindrops(raindrops): ####
    for b in raindrops:
        if not reverse_cheat and not slow_cheat:
            b['rect'].move_ip(0, b['speed'])
        elif reverse_cheat:
            b['rect'].move_ip(0, -5)
        elif slow_cheat:
            b['rect'].move_ip(0, 1)


def remove_raindrops_outside_window(raindrops): ####
    for b in raindrops[:]:
        if b['rect'].top > WINDOW_HEIGHT:
            raindrops.remove(b)


def player_has_hit_raindrop(player_rectangle, raindrops):
    for b in raindrops:
        if player_rectangle.colliderect(b['rect']):
            lost_life_sound.set_volume(1.0) ####
            lost_life_sound.play() ####
            raindrops.remove(b) ####
            return True
    return False


def alive(): ####
    global lives
    if player_has_hit_raindrop(player_rectangles[player], raindrops):
        lives -= 1
        if lives < 1:
            write_top_score()
            return False
    return True


def terminate():
    write_top_score() ####
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


print('Hello from Lars Lindehaven. https://larslindehaven.wordpress.com/') ####
init_game()
init_images()
init_audio()
display_start_screen()
read_top_score()

while True:

    start_game()

    while True:
        handle_points_and_difficulty()
        handle_pygame_event(player_rectangles[player])
        move_player(player_rectangles[player])
        add_raindrops_inside_window(raindrops)
        move_raindrops(raindrops)
        remove_raindrops_outside_window(raindrops)
        display_clouds()
        display_player(player_images[player], player_rectangles[player])
        display_raindrops(raindrops)
        display_game_stats()
        pygame.display.update()
        game_clock.tick(FRAMES_PER_SECOND)
        if not alive():
            break

    end_game()
