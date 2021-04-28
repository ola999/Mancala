import pygame
import time
import random

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
# creat the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Mancala")
icon = pygame.image.load('mancala.png')
pygame.display.set_icon(icon)

boardx = 80
boardy = 180
holex = 27
holey = 55
boardImage = pygame.image.load('mancala_board.png')
ballImage = pygame.image.load('ball.png')
rightArrowImage = pygame.image.load('right-arrow.png')
leftArrowImage = pygame.image.load('left-arrow.png')


class Hole:
    def __init__(self, name, location, hole_number, num):
        self.numOfStones = num
        self.holeName = name
        self.holeLocation = location
        self.hole_number = hole_number
        self.stonesListLocations = [(location[0], location[1]),
                                    (location[0] + (holex / 2), location[1]),
                                    (location[0] + (holex / 2) * 2, location[1]),
                                    (location[0], location[1] + (holey / 4)),
                                    (location[0] + (holex / 2), location[1] + (holey / 4)),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4)),
                                    (location[0], location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 2),
                                    (location[0], location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 3),
                                    (location[0], location[1] + (holey / 4) * 4),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 4),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 4),
                                    ######################
                                    (location[0] + (holex / 4), location[1]),
                                    (location[0] + (holex / 4) * 3, location[1]),
                                    # (location[0] + (holex / 2) * 2, location[1]),
                                    (location[0] + (holex / 4), location[1] + (holey / 4)),
                                    (location[0] + (holex / 4) * 3, location[1] + (holey / 4)),
                                    # (location[0] + (holex / 2) * 2, location[1] + (holey / 4)),
                                    (location[0] + (holex / 4), location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 4) * 3, location[1] + (holey / 4) * 2),
                                    # (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 4), location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 4) * 3, location[1] + (holey / 4) * 3),
                                    # (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 4), location[1] + (holey / 4) * 4),
                                    (location[0] + (holex / 4) * 3, location[1] + (holey / 4) * 4),
                                    # (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 4),
                                    (location[0], location[1]),
                                    (location[0] + (holex / 2), location[1]),
                                    (location[0] + (holex / 2) * 2, location[1]),
                                    (location[0], location[1] + (holey / 4)),
                                    (location[0] + (holex / 2), location[1] + (holey / 4)),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4)),
                                    (location[0], location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 2),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 2),
                                    (location[0], location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 3),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 3),
                                    (location[0], location[1] + (holey / 4) * 4),
                                    (location[0] + (holex / 2), location[1] + (holey / 4) * 4),
                                    (location[0] + (holex / 2) * 2, location[1] + (holey / 4) * 4),
                                    ]

    def print_stones(self):
        counter = 0
        while counter < self.numOfStones:
            screen.blit(ballImage, self.stonesListLocations[counter])
            counter += 1
        if self.holeName[5] == '1':
            label = myfont.render(str(self.numOfStones), True, (0, 0, 0))
            screen.blit(pygame.transform.flip(label, True, True), (self.holeLocation[0] + holex * 0.7,
                                                                   self.holeLocation[1] - holey * 0.42))
        if self.holeName[5] == '2':
            label = myfont.render(str(self.numOfStones), True, (0, 0, 0))
            screen.blit(label, (self.holeLocation[0] + holex * 0.7, self.holeLocation[1] + holey * 1.5))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.holeLocation[0] <= x1 <= self.holeLocation[0] + holex and \
                self.holeLocation[1] <= y1 <= self.holeLocation[1] + holey:
            return True
        else:
            return False


class Holes:
    def __init__(self, arr):
        self.bigHole1 = Hole("bigHole1", (120, 250), -1, arr[0])
        self.bigHole2 = Hole("bigHole2", (635, 250), -2, arr[1])
        self.holeA1 = Hole("holeA1", (200, 200), 1, arr[2])
        self.holeB1 = Hole("holeB1", (270, 200), 2, arr[3])
        self.holeC1 = Hole("holeC1", (344, 200), 3, arr[4])
        self.holeD1 = Hole("holeD1", (416, 200), 4, arr[5])
        self.holeE1 = Hole("holeE1", (487, 200), 5, arr[6])
        self.holeF1 = Hole("holeF1", (558, 200), 6, arr[7])

        self.holeA2 = Hole("holeA2", (200, 310), 1, arr[8])
        self.holeB2 = Hole("holeB2", (270, 310), 2, arr[9])
        self.holeC2 = Hole("holeC2", (344, 310), 3, arr[10])
        self.holeD2 = Hole("holeD2", (416, 310), 4, arr[11])
        self.holeE2 = Hole("holeE2", (487, 310), 5, arr[12])
        self.holeF2 = Hole("holeF2", (558, 310), 6, arr[13])
        self.myHoles = [self.bigHole1, self.bigHole2, self.holeA1, self.holeB1, self.holeC1, self.holeD1,
                        self.holeE1, self.holeF1, self.holeA2, self.holeB2, self.holeC2, self.holeD2,
                        self.holeE2, self.holeF2]

    def copy(self):
        arr = []
        for index in range(0, 14):
            arr.append(self.myHoles[index].numOfStones)
        return Holes(arr)

    def print_all_stones(self):
        for hole in self.myHoles:
            hole.print_stones()

    def get_hole_by_number(self, n, p):
        if n == -1:
            return self.bigHole1
        if n == -2:
            return self.bigHole2

        for hole in self.myHoles:
            if hole.holeName[0] == 'b':
                continue
            if int(hole.holeName[5]) != p:
                continue
            if n == hole.hole_number:
                return hole


