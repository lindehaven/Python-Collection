'''Onboard Computer Display Unit (OBCDU)

Author : Lars Lindehaven
Date   : 2019-06-11
'''
# pylint: disable=global-statement,invalid-name,too-many-arguments

# Imports
import pygame
import pygame.locals

# Constants
NAME = 'Better Made Vehicle - Onboard Computer'
FONT = 'verdana'
FPS = 40
WW = 800
WH = 450
BACK = (0, 0, 0)
WARN = (255, 0, 0)
FORE = (63, 63, 255)

# Globals
g_win = None
g_font1 = None
g_font2 = None
g_font3 = None
g_td = 0 # travelled_distance
g_rd = 0 # remaining_distance
g_cs = 0 # current_speed
g_as = 0 # average_speed
g_ap = 0 # average_power
g_at = 0 # accumulated_time
g_re = 0 # remaining_energy

def _init():
    global g_win
    global g_font1
    global g_font2
    global g_font3
    pygame.init()
    g_win = pygame.display.set_mode((WW, WH))
    pygame.display.set_caption(NAME)
    pygame.mouse.set_visible(False)
    g_font1 = pygame.font.SysFont(FONT, 20)
    g_font2 = pygame.font.SysFont(FONT, 40)
    g_font3 = pygame.font.SysFont(FONT, 80)
    g_win.fill(BACK)
    _text('Travelled Distance [km]', g_font1, FORE, g_win, 20, WH-90)
    _text('Remaining Distance [km]', g_font1, FORE, g_win, WW-290, WH-90)
    _text('Current Speed [km/h]', g_font1, FORE, g_win, WW//2-120, 20)
    _text('Average Speed [km/h]', g_font1, FORE, g_win, 20, 20)
    _text('Average Power [kW]', g_font1, FORE, g_win, WW-240, 20)
    _text('Travelled Time [s]', g_font1, FORE, g_win, 20, WH-190)
    _text('Remaining Energy [kWh]', g_font1, FORE, g_win, WW-290, WH-190)
    pygame.display.update()

def _text(text, font, col, surf, x, y):
    textobj = font.render(text, 1, col)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surf.blit(textobj, textrect)

def _time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

def _display(travelled_distance,
             remaining_distance,
             current_speed,
             average_speed,
             average_power,
             skid_warning,
             spin_warning,
             accumulated_time,
             remaining_energy):

    global g_win
    global g_td
    global g_rd
    global g_cs
    global g_as
    global g_ap
    global g_at
    global g_re

    travelled_distance /= 1000
    remaining_distance /= 1000

    _text('{:08.1f}'.format(g_td), g_font2, BACK, g_win, 25, WH-60)
    g_td = travelled_distance
    _text('{:08.1f}'.format(g_td), g_font2, FORE, g_win, 25, WH-60)

    _text('{:08.1f}'.format(g_rd), g_font2, BACK, g_win, WW-230, WH-60)
    g_rd = remaining_distance
    _text('{:08.1f}'.format(g_rd), g_font2, FORE, g_win, WW-230, WH-60)

    _text('{:03d}'.format(g_cs), g_font3, BACK, g_win, WW//2-90, 50)
    g_cs = current_speed
    _text('{:03d}'.format(g_cs), g_font3, FORE, g_win, WW//2-90, 50)

    _text('{:03d}'.format(g_as), g_font2, BACK, g_win, 25, 50)
    g_as = average_speed
    _text('{:03d}'.format(g_as), g_font2, FORE, g_win, 25, 50)

    _text('{:03d}'.format(g_ap), g_font2, BACK, g_win, WW-110, 50)
    g_ap = average_power
    _text('{:03d}'.format(g_ap), g_font2, FORE, g_win, WW-110, 50)

    if skid_warning:
        _text('SKID', g_font2, WARN, g_win, 25, WH-260)
    else:
        _text('SKID', g_font2, BACK, g_win, 25, WH-260)

    if spin_warning:
        _text('SPIN', g_font2, WARN, g_win, WW-135, WH-260)
    else:
        _text('SPIN', g_font2, BACK, g_win, WW-135, WH-260)

    _text(_time(g_at), g_font2, BACK, g_win, 25, WH-160)
    g_at = accumulated_time
    _text(_time(g_at), g_font2, FORE, g_win, 25, WH-160)

    _text('{:03d}'.format(g_re), g_font2, BACK, g_win, WW-115, WH-160)
    g_re = remaining_energy
    _text('{:03d}'.format(g_re), g_font2, FORE, g_win, WW-115, WH-160)

    pygame.display.update()


_init()
