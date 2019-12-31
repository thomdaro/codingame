import time

# global constants
TEST_CASE_NAMES = ['descending', 'scattered', 'strong_1', 'strong_2', 'one']
BOARD_WIDTH = 8
BOARD_HEIGHT = 10
STARTING_HEIGHT = 10
GAME_SPEED = 0.01


# [string] filename: corresponds to the name of a test case input file, located in ../test_cases/.
def process_input(filename):
    res = []
    raw_file = open('../test_cases/' + filename + '.csv', 'r')

    for line in raw_file:
        # 'line' is a comma-separated string "x1,x2,x3,x4..."
        # rstrip() removes trailing newline, split(",") breaks line up by commas
        # map(int, line) converts strings to ints, list() converts map object to list
        res.append(list(map(int, line.rstrip().split(','))))
    raw_file.close()
    # res is a list of lists of numbers, each list represents input for a game round
    return res


# [string] filename: corresponds to the name of a test case expected output file, located in ../expected_output/.
def process_output(filename):
    raw_file = open('../expected_output/' + filename + '.csv', 'r')
    # same process as input, but with one line
    res = list(map(int, raw_file.readline().rstrip().split(',')))
    raw_file.close()
    # res is a list of numbers, representing the indices of the tallest mountain at each game round
    return res


# [list(int)] round_input: the heights of mountains in this current game round.
# [list(int)] next_round_input: the heights of mountains in the next game round.
# [int] p_height: the current height of the player. Reduced by 1 each game round.
# [int] tall_index: the index of the player-selected mountain. Determines where to draw laser.
def ascii_display(round_input, next_round_input, p_height, tall_index):
    display = []
    for x in round_input:
        mountain = []
        for _ in range(x):
            # "X" represents a mountain tile. We will rotate this 2D matrix to display mountains vertically
            mountain.append("X")
        for _ in range(BOARD_HEIGHT - x):
            # "." is an empty sky tile
            mountain.append(".")
        display.append(mountain)

    # credit to paldepind on SO for providing this one-liner to rotate a 2D matrix
    # (link: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python)
    for _ in range(3):
        # we rotate three times so that mountains can be drawn vertically, facing upward
        display = list(zip(*display[::-1]))

    # this loop draws a pass of the spaceship from one side to the other. This is a full game round
    for x in range(BOARD_WIDTH):
        # we pass from left to right on even heights, right to left on odd heights
        p_horiz = x if p_height % 2 == 0 else 7 - x
        # used to determine when to draw the reduced-height mountain
        flag = p_horiz > tall_index if p_height % 2 == 0 else p_horiz < tall_index

        print("- " * (BOARD_WIDTH + 2))
        for drawing_row in range(BOARD_HEIGHT):
            print("|", end=" ")
            for drawing_col in range(BOARD_WIDTH):
                # if we are over the player-selected mountain, draw laser below the ship
                if drawing_row > BOARD_HEIGHT - p_height and drawing_col == tall_index and p_horiz == tall_index:
                    print("V", end=" ")
                # if we are drawing the player's position, draw a ship
                elif drawing_col == p_horiz and drawing_row == BOARD_HEIGHT - p_height:
                    print("o", end=" ")
                else:
                    # if we're past the player-selected mountain, draw the mountain at a reduced height
                    if flag and drawing_col == tall_index:
                        # draw the sky down to the height of this mountain in the next game round
                        if drawing_row <= (BOARD_HEIGHT - 1) - next_round_input[tall_index]:
                            print(".", end=" ")
                        else:
                            print("X", end=" ")
                    else:
                        print(display[drawing_row][drawing_col], end=" ")
            print("|")
        print("- - - - - - - - - -")
        print()
        # reads final line of input file, ends game as soon as last mountain is zapped
        if max(next_round_input) == 0 and flag:
            print("All mountains destroyed, clear for landing.")
            break
        time.sleep(GAME_SPEED)


# [list(list(int))] case_in: the processed input for the current test case
# [list(int)] case_out: the processed output for the current test case
def main(case_in, case_out):
    res = []
    player_height = STARTING_HEIGHT

    for i in range(len(case_in)-1):
        heights = case_in[i]
        # this line represents the solution to the original problem
        tallest = heights.index(max(heights))
        res.append(tallest)
        ascii_display(case_in[i], case_in[i + 1], player_height, tallest)
        # if wrong mountain is selected, say so and stop the game
        if res != case_out[:i+1]:
            print("Wrong mountain zapped. Odds of eventual crash: 100%.")
            break
        # otherwise reduce the player height and prepare for next round of input
        heights.clear()
        player_height -= 1


if __name__ == '__main__':
    for name in TEST_CASE_NAMES:
        case_input = process_input(name)
        expected_case_output = process_output(name)
        main(case_input, expected_case_output)