def draw_screen(game):
    screen.fill((0, 0, 50))  # RGB
    screen.blit(boardImage, (boardx, boardy))
    game.my_holes.print_all_stones()
    screen.blit(rightArrowImage, (390, 390))
    screen.blit(leftArrowImage, (390, 180))
    font = pygame.font.SysFont("comicsans", 20)
    text = font.render("player 1", True, (255, 200, 200))
    screen.blit(pygame.transform.rotate(text, 180), (100, 160))
    text = font.render("player 2", True, (255, 200, 200))
    screen.blit(text, (650, 415))
    if game.player == 1:
        text = font.render("It's player 1 turn", True, (255, 200, 200))
        screen.blit(pygame.transform.rotate(text, 90), (20, 230))
    if game.player == 2:
        text = font.render("It's player 2 turn", True, (255, 200, 200))
        screen.blit(pygame.transform.rotate(text, 90), (20, 230))
    pygame.display.update()


def win_screen(winner):
    screen.fill((0, 0, 0))  # RGB
    font = pygame.font.SysFont("comicsans", 60)
    text0 = font.render("Player " + str(winner) + " is the winner!!", True, (255, 200, 200))
    font = pygame.font.SysFont("comicsans", 30)
    text1 = font.render("click to start again", True, (255, 200, 200))
    screen.blit(text0, (20, 50))
    screen.blit(text1, (20, 150))
    pygame.display.update()


def rules_screen():
    screen.fill((0, 0, 0))  # RGB
    font = pygame.font.SysFont("comicsans", 25)
    text0 = font.render("Game Rules: ", True, (255, 200, 200))
    text1 = font.render("1. The game begins with one player picking up all of the pieces in any one of ", True,
                        (255, 200, 200))
    text2 = font.render("the pockets on his/her side. ", True, (255, 200, 200))
    text3 = font.render("2. Moving counter-clockwise, the player deposits one of the stones in each ", True,
                        (255, 200, 200))
    text4 = font.render("pocket until the stones run out. ", True, (255, 200, 200))
    text5 = font.render("3. If you run into your own Mancala (store), deposit one piece in it. If you run", True,
                        (255, 200, 200))
    text6 = font.render("into your opponent's Mancala, skip it and continue moving to the next pocket.", True,
                        (255, 200, 200))
    text7 = font.render("4. If the last piece you drop is in your own Mancala, you take another turn.", True,
                        (255, 200, 200))
    text8 = font.render("5. If the last piece you drop is in an empty pocket on your side, you capture ", True,
                        (255, 200, 200))
    text9 = font.render("that piece and any pieces in the pocket directly opposite.", True, (255, 200, 200))
    text10 = font.render("6. The game ends when all six pockets on one side of the Mancala board", True,
                         (255, 200, 200))
    text11 = font.render(" are empty", True, (255, 200, 200))
    text12 = font.render("7. The player who still has pieces on his/her side of the board when the game", True,
                         (255, 200, 200))
    text13 = font.render(" ends captures all of those pieces.", True, (255, 200, 200))
    text14 = font.render("9. Count all the pieces in each Mancala. The winner is the player with the ", True,
                         (255, 200, 200))
    text15 = font.render("most pieces.", True, (255, 200, 200))
    screen.blit(text0, (20, 20))
    screen.blit(text1, (20, 50))
    screen.blit(text2, (20, 80))
    screen.blit(text3, (20, 110))
    screen.blit(text4, (20, 140))
    screen.blit(text5, (20, 170))
    screen.blit(text6, (20, 200))
    screen.blit(text7, (20, 230))
    screen.blit(text8, (20, 260))
    screen.blit(text9, (20, 290))
    screen.blit(text10, (20, 320))
    screen.blit(text11, (20, 350))
    screen.blit(text12, (20, 380))
    screen.blit(text13, (20, 410))
    screen.blit(text14, (20, 440))
    screen.blit(text15, (20, 470))

    pygame.display.update()


