import pygame
import button
import card

# Initialize Pygame
pygame.init()

#Make colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (250, 231, 83)
PURPLE = (102, 50, 152)
LIGHT_PURPLE = (122, 70, 172)
LIGHT_BLUE = (93, 226, 231)
GREEN = (125, 218, 88)
RED = (228, 8, 10)

#Set up the display
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("SET game")

#Create font for text
Big_font = pygame.font.Font(None, 250)
font = pygame.font.Font(None, 55)
Small_font = pygame.font.Font(None, 40)

#Create user event
Display_new_cards = pygame.USEREVENT + 1
Display_chosen_cards = pygame.USEREVENT + 2

#load images
exit_img = pygame.image.load('Exit_button.png').convert_alpha()
easy_img = pygame.image.load('Easy_button.png').convert_alpha()
medium_img = pygame.image.load('Medium_button.png').convert_alpha()
hard_img = pygame.image.load('Hard_button.png').convert_alpha()
impossible_img = pygame.image.load('Impossible_button.png').convert_alpha()
instructions_img = pygame.image.load('Instructions.png').convert_alpha()
rules_img = pygame.image.load('rules.png').convert_alpha()
return_begin_img = pygame.image.load('Return_begin.png').convert_alpha()
return_game_img = pygame.image.load('Return_game.png').convert_alpha()
exit_pause_img = pygame.image.load('Exit_pause.png').convert_alpha()
stack_img = pygame.image.load('Set_stack.png').convert_alpha()
submit_img = pygame.image.load('submit_button.png').convert_alpha()

#create buttons
return_begin_button = button.Button(800, 320, return_begin_img, 0.2)
return_game_button = button.Button(800, 190, return_game_img, 0.2)
exit_pause_button = button.Button(800, 450, exit_pause_img, 0.2)
rules_button = button.Button(35, 95, rules_img, 1)
exit_button = button.Button(1, 1, exit_img, 0.04)
easy_button = button.Button(320, 170, easy_img, 0.2)
medium_button = button.Button(320, 300, medium_img, 0.2)
hard_button = button.Button(320, 430, hard_img, 0.2)
impossible_button = button.Button(320, 560, impossible_img, 0.2)
instructions_button = button.Button(1030, 10, instructions_img, 0.05)
stack_button = button.Button(775, 115, stack_img, 0.2)
submit_button = button.Button(740, 535, submit_img, 0.5)

#create text and rectangles
end_screen_rect = pygame.Rect(50, 50, 1000, 700)
you_win = Big_font.render('You won!', True, GREEN)
you_win_shade = Big_font.render('You won!', True, BLACK)
you_lose = Big_font.render('You lost!', True, RED)
you_lose_shade = Big_font.render('You lost!', True, BLACK)
it_is_a_draw = Big_font.render("It's a draw!", True, LIGHT_BLUE)
it_is_a_draw_shade = Big_font.render("It's a draw!", True, BLACK)
press_any_key = font.render('Press any key to continue', True, WHITE)
your_score = font.render('Your score: ', True, WHITE)
computer_score = font.render('Computer score: ', True, WHITE)
you_have_to_choose_3_cards = Small_font.render('You have to choose 3 cards!', True, WHITE)
Main_menu = font.render('Choose your difficulty', True, WHITE)
too_slow = font.render('Your turn has passed, the computer gets to try', True, WHITE)
Player = font.render('Player:', True, WHITE)
Computer = font.render('Computer:', True, WHITE)
score_board = pygame.Rect(710, 300, 355, 200)
selected_rect1 = pygame.Rect(92, 55, 120, 220)
selected_rect2 = pygame.Rect(92, 290, 120, 220)
selected_rect3 = pygame.Rect(92, 525, 120, 220)
selected_rect4 = pygame.Rect(227, 55, 120, 220)
selected_rect5 = pygame.Rect(227, 290, 120, 220)
selected_rect6 = pygame.Rect(227, 525, 120, 220)
selected_rect7 = pygame.Rect(362, 55, 120, 220)
selected_rect8 = pygame.Rect(362, 290, 120, 220)
selected_rect9 = pygame.Rect(362, 525, 120, 220)
selected_rect10 = pygame.Rect(497, 55, 120, 220)
selected_rect11 = pygame.Rect(497, 290, 120, 220)
selected_rect12 = pygame.Rect(497, 525, 120, 220)
exit_rect = pygame.Rect(12, 15, 58, 50)

