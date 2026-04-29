import pygame as py
import sys
import random, time
import persistence as db
from ui import *
from racer import Player, Enemy, PowerUp, Hazard, Coin

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Racer")
clock = py.time.Clock()
background = py.image.load("TSIS/TSIS3/assets/road.png")
accident = py.image.load("TSIS/TSIS3/assets/boom.png")
screen.blit(background, (0, 0))
fail_sound = py.mixer.Sound("TSIS/TSIS3/assets/boom.wav")
py.mixer.music.load("TSIS/TSIS3/assets/background.wav") #background music on repeat
py.mixer.music.play(-1)

class Game:
    def __init__(self):
        self.settings = db.get_settings()
        self.state = "MENU"
        self.username = "Johny"
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.coins_count = 0
        self.distance = 0
        base_speed = {"Easy": 3, "Medium": 5, "Hard": 8}
        self.game_speed = base_speed.get(self.settings.get('difficulty'), 5)
        self.player = Player(self.settings['car_color'])
        self.enemies = py.sprite.Group()
        self.coins = py.sprite.Group()
        self.powerups = py.sprite.Group()
        self.all_sprites = py.sprite.Group()
        self.all_sprites.add(self.player)
        self.active_powerup = None
        self.powerup_timer = 0
        self.shield_timer = 0

    def run(self):
        while True:
            if self.state == "MENU":
                self.main_menu()
            elif self.state == "GAME":
                self.play_game()
            elif self.state == "LEADERBOARD":
                self.show_leaderboard()
            elif self.state == "GAME_OVER":
                self.game_over_screen()

    def main_menu(self):
        screen.fill(WHITE)
        draw_text(screen, "Racer", 40, WIDTH//2, 100, RED, True)
        btn_play = Button("PLAY", 125, 200, 150, 50, GREEN)
        btn_lead = Button("SCORES", 125, 270, 150, 50, GRAY)
        btn_quit = Button("QUIT", 125, 340, 150, 50, BLACK)
        draw_text(screen, f"Name: {self.username}", 20, WIDTH//2, 180, BLACK, True)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if btn_play.is_clicked(pos): 
                    self.reset_game()
                    self.state = "GAME"
                if btn_lead.is_clicked(pos): 
                    self.state = "LEADERBOARD"
                if btn_quit.is_clicked(pos): 
                    py.quit()
                    sys.exit()
        for b in [btn_play, btn_lead, btn_quit]: 
            b.draw(screen, py.font.SysFont("timesnewroman", 20))
        py.display.update()

    def play_game(self):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        self.distance += 0.1
        self.score = int(self.distance) + (self.coins_count * 100)
        self.game_speed += 0.001 
        if self.player.shielded:
            current_time = py.time.get_ticks()
            if current_time - self.shield_timer > 5000:
                self.player.shielded = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        if random.randint(1, 60) == 1 and len(self.enemies) < 4:
            e = Enemy(self.game_speed)
            self.enemies.add(e)
            self.all_sprites.add(e)
        if random.randint(1, 120) == 1:
            c = Coin()
            self.coins.add(c)
            self.all_sprites.add(c)
        if random.randint(1, 300) == 1:
            p = PowerUp(random.choice(['Nitro', 'Shield']))
            self.powerups.add(p)
            self.all_sprites.add(p)
        self.player.move()
        self.enemies.update()
        self.coins.update()
        self.powerups.update()
        coins_collected = py.sprite.spritecollide(self.player, self.coins, True)
        if coins_collected:
            self.coins_count += len(coins_collected)
        powerups_collected = py.sprite.spritecollide(self.player, self.powerups, True)
        for p in powerups_collected:
            if p.type == 'Nitro':
                self.game_speed += 3 
            elif p.type == 'Shield':
                self.player.shielded = True
                self.shield_timer = py.time.get_ticks()
        enemies_hit = py.sprite.spritecollide(self.player, self.enemies, False)
        if enemies_hit:
            if self.player.shielded:
                self.player.shielded = False
                for e in enemies_hit:
                    e.kill()
            else:
                py.mixer.Sound(fail_sound).play()
                accident_rect = accident.get_rect(center=self.player.rect.center)
                screen.blit(accident, accident_rect)
                py.display.update()
                time.sleep(2)
                db.save_score(self.username, self.score, int(self.distance))
                self.state = "GAME_OVER"
                return
        for entity in self.all_sprites:
            screen.blit(entity.image, entity.rect)
        draw_text(screen, f"SCORE: {self.score}", 15, 10, 10, BLACK)
        draw_text(screen, f"COINS: {self.coins_count}", 15, 10, 40, (180, 150, 0))
        draw_text(screen, f"SPEED: {int(self.game_speed)}", 15, 10, 70, BLACK)
        if self.player.shielded:
            draw_text(screen, "SHIELD ACTIVE!", 15, WIDTH//2, 20, (0, 255, 255), True)
        py.display.update()
        clock.tick(FPS)

    def game_over_screen(self):
        screen.fill(RED)
        draw_text(screen, "WASTED!", 40, WIDTH//2, 150, WHITE, True)
        draw_text(screen, f"Your Score: {self.score}", 25, WIDTH//2, 220, WHITE, True)
        draw_text(screen, f"Coins Collected: {self.coins_count}", 20, WIDTH//2, 260, WHITE, True)
        draw_text(screen, f"Distance: {int(self.distance)}m", 20, WIDTH//2, 300, WHITE, True)
        btn_retry = Button("RETRY", 125, 350, 150, 50, BLACK)
        btn_menu = Button("MENU", 125, 420, 150, 50, GRAY)
        btn_scores = Button("SCORES", 125, 490, 150, 50, (100, 100, 200))
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if btn_retry.is_clicked(pos): 
                    self.reset_game()
                    self.state = "GAME"
                if btn_menu.is_clicked(pos): 
                    self.state = "MENU"
                if btn_scores.is_clicked(pos):
                    self.state = "LEADERBOARD"
        btn_retry.draw(screen, py.font.SysFont("timesnewroman", 18))
        btn_menu.draw(screen, py.font.SysFont("timesnewroman", 18))
        btn_scores.draw(screen, py.font.SysFont("timesnewroman", 18))
        py.display.update()

    def show_leaderboard(self):
        screen.fill(WHITE)
        draw_text(screen, "TOP SCORES", 30, WIDTH//2, 50, BLACK, True)
        scores = db.get_leaderboard()
        if not scores:
            draw_text(screen, "No scores yet!", 20, WIDTH//2, 150, GRAY, True)
        else:
            draw_text(screen, "Rank", 18, 50, 100, BLACK)
            draw_text(screen, "Name", 18, 150, 100, BLACK)
            draw_text(screen, "Score", 18, 250, 100, BLACK)
            draw_text(screen, "Distance", 18, 330, 100, BLACK)
            for i, entry in enumerate(scores[:10]): 
                y_pos = 150 + i * 35
                draw_text(screen, f"{i+1}", 18, 50, y_pos, BLACK)
                draw_text(screen, entry['name'][:10], 18, 150, y_pos, BLACK)
                draw_text(screen, str(entry['score']), 18, 250, y_pos, BLACK)
                draw_text(screen, str(entry.get('distance', 0)), 18, 330, y_pos, BLACK)
        btn_back = Button("BACK", 125, 500, 150, 50, BLACK)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if btn_back.is_clicked(py.mouse.get_pos()):
                    self.state = "MENU"
        btn_back.draw(screen, py.font.SysFont("timesnewroman", 18))
        py.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()