class Game:
    def __init__(self, my_holes):
        self.my_holes = my_holes
        self.player = 1
        self.last_hole = None

    def copy(self):
        holes = self.my_holes.copy()
        return Game(holes)

    def check_if_to_collect(self, flag=True):
        if self.last_hole.numOfStones == 1:
            if self.player == 1 and self.last_hole.holeName[5] == '1':
                self.last_hole.numOfStones = 0
                the_other_hole = self.my_holes.get_hole_by_number(self.last_hole.hole_number, 2)
                sum = the_other_hole.numOfStones + 1
                the_other_hole.numOfStones = 0

                if flag:
                    draw_screen(self)
                    time.sleep(0.3)
                my_big_hole = self.my_holes.get_hole_by_number(-1, 2)
                my_big_hole.numOfStones += sum

                if flag:
                    draw_screen(self)
                    time.sleep(0.3)
            if self.player == 2 and self.last_hole.holeName[5] == '2':
                self.last_hole.numOfStones = 0
                the_other_hole = self.my_holes.get_hole_by_number(self.last_hole.hole_number, 1)
                sum = the_other_hole.numOfStones + 1
                the_other_hole.numOfStones = 0

                if flag:
                    draw_screen(self)
                    time.sleep(0.3)
                my_big_hole = self.my_holes.get_hole_by_number(-2, 2)
                my_big_hole.numOfStones += sum

                if flag:
                    draw_screen(self)
                    time.sleep(0.3)

    def check_if_to_replay(self):
        if self.player == 1:
            if self.last_hole == self.my_holes.get_hole_by_number(-1, 1):
                return True
        else:
            if self.last_hole == self.my_holes.get_hole_by_number(-2, 1):
                return True
        return False

    def check_win(self):
        n1 = 0
        for hole_index in range(1, 7):
            n1 = n1 + self.my_holes.get_hole_by_number(hole_index, 1).numOfStones
        n2 = 0
        for hole_index in range(1, 7):
            n2 = n2 + self.my_holes.get_hole_by_number(hole_index, 2).numOfStones
        if n1 != 0 and n2 != 0:
            return 0

        if self.my_holes.get_hole_by_number(-1, 2).numOfStones + n1 > self.my_holes.get_hole_by_number(-2,
                                                                                                       2).numOfStones + n2:
            return 1
        return 2

    def move_stones(self, hole, flag=True):
        n = hole.numOfStones
        hole_number = hole.hole_number
        hole.numOfStones = 0
        if flag:
            time.sleep(0.3)
            draw_screen(self)
        if self.player == 1:
            hole_number = hole_number - 1
        else:
            hole_number = hole_number + 1
        if self.player == 1:
            start = 1
        else:
            start = 0
        while n > 0:
            if start:
                while n > 0 and hole_number > 0:
                    tmp = self.my_holes.get_hole_by_number(hole_number, 1)
                    self.last_hole = tmp
                    tmp.numOfStones = tmp.numOfStones + 1
                    if flag:
                        time.sleep(0.3)
                        draw_screen(self)
                    n = n - 1
                    hole_number = hole_number - 1
                hole_number = 1
                if n > 0 and self.player == 1:
                    tmp = self.my_holes.get_hole_by_number(-1, 1)
                    self.last_hole = tmp
                    tmp.numOfStones = tmp.numOfStones + 1
                    if flag:
                        time.sleep(0.3)
                        draw_screen(self)
                    n = n - 1

            while n > 0 and hole_number <= 6:
                tmp = self.my_holes.get_hole_by_number(hole_number, 2)
                self.last_hole = tmp
                tmp.numOfStones = tmp.numOfStones + 1
                if flag:
                    time.sleep(0.3)
                    draw_screen(self)
                n = n - 1
                hole_number = hole_number + 1
            start = 1
            hole_number = 6
            if n > 0 and self.player == 2:
                tmp = self.my_holes.get_hole_by_number(-2, 1)
                self.last_hole = tmp
                tmp.numOfStones = tmp.numOfStones + 1
                if flag:
                    time.sleep(0.3)
                    draw_screen(self)
                n = n - 1

    # random
    def play_easy(self):
        hole_num = random.randint(1, 6)
        while self.my_holes.get_hole_by_number(hole_num, 1).numOfStones == 0:
            hole_num = random.randint(1, 6)
        self.move_stones(self.my_holes.get_hole_by_number(hole_num, 1))
        self.check_if_to_collect()
        if not self.check_if_to_replay():
            self.player = 2

    # greedy
    def play_med(self):
        n = 0
        max = 0
        holeIndex = None
        tmp = None
        for hole_index in range(1, 7):
            tmpGame = self.copy()
            tmp = tmpGame.my_holes.get_hole_by_number(hole_index, 1)
            if tmp.numOfStones == 0:
                continue
            tmpGame.move_stones(tmp, False)
            n = tmpGame.my_holes.get_hole_by_number(-1, 1).numOfStones
            if n > max:
                max = n
                holeIndex = hole_index
        self.move_stones(self.my_holes.get_hole_by_number(holeIndex, 1))
        self.check_if_to_collect()
        if not self.check_if_to_replay():
            self.player = 2

    # greedy for the other player
    def play_best_for_2(self):
        n = 0
        max = 0
        holeIndex = None
        tmp = None
        for hole_index in range(1, 7):
            tmpGame = self.copy()
            tmp = tmpGame.my_holes.get_hole_by_number(hole_index, 2)
            if tmp.numOfStones == 0:
                continue
            tmpGame.move_stones(tmp, False)
            n = tmpGame.my_holes.get_hole_by_number(-2, 2).numOfStones
            if n >= max:
                max = n
                holeIndex = hole_index
        self.move_stones(self.my_holes.get_hole_by_number(holeIndex, 2), False)

    # similar to min max algorithm
    def play_hard_aux(self):
        if self.check_win():
            if self.my_holes.get_hole_by_number(-1, 1).numOfStones \
                    > self.my_holes.get_hole_by_number(-2, 1).numOfStones:
                return 1

        for hole_index in range(1, 7):
            tmpGame = self.copy()
            tmp = tmpGame.my_holes.get_hole_by_number(hole_index, 1)
            if tmp.numOfStones == 0:
                continue
            tmpGame.move_stones(tmp, False)
            tmpGame.play_best_for_2()
            if tmpGame.play_hard_aux() is not None:
                return hole_index
            return None

    def play_hard(self):
        holeIndex = self.play_hard_aux()
        if holeIndex is None:
            self.play_med()
        else:
            self.move_stones(self.my_holes.get_hole_by_number(holeIndex, 1))
            self.check_if_to_collect()
            if not self.check_if_to_replay():
                self.player = 2

    def run_game(self, num_of_players, level):
        if num_of_players == 1 and self.player == 1:
            time.sleep(2)
            if level == 1:
                self.play_easy()
            if level == 2:
                self.play_med()
            if level == 3:
                self.play_hard()
            if self.check_win():
                return self.check_win()
            return 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for hole in self.my_holes.myHoles:
                    if hole.click(pos) and hole.numOfStones != 0:
                        if self.player == 1 and hole.holeName[5] == '1':
                            self.move_stones(hole)
                            self.check_if_to_collect()
                            if not self.check_if_to_replay():
                                self.player = 2
                        if self.player == 2 and hole.holeName[5] == '2':
                            self.move_stones(hole)
                            self.check_if_to_collect()
                            if not self.check_if_to_replay():
                                self.player = 1
                        if self.check_win():
                            return self.check_win()
        return 3


