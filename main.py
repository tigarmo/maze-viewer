# import the pygame module, so you can use it
import pygame


def create_background(lines, wall, ground, width, height):
    tile_dict = {
        '#': wall,
    }

    background = pygame.Surface((width, height))

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            tile = tile_dict.get(c, ground)
            background.blit(tile, (j*32,i*32))

    return background


def main():
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 30)

    import sys
    if len(sys.argv) == 3:
        maze_file = sys.argv[1]
        steps_file = sys.argv[2]
    elif len(sys.argv) != 1:
        print('Usage: maze-viewer mazefile.txt stepsfile.txt')
        sys.exit(0)
    else:
        maze_file = 'maze.txt'
        steps_file = 'steps.txt'

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load('res/wall.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('maze-viewer')

    # Load the maze itself
    maze_lines = open(maze_file,'r').readlines()
    maze_lines = [line.strip() for line in maze_lines]

    rows = len(maze_lines)
    columns = len(maze_lines[0])

    height = rows * 32
    width = columns * 32

    # Load the steps
    steps = open(steps_file, 'r').readlines()
    steps = [tuple(line.strip().split(' ')) for line in steps]
    steps = [(int(x), int(y)) for x,y in steps]

    player = pygame.image.load('res/minotaur.png')

    screen = pygame.display.set_mode((width,height))

    wall = pygame.image.load("res/wall.png")
    ground = pygame.image.load('res/ground.png')

    background = create_background(maze_lines, wall, ground, width, height)

    # create a surface on screen that has the size of 240 x 180

    screen.blit(background,(0,0))
    pygame.display.update()
    # define a variable to control the main loop
    running = True

    step_counter = 0
    stepping = True
    sleep_time = 5000 // len(steps)
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    stepping = True
                    step_counter = 0

        if stepping:
            screen.blit(background, (0,0))
            x, y = steps[step_counter]
            screen.blit(player, (y*32, x*32))
            pygame.display.update()

            step_counter += 1
            if step_counter >= len(steps):
                stepping = False

            pygame.time.delay(sleep_time)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()