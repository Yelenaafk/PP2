import pygame, sys
from tools import *
import datetime

pygame.init()
BLUE, PINK, YELLOW, GREEN = (70, 130, 180), (219, 112, 147), (255, 215, 0), (107, 142, 35)
BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (230, 230, 230)
WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pro Paint")
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(WHITE)
COLOR = BLACK
THICKNESS = 5
TOOL = 'brush'
LMBpressed = False
prevX, prevY = 0, 0
clock = pygame.time.Clock()
text_tool = Text_tool()

def draw_figure(target_surf, color, start_pos, end_pos, current_tool):
    x1, y1 = start_pos
    x2, y2 = end_pos
    if current_tool == 'rectangle':
        pygame.draw.rect(target_surf, color, calculate_rect(x1, y1, x2, y2), THICKNESS)
    elif current_tool == 'rhombus':
        pygame.draw.polygon(target_surf, color, calculate_rhombus(x1, y1, x2, y2), THICKNESS)
    elif current_tool == 'square':
        pygame.draw.rect(target_surf, color, calculate_square(x1, y1, x2, y2), THICKNESS)
    elif current_tool == 'circle':
        center, radius = calculate_circle(x1, y1, x2, y2)
        pygame.draw.circle(target_surf, color, center, radius, THICKNESS)
    elif current_tool == 'righttriangle':
        pygame.draw.polygon(target_surf, color, calculate_right_triangle(x1, y1, x2, y2), THICKNESS)
    elif current_tool == 'equilateraltriangle':
        pygame.draw.polygon(target_surf, color, calculate_equilateral_triangle(x1, y1, x2, y2), THICKNESS)
    elif current_tool == 'line':
        pygame.draw.line(target_surf, color, (x1, y1), (x2, y2), THICKNESS)

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b: COLOR = BLUE
            if event.key == pygame.K_p: COLOR = PINK
            if event.key == pygame.K_g: COLOR = GREEN
            if event.key == pygame.K_y: COLOR = YELLOW
            if event.key == pygame.K_h: COLOR = BLACK
            if event.key == pygame.K_1: TOOL = 'brush'
            if event.key == pygame.K_2: TOOL = 'rectangle'
            if event.key == pygame.K_3: TOOL = 'square'
            if event.key == pygame.K_4: TOOL = 'rhombus'
            if event.key == pygame.K_5: TOOL = 'circle'
            if event.key == pygame.K_6: TOOL = 'righttriangle'
            if event.key == pygame.K_7: TOOL = 'equilateraltriangle'
            if event.key == pygame.K_8: TOOL = 'eraser'
            if event.key == pygame.K_9: TOOL = 'line'
            if event.key == pygame.K_0: TOOL = 'fill_tool'
            if event.key == pygame.K_t: TOOL = 'text_tool'
            if event.key == pygame.K_q: THICKNESS = 2
            if event.key == pygame.K_a: THICKNESS = 5
            if event.key == pygame.K_z: THICKNESS = 10
            if event.key == pygame.K_c: base_layer.fill(WHITE)
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_LCTRL):
                save_image(base_layer)
            if text_tool.active:
                res = text_tool.keydown(event)
                if res == "confirm":
                    text_tool.finalize(base_layer, COLOR)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_pos[1] > 85: # Ignore clicks inside the UI menu
                LMBpressed = True
                prevX, prevY = event.pos
                if TOOL == 'fill_tool':
                    fill_tool(base_layer, prevX, prevY, COLOR)
                elif TOOL == 'text_tool':
                    text_tool.activate(event.pos)
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX, currY = event.pos
            if TOOL == 'brush':
                pygame.draw.line(base_layer, COLOR, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
            elif TOOL == 'eraser':
                pygame.draw.circle(base_layer, WHITE, (currX, currY), THICKNESS)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if LMBpressed:
                if TOOL not in ['brush', 'eraser', 'fill_tool', 'text_tool']:
                    draw_figure(base_layer, COLOR, (prevX, prevY), event.pos, TOOL)
                LMBpressed = False

    screen.blit(base_layer, (0, 0))
    if LMBpressed and TOOL not in ['brush', 'eraser', 'fill_tool', 'text_tool']:
        draw_figure(screen, COLOR, (prevX, prevY), mouse_pos, TOOL)
    if text_tool.active:
        text_tool.draw_preview(screen, COLOR)
    pygame.draw.rect(screen, GRAY, (0, 0, 550, 85))
    small_font = pygame.font.SysFont("timesnewroman", 14)
    ui_text = [
        f"COLORS: B (Blue) | P (Pink) | Y (Yellow) | G (Green) | H (Black)    [CURRENT: {TOOL.upper()}]",
        "TOOLS: 1 (Brush) | 2 (Rect) | 3 (Sq) | 4 (Rhomb) | 5 (Circ) | 6 (R-Tri) | 7 (E-Tri) | 8 (Eraser)",
        "OTHER: 9 (Line) | 0 (Fill) | T (Text) | C (Clear) | Ctrl+S (Save)",
        f"SIZE: Q (2px) | A (5px) | Z (10px)    Thickness: {THICKNESS}"
    ]
    for i, line in enumerate(ui_text):
        rendered = small_font.render(line, True, BLACK)
        screen.blit(rendered, (10, 5 + (i * 20)))
    pygame.display.flip()
    clock.tick(60)