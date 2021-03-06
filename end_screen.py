from global_objects import *
from global_funcs import *
from constants import *
from highscore import *
# checking for user inputs


def events():
    global option
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and (pressed[pygame.K_RALT] or pressed[pygame.K_LALT]):
                os._exit(0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_d:
                option = (option + 1) % 3
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_a:
                option = (option + 2) % 3
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                return True  # to indicate that player has made a choice
        if event.type == pygame.QUIT:
            os._exit(0)
        return False


def highscore(score):
    pass


def end_screen(screen, win, score, seconds_first, seconds_second, minutes_first, minutes_second, clock):
    global option

    # initialising ball for this screen
    ball = Ball(scr_width / 2, scr_height - wall_brick_height)
    new_high = highscore(score)
    option = 0
    random_hint = random.randint(0, 7)  # getting value for random hint
    while True:

        # time passed
        delta_time = clock.get_time() / 10

        # if player won the game, theme like he is out of the captivity
        if win:
            screen.fill(white)
            disp_text(screen, "Sweet Open Air!", (scr_width / 2, scr_height / 4), end_title_text_win,
                      peace_green)
            # displaying menu options
            if option == 0:
                disp_text(screen, "Get Dirty Again", (scr_width / 2,
                                                      scr_height / 2 + 80), menu_item_text_selected, black)
            else:
                disp_text(screen, "Get Dirty Again", (scr_width / 2,
                                                      scr_height / 2 + 80), menu_item_text, light_black)

            if option == 1:
                disp_text(screen, "Rest A While", (scr_width / 2,
                                                   scr_height / 2 + 130), menu_item_text_selected, black)
            else:
                disp_text(screen, "Rest A While", (scr_width / 2,
                                                   scr_height / 2 + 130), menu_item_text, light_black)

            if option == 2:
                disp_text(screen, "Food Stinks There!", (scr_width / 2,
                                                         scr_height / 2 + 180), menu_item_text_selected, black)
            else:
                disp_text(screen, "Food Stinks There!", (scr_width / 2,
                                                         scr_height / 2 + 180), menu_item_text, light_black)

            # drawing box around options
            pygame.draw.rect(screen, black, (scr_width / 2 -
                                             250, scr_height / 2 + 40, 500, 190), 2)
            pygame.draw.rect(screen, black, (scr_width / 2 -
                                             242, scr_height / 2 + 48, 484, 174), 2)

        # if player caught
        else:
            screen.fill(black)
            draw_walls(screen, wall_brick_width, wall_brick_height)
            disp_text(screen, "Dragged Behind Bars!!", (scr_width / 2,
                                                        scr_height / 4), end_title_text_lose, blood_red)

            # ball updates
            ball.menu_screen_move(delta_time)
            ball.check_collide_lose()
            ball.check_collide_wall()
            ball.draw(screen)

            # displaying menu options
            if option == 0:
                disp_text(screen, "Pull It Again", (scr_width / 2,
                                                    scr_height / 2 + 80), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Pull It Again", (scr_width / 2,
                                                    scr_height / 2 + 80), menu_item_text, grey)

            if option == 1:
                disp_text(screen, "Change Disguise", (scr_width / 2,
                                                      scr_height / 2 + 130), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Change Disguise", (scr_width / 2,
                                                      scr_height / 2 + 130), menu_item_text, grey)

            if option == 2:
                disp_text(screen, "Give Up?", (scr_width / 2,
                                               scr_height / 2 + 180), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Give Up?", (scr_width / 2,
                                               scr_height / 2 + 180), menu_item_text, grey)

            # drawing box around options
            pygame.draw.rect(screen, white, (scr_width / 2 -
                                             250, scr_height / 2 + 40, 500, 190), 3)
            pygame.draw.rect(screen, white, (scr_width / 2 -
                                             242, scr_height / 2 + 48, 484, 174), 2)

        # display score
        disp_text(screen, "score : ", (scr_width / 4 - 65,
                                       scr_height / 8 - 30), end_screen_text, grey)
        disp_text(screen, str(score), (scr_width / 4, scr_height /
                                       8 + 2 - 30), end_screen_number, light_green)

        # display time
        disp_text(screen, "pursuit : ", (3 * scr_width / 4,
                                         scr_height / 8 - 30), end_screen_text, grey)
        disp_text(screen, str(minutes_second) + str(minutes_first) + ":" + str(seconds_second) + str(seconds_first),
                  (3 * scr_width / 4 + 85, scr_height / 8 + 2 - 30), end_screen_number, light_red)

        # display message
        if option == 0:
            disp_text(screen, "Press Enter To Restart",
                      (scr_width / 2, scr_height / 2 + 300), message_text, red)
        elif option == 1:
            disp_text(screen, "Press Enter To Go To Menu",
                      (scr_width / 2, scr_height / 2 + 300), message_text, red)
        elif option == 2:
            disp_text(screen, "Press Enter To Quit Game",
                      (scr_width / 2, scr_height / 2 + 300), message_text, red)

        # displaying random hint
        disp_text(screen, "\""+hint_message[random_hint % 7]+"\"",
                  (scr_width / 2, scr_height / 4 + 100), quote_text, orange)

        if events():
            if option == 2:
                os._exit(0)
            else:
                return option + 2
        pygame.display.update()
        clock.tick(FPS)
