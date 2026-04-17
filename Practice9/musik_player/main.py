import pygame as py
from player import MusicPlayer

py.init()
screen = py.display.set_mode((800, 400))
font = py.font.SysFont("timesnewroman", 20)
playlist = ["Practice9\musik_player\musik\jjba_2_op.mp3", "Practice9\musik_player\musik\jjba_chase.mp3", "Practice9\musik_player\musik\mary_go_round_of_life.mp3"]
player = MusicPlayer(playlist)
player.load()
clock = py.time.Clock()

running = True
while running:
    screen.fill((255, 250, 205))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_p:
                player.play()
            elif event.key == py.K_s:
                player.stop()
            elif event.key == py.K_n:
                player.next()
            elif event.key == py.K_b:
                player.previous()
            elif event.key == py.K_q:
                running = False
    track = player.get_curr()
    text1 = font.render(f"Current track: {track}", True, (25, 25, 112))
    text2 = font.render(f"Current time: {py.mixer.music.get_pos() / 1000}", True, (25, 25, 112))
    text3 = font.render("P (play) | S (stop) | N (next track) | B (previous track) | Q (quit)", True, (199, 21, 133))
    screen.blit(text1, (20, 50))
    screen.blit(text2, (20, 150))
    screen.blit(text3, (20, 250))
    py.display.flip()
    clock.tick(60)
py.quit()