def main():
    running = True
    screen.fill((0, 0, 0))  # RGB
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("Click to Play Mancala!", True, (255, 0, 0))
    screen.blit(text, (100, 200))
    pygame.display.update()
    arr = []
    arr.append(0)
    arr.append(0)
    for index in range(0, 12):
        arr.append(4)
    my_holes = Holes(arr)
    game = Game(my_holes)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
    running = True

    rules_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
    running = True

    screen.fill((0, 0, 0))  # RGB
    font = pygame.font.SysFont("comicsans", 30)
    text = font.render("one player", True, (255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), [85, 180, 130, 60])
    screen.blit(text, (100, 200))
    text = font.render("two players", True, (255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), [290, 180, 130, 60])
    screen.blit(text, (300, 200))
    pygame.display.update()
    num_of_players = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 85 < pos[0] < 85 + 130 and 180 < pos[1] < 180 + 60:
                    num_of_players = 1
                    running = False
                if 290 < pos[0] < 290 + 130 and 180 < pos[1] < 180 + 60:
                    num_of_players = 2
                    running = False
    running = True
    level = 0
    if num_of_players == 1:
        screen.fill((0, 0, 0))  # RGB
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Easy", True, (255, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [85, 180, 130, 60])
        screen.blit(text, (100, 200))
        text = font.render("Medium", True, (255, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [290, 180, 130, 60])
        screen.blit(text, (300, 200))
        text = font.render("Hard", True, (255, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [480, 180, 130, 60])
        screen.blit(text, (500, 200))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 85 < pos[0] < 85 + 130 and 180 < pos[1] < 180 + 60:
                        level = 1
                        running = False
                    if 290 < pos[0] < 290 + 130 and 180 < pos[1] < 180 + 60:
                        level = 2
                        running = False
                    if 480 < pos[0] < 480 + 130 and 180 < pos[1] < 180 + 60:
                        level = 3
                        running = False
        running = True

    # game loop
    while running:
        draw_screen(game)
        win = game.run_game(num_of_players, level)
        # check if game quit
        if win == 0:
            return
        # check if someone win
        if win == 1 or win == 2:
            win_screen(win)
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        main()
                        return


main()