#Create necessary time variables
time_left_int = 0
time_while_paused = 0
unpaused_time = 0
paused_time = 0

#intialising settings
computer_turn = False
time_paused = False
select_cards = True
reset_game = True
running = True
#start game-loop
while running:
    #reset the game.
    if reset_game:
        reset_game = False
        #create stack of cards in number form
        stack = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        stack.append([i, j, k, l])

        #create stack of cards in word form
        dict_colour = {1:'green', 2:'purple', 3:'red'}
        dict_symbol = {1:'diamond', 2:'oval', 3:'squiggle'}
        dict_shading = {1:'empty', 2:'filled', 3:'shaded'}
        stack_name = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        stack_name.append(dict_colour[i] + dict_symbol[j] + dict_shading[k] + str(l))
                        
        #create random cards and their corresponding image
        card1 = card.Card.random(stack, stack_name)
        card1_img = pygame.image.load('kaarten/' + card1[1] + '.gif').convert_alpha()
        card2 = card.Card.random(stack, stack_name)
        card2_img = pygame.image.load('kaarten/' + card2[1] + '.gif').convert_alpha()
        card3 = card.Card.random(stack, stack_name)
        card3_img = pygame.image.load('kaarten/' + card3[1] + '.gif').convert_alpha()
        card4 = card.Card.random(stack, stack_name)
        card4_img = pygame.image.load('kaarten/' + card4[1] + '.gif').convert_alpha()
        card5 = card.Card.random(stack, stack_name)
        card5_img = pygame.image.load('kaarten/' + card5[1] + '.gif').convert_alpha()
        card6 = card.Card.random(stack, stack_name)
        card6_img = pygame.image.load('kaarten/' + card6[1] + '.gif').convert_alpha()
        card7 = card.Card.random(stack, stack_name)
        card7_img = pygame.image.load('kaarten/' + card7[1] + '.gif').convert_alpha()
        card8 = card.Card.random(stack, stack_name)
        card8_img = pygame.image.load('kaarten/' + card8[1] + '.gif').convert_alpha()
        card9 = card.Card.random(stack, stack_name)
        card9_img = pygame.image.load('kaarten/' + card9[1] + '.gif').convert_alpha()
        card10 = card.Card.random(stack, stack_name)
        card10_img = pygame.image.load('kaarten/' + card10[1] + '.gif').convert_alpha()
        card11 = card.Card.random(stack, stack_name)
        card11_img = pygame.image.load('kaarten/' + card11[1] + '.gif').convert_alpha()
        card12 = card.Card.random(stack, stack_name)
        card12_img = pygame.image.load('kaarten/' + card12[1] + '.gif').convert_alpha()
        
        #create buttons for cards
        card1_button = button.Button(102, 65, card1_img, 1)
        card2_button = button.Button(102, 300, card2_img, 1)
        card3_button = button.Button(102, 535, card3_img, 1)
        card4_button = button.Button(237, 65, card4_img, 1)
        card5_button = button.Button(237, 300, card5_img, 1)
        card6_button = button.Button(237, 535, card6_img, 1)
        card7_button = button.Button(372, 65, card7_img, 1)
        card8_button = button.Button(372, 300, card8_img, 1)
        card9_button = button.Button(372, 535, card9_img, 1)
        card10_button = button.Button(507, 65, card10_img, 1)
        card11_button = button.Button(507, 300, card11_img, 1)
        card12_button = button.Button(507, 535, card12_img, 1)
        
        #initialize score and stack count
        stack_count = font.render(str(len(stack)), True, WHITE)
        pygame.time.set_timer(Display_new_cards, 900)
        sp = 0
        score_Player = font.render(str(sp), True, WHITE)
        sc = 0
        score_Computer = font.render(str(sc), True, WHITE)
        
        #set all card variables to False
        card1_selected, new_card1, make_card1 = False, False, False
        card2_selected, new_card2, make_card2 = False, False, False
        card3_selected, new_card3, make_card3 = False, False, False
        card4_selected, new_card4, make_card4 = False, False, False
        card5_selected, new_card5, make_card5 = False, False, False
        card6_selected, new_card6, make_card6 = False, False, False
        card7_selected, new_card7, make_card7 = False, False, False
        card8_selected, new_card8, make_card8 = False, False, False
        card9_selected, new_card9, make_card9 = False, False, False
        card10_selected, new_card10, make_card10 = False, False, False
        card11_selected, new_card11, make_card11 = False, False, False
        card12_selected, new_card12, make_card12 = False, False, False
        show_you_have_to_choose_3_cards = False
        
        #reset time left
        time_left_int = 0
        
        #create important lists
        selected = []
        selected_computer = []
        on_table = [card1, card2, card3, card4, 
                    card5, card6, card7, card8, 
                    card9, card10, card11, card12]
        
        #initialize game state
        win_screen, loss_screen, draw_screen = False, False, False
        begin_screen = True
        help_not_needed = True
        game_screen = False
    
    #event game-loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False

        #reset timer and show cards
        if event.type == Display_new_cards:
            pygame.time.set_timer(Display_new_cards, 0)
            new_card1 = True
            new_card2 = True 
            new_card3 = True
            new_card4 = True
            new_card5 = True
            new_card6 = True
            new_card7 = True
            new_card8 = True
            new_card9 = True
            new_card10 = True
            new_card11 = True
            new_card12 = True
        #if the timer runs out new cards should apear
        if event.type == Display_chosen_cards:
            #reset timer
            pygame.time.set_timer(Display_chosen_cards, 0)
            
            #remove cards from table
            for i in card.Card.pick_set(on_table):
                on_table.remove(i)
            
            #Give computer point
            sc += 1
            score_Computer = font.render(str(sc), True, WHITE)
            
            #add new cards
            if card1 in selected_computer and len(stack) != 0:
                make_card1 = True
            if card2 in selected_computer and len(stack) != 0:
                make_card2 = True
            if card3 in selected_computer and len(stack) != 0:
                make_card3 = True
            if card4 in selected_computer and len(stack) != 0:
                make_card4 = True
            if card5 in selected_computer and len(stack) != 0:
                make_card5 = True
            if card6 in selected_computer and len(stack) != 0:
                make_card6 = True
            if card7 in selected_computer and len(stack) != 0:
                make_card7 = True
            if card8 in selected_computer and len(stack) != 0:
                make_card8 = True
            if card9 in selected_computer and len(stack) != 0:
                make_card9 = True
            if card10 in selected_computer and len(stack) != 0:
                make_card10 = True
            if card11 in selected_computer and len(stack) != 0:
                make_card11 = True
            if card12 in selected_computer and len(stack) != 0:
                make_card12 = True
            #you can select cards again and reset selected_computer        
            select_cards = True
            selected_computer = []
            #set timer untill new cards apear
            pygame.time.set_timer(Display_new_cards, 900)
            #in-game timer should play again
            time_paused = False
            #reset start time
            start_time = pygame.time.get_ticks()
            #reset the time that was paused, because this should only hold for one round
            unpaused_time = 0
            paused_time = 0
            time_while_paused = 0
        #if space exit instructions
        if event.type == pygame.KEYDOWN:
            #you can pause and unpause the game by clicking the space button.
            if event.key == pygame.K_SPACE and not time_paused:
                if not help_not_needed:
                    help_not_needed = True
                    unpaused_time = pygame.time.get_ticks()
                elif help_not_needed:
                    help_not_needed = False
                    paused_time = pygame.time.get_ticks()
            #after game has ended, press any key to go back to the start screen
            if win_screen or loss_screen or draw_screen:
                win_screen, loss_screen, draw_screen = False, False, False
                reset_game = True
                begin_screen = True
                
    #Fill the screen with a color
    screen.fill(PURPLE)
    #show the final screen depending on the score
    if win_screen:
        game_screen = False
        pygame.draw.rect(screen, LIGHT_PURPLE, end_screen_rect)
        screen.blit(you_win_shade, (180, 160))
        screen.blit(you_win, (170, 150))
        screen.blit(press_any_key, (300, 350))
        screen.blit(your_score, (300, 550))
        screen.blit(score_Player, (630, 550))
        screen.blit(computer_score, (300, 475))
        screen.blit(score_Computer, (630, 475))
    elif loss_screen:
        game_screen = False
        pygame.draw.rect(screen, LIGHT_PURPLE, end_screen_rect)
        screen.blit(you_lose_shade, (180, 160))
        screen.blit(you_lose, (170, 150))
        screen.blit(press_any_key, (300, 350))
        screen.blit(your_score, (300, 550))
        screen.blit(score_Player, (630, 550))
        screen.blit(computer_score, (300, 475))
        screen.blit(score_Computer, (630, 475))
    elif draw_screen:
        game_screen = False
        pygame.draw.rect(screen, LIGHT_PURPLE, end_screen_rect)
        screen.blit(it_is_a_draw_shade, (110, 160))
        screen.blit(it_is_a_draw, (100, 150))
        screen.blit(press_any_key, (300, 350))
        screen.blit(your_score, (300, 550))
        screen.blit(score_Player, (630, 550))
        screen.blit(computer_score, (300, 475))
        screen.blit(score_Computer, (630, 475))
    
    #if help button clicked, show instructions and pause menu.
    if not help_not_needed:
        rules_button.draw(screen)
        if return_game_button.draw(screen):
            help_not_needed = True
            unpaused_time = pygame.time.get_ticks()
        if return_begin_button.draw(screen):
            reset_game = True
            begin_screen = True
            help_not_needed = True
            unpaused_time = 0
        if exit_pause_button.draw(screen):
            running = False
    else:
        if begin_screen:
            paused_time = 0
            unpaused_time = 0
            time_while_paused = 0 
            pygame.draw.rect(screen, WHITE, exit_rect)
            screen.blit(Main_menu, (325, 100))
            
            #decide difficulty and start game
            if easy_button.draw(screen):
                timer = 60900
                start_time = pygame.time.get_ticks()
                begin_screen = False
                game_screen = True
            elif medium_button.draw(screen):
                timer = 30900
                start_time = pygame.time.get_ticks()
                begin_screen = False
                game_screen = True
            elif hard_button.draw(screen):
                timer = 15900
                start_time = pygame.time.get_ticks()
                begin_screen = False
                game_screen = True
            elif impossible_button.draw(screen):
                timer = 5900
                start_time = pygame.time.get_ticks()
                begin_screen = False
                game_screen = True
            #both corner buttons
            if instructions_button.draw(screen):
                help_not_needed = False
                paused_time = pygame.time.get_ticks()
            if exit_button.draw(screen):
                running = False

        #Playing the game.
        elif game_screen:
            #Check the time at all moments during the game.
            current_time = pygame.time.get_ticks()
            #draw corner buttons
            if instructions_button.draw(screen) and not time_paused:
                help_not_needed = False
                paused_time = pygame.time.get_ticks()
            pygame.draw.rect(screen, WHITE, exit_rect)
            if exit_button.draw(screen):
                running = False
            #create rectangles for computer select
            if card1 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect1)
            if card2 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect2)
            if card3 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect3)
            if card4 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect4)
            if card5 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect5)
            if card6 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect6)
            if card7 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect7)
            if card8 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect8)
            if card9 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect9)
            if card10 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect10)
            if card11 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect11)
            if card12 in selected_computer:
                pygame.draw.rect(screen, LIGHT_BLUE, selected_rect12)
                
            #create rectangles for selecting
            if card1_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect1)
            if card2_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect2)
            if card3_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect3)
            if card4_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect4)
            if card5_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect5)
            if card6_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect6)
            if card7_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect7)
            if card8_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect8)
            if card9_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect9)
            if card10_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect10)
            if card11_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect11)
            if card12_selected:
                pygame.draw.rect(screen, YELLOW, selected_rect12)

            #determine the time that passed while the game was paused
            time_while_paused -= paused_time
            paused_time = 0
            time_while_paused += unpaused_time
            unpaused_time = 0

            #create cards on screen and make them selectable.
            if new_card1:
                if card1 in on_table:
                    if card1_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card1_selected:
                                card1_selected = True
                                selected.append(card1)
                            elif card1_selected:
                                card1_selected = False
                                selected.remove(card1)
                        elif card1_selected:
                            card1_selected = False
                            selected.remove(card1)
            if new_card2:
                if card2 in on_table:
                    if card2_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card2_selected:
                                card2_selected = True
                                selected.append(card2)
                            elif card2_selected:
                                card2_selected = False
                                selected.remove(card2)
                        elif card2_selected:
                            card2_selected = False
                            selected.remove(card2)
            if new_card3:
                if card3 in on_table:
                    if card3_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card3_selected:
                                card3_selected = True
                                selected.append(card3)
                            elif card3_selected:
                                card3_selected = False
                                selected.remove(card3)
                        elif card3_selected:
                            card3_selected = False
                            selected.remove(card3)
            if new_card4:
                if card4 in on_table:
                    if card4_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card4_selected:
                                card4_selected = True
                                selected.append(card4)
                            elif card4_selected:
                                card4_selected = False
                                selected.remove(card4)
                        elif card4_selected:
                            card4_selected = False
                            selected.remove(card4)
            if new_card5:
                if card5 in on_table:
                    if card5_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card5_selected:
                                card5_selected = True
                                selected.append(card5)
                            elif card5_selected:
                                card5_selected = False
                                selected.remove(card5)
                        elif card5_selected:
                            card5_selected = False
                            selected.remove(card5)
            if new_card6:
                if card6 in on_table:
                    if card6_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card6_selected:
                                card6_selected = True
                                selected.append(card6)
                            elif card6_selected:
                                card6_selected = False
                                selected.remove(card6)
                        elif card6_selected:
                            card6_selected = False
                            selected.remove(card6)
            if new_card7:
                if card7 in on_table:
                    if card7_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card7_selected:
                                card7_selected = True
                                selected.append(card7)
                            elif card7_selected:
                                card7_selected = False
                                selected.remove(card7)
                        elif card7_selected:
                            card7_selected = False
                            selected.remove(card7)
            if new_card8:
                if card8 in on_table:
                    if card8_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card8_selected:
                                card8_selected = True
                                selected.append(card8)
                            elif card8_selected:
                                card8_selected = False
                                selected.remove(card8)
                        elif card8_selected:
                            card8_selected = False
                            selected.remove(card8)
            if new_card9:
                if card9 in on_table:
                    if card9_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card9_selected:
                                card9_selected = True
                                selected.append(card9)
                            elif card9_selected:
                                card9_selected = False
                                selected.remove(card9)
                        elif card9_selected:
                            card9_selected = False
                            selected.remove(card9)
            if new_card10:
                if card10 in on_table:
                    if card10_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card10_selected:
                                card10_selected = True
                                selected.append(card10)
                            elif card10_selected:
                                card10_selected = False
                                selected.remove(card10)
                        elif card10_selected:
                            card10_selected = False
                            selected.remove(card10)
            if new_card11:
                if card11 in on_table:
                    if card11_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card11_selected:
                                card11_selected = True
                                selected.append(card11)
                            elif card11_selected:
                                card11_selected = False
                                selected.remove(card11)
                        elif card11_selected:
                            card11_selected = False
                            selected.remove(card11)
            if new_card12:
                if card12 in on_table:
                    if card12_button.draw(screen):
                        if len(selected) < 3 and select_cards:
                            if not card12_selected:
                                card12_selected = True
                                selected.append(card12)
                            elif card12_selected:
                                card12_selected = False
                                selected.remove(card12)
                        elif card12_selected:
                            card12_selected = False
                            selected.remove(card12)
                            
            #create scoreboard
            pygame.draw.rect(screen, LIGHT_PURPLE, score_board)
            screen.blit(Player, (760, 405))
            screen.blit(Computer, (760, 355))
            screen.blit(score_Player, (1000, 405))
            screen.blit(score_Computer, (1000, 355))
            #if 3 cards ar enot selected show message
            if show_you_have_to_choose_3_cards:
                screen.blit(you_have_to_choose_3_cards, (700, 570))
                
            #display time left for player
            if time_paused:
                time_left = font.render('Time left: ' + str(time_left_int), True, WHITE)
            else:
                time_left = font.render('Time left: ' + str(int((timer - current_time + start_time + time_while_paused)/1000)), True, WHITE)
            screen.blit(time_left, (102, 15))
            
            #create stack
            stack_button.draw(screen)
            screen.blit(stack_count, (760, 65))
            
            #create submit button on screen:
            if submit_button.draw(screen):
                #deselect all cards and remove message
                card1_selected = False
                card2_selected = False
                card3_selected = False
                card4_selected = False
                card5_selected = False
                card6_selected = False
                card7_selected = False
                card8_selected = False
                card9_selected = False
                card10_selected = False
                card11_selected = False
                card12_selected = False
                show_you_have_to_choose_3_cards = False
                if len(selected) == 3:
                    #Check if the selected cards are a real SET
                    if card.Card.check_set(selected):
                        #reset the time that was paused, because this should only hold for one round
                        unpaused_time = 0
                        paused_time = 0
                        time_while_paused = 0
                        pygame.time.set_timer(Display_new_cards, 900)
                        
                        #give player point
                        sp += 1
                        score_Player = font.render(str(sp), True, WHITE)
                        
                        #remove cards from table
                        for i in selected:
                            on_table.remove(i)
                        #make new cards
                        if card1 in selected and len(stack) != 0:
                            make_card1 = True
                        if card2 in selected and len(stack) != 0:
                            make_card2 = True
                        if card3 in selected and len(stack) != 0:
                            make_card3 = True
                        if card4 in selected and len(stack) != 0:
                            make_card4 = True
                        if card5 in selected and len(stack) != 0:
                            make_card5 = True
                        if card6 in selected and len(stack) != 0:
                            make_card6 = True
                        if card7 in selected and len(stack) != 0:
                            make_card7 = True
                        if card8 in selected and len(stack) != 0:
                            make_card8 = True
                        if card9 in selected and len(stack) != 0:
                            make_card9 = True
                        if card10 in selected and len(stack) != 0:
                            make_card10 = True
                        if card11 in selected and len(stack) != 0:
                            make_card11 = True
                        if card12 in selected and len(stack) != 0:
                            make_card12 = True
                                
                        #reset selected
                        selected = []
                        start_time = pygame.time.get_ticks()
                    #if not a SET computer can make a turn
                    else:
                        computer_turn = True
                #less than 3 cards were selected
                else:
                    show_you_have_to_choose_3_cards = True
                    #reset selected
                    selected = []
            #if the timer runs out the computer needs to make a move
            elif timer - current_time + start_time + time_while_paused < 0 and help_not_needed and time_paused == False:
                computer_turn = True
                #deselect all cards
                card1_selected = False
                card2_selected = False
                card3_selected = False
                card4_selected = False
                card5_selected = False
                card6_selected = False
                card7_selected = False
                card8_selected = False
                card9_selected = False
                card10_selected = False
                card11_selected = False
                card12_selected = False
                show_you_have_to_choose_3_cards = False
            #if it is the computer his turn
            if computer_turn:
                computer_turn = False
                #check if the game is over
                if card.Card.pick_set(on_table) == False and len(stack) == 0:
                    if sc > sp:
                        loss_screen = True
                    elif sp > sc:
                        win_screen = True
                    else:
                        draw_screen = True
                #check if there exists a SET
                elif card.Card.pick_set(on_table) == False:
                    #remove 3 cards and make new ones
                    on_table.remove(card10)
                    make_card10 = True
                    on_table.remove(card11)
                    make_card11 = True
                    on_table.remove(card12)
                    make_card12 = True
                    
                    #reset the time that was paused, because this should only hold for one round
                    unpaused_time = 0
                    paused_time = 0
                    time_while_paused = 0
                    
                    #start timer until new cards apear
                    pygame.time.set_timer(Display_new_cards, 900)

                    #reset selected
                    selected = []
                    start_time = pygame.time.get_ticks()
                #there is a SET 
                else:
                    #make selected_computer
                    for i in card.Card.pick_set(on_table):
                        selected_computer.append(i)
                    
                    #determine the time left
                    time_left_int = int((timer - current_time + start_time + time_while_paused)/1000)
                        
                    #start timer for how long selected cards show and pause in-game timer
                    pygame.time.set_timer(Display_chosen_cards, 3000)
                    time_paused = True
                    
                    #you can not pick any cards until cards are removed
                    select_cards = False
                    
                    #reset selected
                    selected = []
            #make the actual cards if they need to be made
            if make_card1 and card1 not in on_table:
                new_card1 = False
                make_card1 = False
                card1 = card.Card.random(stack, stack_name)
                card1_img = pygame.image.load('kaarten/' + card1[1] + '.gif').convert_alpha()
                card1_button = button.Button(102, 65, card1_img, 1)
                on_table.append(card1)
            if make_card2 and card2 not in on_table:
                new_card2 = False
                make_card2 = False
                card2 = card.Card.random(stack, stack_name)
                card2_img = pygame.image.load('kaarten/' + card2[1] + '.gif').convert_alpha()
                card2_button = button.Button(102, 300, card2_img, 1)
                on_table.append(card2)
            if make_card3 and card3 not in on_table:
                new_card3 = False
                make_card3 = False
                card3 = card.Card.random(stack, stack_name)
                card3_img = pygame.image.load('kaarten/' + card3[1] + '.gif').convert_alpha()
                card3_button = button.Button(102, 535, card3_img, 1)
                on_table.append(card3)
            if make_card4 and card4 not in on_table:
                new_card4 = False
                make_card4 = False
                card4 = card.Card.random(stack, stack_name)
                card4_img = pygame.image.load('kaarten/' + card4[1] + '.gif').convert_alpha()
                card4_button = button.Button(237, 65, card4_img, 1)
                on_table.append(card4)
            if make_card5 and card5 not in on_table:
                new_card5 = False
                make_card5 = False
                card5 = card.Card.random(stack, stack_name)
                card5_img = pygame.image.load('kaarten/' + card5[1] + '.gif').convert_alpha()
                card5_button = button.Button(237, 300, card5_img, 1)
                on_table.append(card5)
            if make_card6 and card6 not in on_table:
                new_card6 = False
                make_card6 = False
                card6 = card.Card.random(stack, stack_name)
                card6_img = pygame.image.load('kaarten/' + card6[1] + '.gif').convert_alpha()
                card6_button = button.Button(237, 535, card6_img, 1)
                on_table.append(card6)
            if make_card7 and card7 not in on_table:
                new_card7 = False
                make_card7 = False
                card7 = card.Card.random(stack, stack_name)
                card7_img = pygame.image.load('kaarten/' + card7[1] + '.gif').convert_alpha()
                card7_button = button.Button(372, 65, card7_img, 1)
                on_table.append(card7)
            if make_card8 and card8 not in on_table:
                new_card8 = False
                make_card8 = False
                card8 = card.Card.random(stack, stack_name)
                card8_img = pygame.image.load('kaarten/' + card8[1] + '.gif').convert_alpha()
                card8_button = button.Button(372, 300, card8_img, 1)
                on_table.append(card8)
            if make_card9 and card9 not in on_table:
                new_card9 = False
                make_card9 = False
                card9 = card.Card.random(stack, stack_name)
                card9_img = pygame.image.load('kaarten/' + card9[1] + '.gif').convert_alpha()
                card9_button = button.Button(372, 535, card9_img, 1)
                on_table.append(card9)
            if make_card10 and card10 not in on_table:
                new_card10 = False
                make_card10 = False
                card10 = card.Card.random(stack, stack_name)
                card10_img = pygame.image.load('kaarten/' + card10[1] + '.gif').convert_alpha()
                card10_button = button.Button(507, 65, card10_img, 1)
                on_table.append(card10)
            if make_card11 and card11 not in on_table:
                new_card11 = False
                make_card11 = False
                card11 = card.Card.random(stack, stack_name)
                card11_img = pygame.image.load('kaarten/' + card11[1] + '.gif').convert_alpha()
                card11_button = button.Button(507, 300, card11_img, 1)
                on_table.append(card11)
            if make_card12 and card12 not in on_table:
                new_card12 = False
                make_card12 = False
                card12 = card.Card.random(stack, stack_name)
                card12_img = pygame.image.load('kaarten/' + card12[1] + '.gif').convert_alpha()
                card12_button = button.Button(507, 535, card12_img, 1)
                on_table.append(card12)
            
            #update stack_count
            stack_count = font.render('Cards left: ' + str(len(stack)), True, WHITE)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
