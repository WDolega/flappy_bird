import pygame

import point


def game():
    run = True
    player = point.Player()
    win = True
    clock = 0
    score = 0
    pips = []
    cash = []
    background = point.Background()
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if clock >= 2:
            clock = 0
            pips.append(point.Object())
            pips.append(point.Pip())
            cash.append(point.Cash())
        player.tick_bird(keys)
        background.tick()
        background.draw(point.window)
        for p in pips:
            p.tick()
        for c in cash:
            c.tick()
        for p in pips:
            if p.x_cord < -53:
                pips.remove(p)
        for c in cash:
            if player.hitbox.colliderect(c.hitbox):
                cash.remove(c)
                score += 1
        # point.window.blit(background, (0, 0))
        # window.fill((32, 184, 214))
        player.draw()
        for c in cash:
            c.draw()
        for p in pips:
            p.draw()
        for p in pips:
            if p.hitbox.colliderect(player.hitbox):
                print("XD")
                player.hor_velocity = 0
                win = False
        if win:
            text_img = pygame.font.Font.render(point.game_font, f"Points: {score}", True, (255, 255, 255))
            text_img2 = pygame.font.Font.render(point.game_font2, f"Points: {score}", True, (0, 0, 0))
            point.window.blit(text_img2, (559, 99))
            point.window.blit(text_img, (560, 100))
        else:
            point.draw_text(point.window, point.game_font2, "DEFEAT", (255, 47, 0), (560, 100))
        if player.y_cord > 720:
            point.draw_text(point.window, point.game_font2, "DEFEAT", (255, 47, 0), (560, 100))
            print("NOT OK")
        # if score < 5:
        #     text_img = pygame.font.Font.render(game_font, f"Points: {score}", True, (255, 255, 255))
        #     text_img2 = pygame.font.Font.render(game_font2, f"Points: {score}", True, (0, 0, 0))
        #     window.blit(text_img2, (559, 99))
        #     window.blit(text_img, (560, 100))
        # else:
        #     text_vic = pygame.font.Font.render(game_font, "Victory", True, (37, 186, 37))
        #     window.blit(text_vic, (560, 300))
        pygame.display.update()


def main():
    game()


if __name__ == "__main__":
    main()
