import sys
import keyboard
import time
import curses
import pygame

TEST_CASE_NAMES = ['descending', 'scattered', 'strong_1', 'strong_2', 'one']
BOARD_WIDTH = 8
BOARD_HEIGHT = 10
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 400
IMAGE_SIZE = 40
GAME_SPEED = 0.1


def process_input(file_name):
    """
    :param file_name: name of the file to be processed
    :type file_name: str
    """

    res = []
    raw_file = open('../test_cases/' + file_name + '.csv', 'r')

    for line in raw_file:
        res.append(list(map(int, line.rstrip().split(','))))
    raw_file.close()
    return res


def process_output(file_name):
    """
    :param file_name: name of the file to be processed
    :type file_name: str
    """
    raw_file = open('../expected_output/' + file_name + '.csv', 'r')
    res = list(map(int, raw_file.readline().rstrip().split(',')))
    raw_file.close()
    return res


def display(round_input, next_round_input, ship_row, tall_index):
    """
    :param round_input: heights of mountains in the current game round
    :type round_input: list[int]
    :param next_round_input: heights of mountains in the next game round
    :type next_round_input: list[int]
    :param ship_row: row the ship is drawn in
    :type ship_row: int
    :param tall_index: index of the selected mountain
    :type tall_index: int
    """

    disp_list = []
    for x in round_input:
        mountain = []
        for _ in range(x):
            mountain.append("X")
        for _ in range(BOARD_HEIGHT - x):
            mountain.append(".")
        disp_list.append(mountain)

    # credit to paldepind on SO for providing this one-liner to rotate a 2D matrix
    # (link: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python)
    for _ in range(3):
        disp_list = list(zip(*disp_list[::-1]))

    for x in range(BOARD_WIDTH):
        SCREEN.move(1, 0)
        move = x if ship_row % 2 == 0 else 7 - x
        flag = move > tall_index if ship_row % 2 == 0 else move < tall_index

        SCREEN.addstr("- " * (BOARD_WIDTH + 2) + "\n")
        for drawing_row in range(BOARD_HEIGHT):
            SCREEN.addstr("| ")
            for drawing_col in range(BOARD_WIDTH):
                if drawing_row > BOARD_HEIGHT - ship_row and drawing_col == tall_index and move == tall_index:
                    SCREEN.addstr("V ")
                elif drawing_col == move and drawing_row == BOARD_HEIGHT - ship_row:
                    SCREEN.addstr("o ")
                else:
                    if flag and drawing_col == tall_index:
                        if drawing_row <= (BOARD_HEIGHT - 1) - next_round_input[tall_index]:
                            SCREEN.addstr(". ")
                        else:
                            SCREEN.addstr("X ")
                    else:
                        SCREEN.addstr(disp_list[drawing_row][drawing_col] + " ")
            SCREEN.addstr("|\n")
        SCREEN.addstr("- " * (BOARD_WIDTH + 2) + "\n")
        SCREEN.refresh()

        if max(next_round_input) == 0 and flag:
            SCREEN.move(BOARD_HEIGHT + 3, 0)
            SCREEN.addstr("All mountains destroyed, clear for landing.")
            SCREEN.refresh()
            time.sleep(2)
            SCREEN.clear()
            break

        time.sleep(GAME_SPEED)


