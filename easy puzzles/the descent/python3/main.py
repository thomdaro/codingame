import time
import curses
import pygame

TEST_CASE_NAMES = ['descending', 'scattered', 'strong_1', 'strong_2', 'one']
BOARD_WIDTH = 8
BOARD_HEIGHT = 10
WINDOW_SIZE = 400
GAME_SPEED = 0.05
DISPLAY_MODE = ["console", "terminal", "graphical"][2]
SCREEN = curses.initscr() if DISPLAY_MODE == "terminal" else None
if DISPLAY_MODE == "graphical":
    pygame.init()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SHIP_IMG = pygame.image.load('../images/spaceship.png')
    SPACE_IMG = pygame.image.load('../images/space.png')
    MOUNTAIN_IMG = pygame.image.load('../images/mountain.png')
    LASER_TIP_IMG = pygame.image.load('../images/laser_tip.png')
    LASER_IMG = pygame.image.load('../images/laser.png')


# [string] filename: corresponds to the name of a test case input file, located in ../test_cases/.
def process_input(filename):
    res = []
    raw_file = open('../test_cases/' + filename + '.csv', 'r')

    for line in raw_file:
        res.append(list(map(int, line.rstrip().split(','))))
    raw_file.close()
    return res


# [string] filename: corresponds to the name of a test case expected output file, located in ../expected_output/.
def process_output(filename):
    raw_file = open('../expected_output/' + filename + '.csv', 'r')
    res = list(map(int, raw_file.readline().rstrip().split(',')))
    raw_file.close()
    return res


# [list(int)] round_input: the heights of mountains in this current game round.
# [list(int)] next_round_input: the heights of mountains in the next game round.
# [int] p_height: the current height of the player. Reduced by 1 each game round.
# [int] tall_index: the index of the player-selected mountain. Determines where to draw laser.
# [string] file_name: used to display the name of the current test case.
def display(round_input, next_round_input, p_height, tall_index, file_name):
    disp = []
    for x in round_input:
        mountain = []
        for _ in range(x):
            mountain.append("X")
        for _ in range(BOARD_HEIGHT - x):
            mountain.append(".")
        disp.append(mountain)

    # credit to paldepind on SO for providing this one-liner to rotate a 2D matrix
    # (link: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python)
    for _ in range(3):
        disp = list(zip(*disp[::-1]))

    for x in range(BOARD_WIDTH):
        p_horiz = x if p_height % 2 == 0 else 7 - x
        flag = p_horiz > tall_index if p_height % 2 == 0 else p_horiz < tall_index

        if DISPLAY_MODE == "console":
            print("test case: " + file_name + "\n")
        elif DISPLAY_MODE == "terminal":
            SCREEN.addstr("test case: " + file_name + "\n")
        elif DISPLAY_MODE == "graphical":
            pygame.display.set_caption("test case: " + file_name)

        res = "- " * (BOARD_WIDTH + 2) + "\n"
        for drawing_row in range(BOARD_HEIGHT):
            res += "| "
            if DISPLAY_MODE == "graphical":
                DISPLAY_SURFACE.blit(SPACE_IMG, (0, 40 * drawing_row))
            for drawing_col in range(BOARD_WIDTH):
                drawing_pos = (40 * drawing_col + 40, 40 * drawing_row)
                if drawing_row > BOARD_HEIGHT - p_height and drawing_col == tall_index and p_horiz == tall_index:
                    res += "V "
                    if DISPLAY_MODE == "graphical":
                        if drawing_row == BOARD_HEIGHT - p_height + 1:
                            DISPLAY_SURFACE.blit(LASER_TIP_IMG, drawing_pos)
                        else:
                            DISPLAY_SURFACE.blit(LASER_IMG, drawing_pos)
                elif drawing_col == p_horiz and drawing_row == BOARD_HEIGHT - p_height:
                    if DISPLAY_MODE == "graphical":
                        DISPLAY_SURFACE.blit(SHIP_IMG, drawing_pos)
                    else:
                        res += "o "
                else:
                    if flag and drawing_col == tall_index:
                        if drawing_row <= (BOARD_HEIGHT - 1) - next_round_input[tall_index]:
                            if DISPLAY_MODE == "graphical":
                                DISPLAY_SURFACE.blit(SPACE_IMG, drawing_pos)
                            else:
                                res += ". "
                        else:
                            if DISPLAY_MODE == "graphical":
                                DISPLAY_SURFACE.blit(MOUNTAIN_IMG, drawing_pos)
                            else:
                                res += "X "
                    else:
                        char = disp[drawing_row][drawing_col]
                        if DISPLAY_MODE == "graphical":
                            if char == ".":
                                DISPLAY_SURFACE.blit(SPACE_IMG, drawing_pos)
                            elif char == "X":
                                DISPLAY_SURFACE.blit(MOUNTAIN_IMG, drawing_pos)
                        res += char + " "
            res += "|\n"
            if DISPLAY_MODE == "graphical":
                DISPLAY_SURFACE.blit(SPACE_IMG, (WINDOW_SIZE - 40, 40 * drawing_row))
        res += "- " * (BOARD_WIDTH + 2) + "\n"
        if DISPLAY_MODE == "console":
            print(res + "\n")
        elif DISPLAY_MODE == "terminal":
            SCREEN.addstr(0, 0, res)
            SCREEN.refresh()
        elif DISPLAY_MODE == "graphical":
            pygame.display.update()
        if max(next_round_input) == 0 and flag:
            if DISPLAY_MODE == "console":
                print("All mountains destroyed, clear for landing.")
            elif DISPLAY_MODE == "terminal":
                SCREEN.addstr("All mountains destroyed, clear for landing.", curses.A_STANDOUT)
                SCREEN.refresh()
            elif DISPLAY_MODE == "graphical":
                pygame.display.set_caption("All mountains destroyed, clear for landing.")
                pygame.display.update()
            time.sleep(2)
            SCREEN.clear() if DISPLAY_MODE == "terminal" else None
            break
        time.sleep(GAME_SPEED)


# [list(list(int))] case_in: the processed input for the current test case
# [list(int)] case_out: the processed output for the current test case
def main(case_in, case_out, case_name):
    res = []
    player_height = BOARD_HEIGHT

    for i in range(len(case_in)-1):
        heights = case_in[i]
        tallest = heights.index(max(heights))
        res.append(tallest)
        display(case_in[i], case_in[i + 1], player_height, tallest, case_name)
        heights.clear()
        player_height -= 1


if __name__ == '__main__':

    for name in TEST_CASE_NAMES:
        case_input = process_input(name)
        expected_case_output = process_output(name)
        main(case_input, expected_case_output, name)

    if DISPLAY_MODE == "terminal":
        curses.endwin()
    elif DISPLAY_MODE == "graphical":
        pygame.quit()
