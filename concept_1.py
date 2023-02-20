from manim_chess.chess import get_board
import numpy as np
from manim import *
config.frame_size = (2000, 2000)

def matrix():
    return Tex(r"$\begin{bmatrix}0.1 & 0.6 & -0.1 & ... & 0.5 & 0.1 & 0.6 \end{bmatrix}$", fill_color=BLACK).scale(1.3)

class Chess(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(20)
        self.camera.background_color = WHITE
        fens = ["r1kr/1p1p/pPpR/P1P1/R1QK b - - 4 6", "r1kr/1p1p/pPpq/P1PR/RQK1 w - - 0 4", "3r/PPk1/p1pp/2PR/RQ1K w - - 1 16"]
        boards = []
        for fen in fens:
            board = get_board(fen)
            boards.append(Group(SurroundingRectangle(board, BLACK), board))
        
        boards[0].next_to(boards[1], LEFT).shift(LEFT * 0.2)
        boards[-1].next_to(boards[1], RIGHT).shift(RIGHT * 0.2)
        statuses = [True, False, True]

        for i, status in enumerate(statuses):
            text = Text("✔" if status else "✗", color=GREEN if status else RED)
            text.scale(1.5 if not status else 1.25)
            text.next_to(boards[i], DOWN)
            self.add(text)
        self.add(*boards)