def graphical_display(round_input, next_round_input, ship_row, tall_index):
    """
    :param round_input: heights of mountains in the current game round
    :type round_input: list[int]
    :param next_round_input: heights of mountains in the next game round
    :type next_round_input: list[int]
    :param ship_row: row the ship is drawn in
    :type ship_row: int
    :param tall_index: index of the selected mountain
    :type tall_index: int
    :return: None
    """

    for display_row in range(BOARD_HEIGHT):
        for display_col in range(BOARD_WIDTH+2):
            DISPLAY_SURFACE.blit(SPACE_IMG, (display_col * IMAGE_SIZE, display_row * IMAGE_SIZE))
    ship_x = 0 if ship_row % 2 == 0 else WINDOW_WIDTH - IMAGE_SIZE
    ship_pos = [ship_x, IMAGE_SIZE * ship_row]
    DISPLAY_SURFACE.blit(SHIP_IMG, ship_pos)

    for i in range(len(round_input)):
        height = round_input[i]
        for tile in range(1, height + 1):
            DISPLAY_SURFACE.blit(MOUNTAIN_IMG, (i * IMAGE_SIZE, WINDOW_HEIGHT - tile * IMAGE_SIZE))

    check_event()
    pygame.display.update()
    time.sleep(GAME_SPEED)

    for move in range(1, BOARD_WIDTH):

        if ship_row % 2 != 0:
            move = BOARD_WIDTH - 1 - move
        flag = move > tall_index if ship_row % 2 == 0 else move < tall_index

        DISPLAY_SURFACE.blit(SPACE_IMG, ship_pos)
        ship_pos[0] += (40 if ship_row % 2 == 0 else -40)
        DISPLAY_SURFACE.blit(SHIP_IMG, ship_pos)

        if move == tall_index:
            DISPLAY_SURFACE.blit(LASER_TIP_IMG, (ship_pos[0], (ship_row + 1) * IMAGE_SIZE))
            for down in range(2, BOARD_HEIGHT - ship_row):
                DISPLAY_SURFACE.blit(LASER_IMG, (ship_pos[0], (ship_row + down) * IMAGE_SIZE))
        elif flag:
            for tile in range(next_round_input[tall_index], BOARD_HEIGHT - ship_row):
                DISPLAY_SURFACE.blit(SPACE_IMG, (tall_index * IMAGE_SIZE, (BOARD_HEIGHT - tile) * IMAGE_SIZE))
            for tile in range(next_round_input[tall_index]):
                DISPLAY_SURFACE.blit(MOUNTAIN_IMG, (tall_index * IMAGE_SIZE, (BOARD_HEIGHT - tile - 1) * IMAGE_SIZE))
            if max(next_round_input) == 0:
                pygame.display.update()
                pygame.display.set_caption("All mountains destroyed.")
                for _ in range(200):
                    pygame.time.wait(5)
                    check_event()
                break

        check_event()
        pygame.display.update()
        time.sleep(GAME_SPEED)


def check_event():
    if pygame.event.poll().type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def main(case_in, case_out, case_name):
    """
    :param case_in: processed input for the current test case
    :type case_in: list[list[int]]
    :param case_out: processed output for the current test case
    :type case_out: list[int]
    :param case_name: name of the current test case
    :type case_name: str
    :return: None
    """
    res = []
    player_height = BOARD_HEIGHT

    for i in range(len(case_in)-1):

        heights = case_in[i]
        tallest = heights.index(max(heights))
        res.append(tallest)

        if res != case_out[:i+1]:
            break

        if DISPLAY_MODE == "terminal":
            SCREEN.addstr(0, 0, "test case: " + case_name + "\n")
            display(case_in[i], case_in[i + 1], player_height, tallest)
        elif DISPLAY_MODE == "graphical":
            pygame.display.set_caption("test case: " + case_name)
            graphical_display(case_in[i], case_in[i+1], i, tallest)
        heights.clear()
        player_height -= 1


if __name__ == '__main__':

    print("Press t for terminal display, g for graphical display.")
    while True:
        if keyboard.is_pressed('t'):
            keyboard.press('\b')
            SCREEN = curses.initscr()
            DISPLAY_MODE = "terminal"
            break
        elif keyboard.is_pressed('g'):
            keyboard.press('\b')
            pygame.init()
            DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.event.set_allowed(pygame.ACTIVEEVENT)
            pygame.event.set_allowed(pygame.QUIT)
            SHIP_IMG = pygame.image.load('../images/spaceship.png')
            SPACE_IMG = pygame.image.load('../images/space.png')
            MOUNTAIN_IMG = pygame.image.load('../images/mountain.png')
            LASER_TIP_IMG = pygame.image.load('../images/laser_tip.png')
            LASER_IMG = pygame.image.load('../images/laser.png')
            DISPLAY_MODE = "graphical"
            break

    for name in TEST_CASE_NAMES:
        case_input = process_input(name)
        expected_case_output = process_output(name)
        main(case_input, expected_case_output, name)

    if DISPLAY_MODE == "terminal":
        curses.endwin()
    elif DISPLAY_MODE == "graphical":
        pygame.quit()
