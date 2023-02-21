from manim_chess.chess import get_board
import numpy as np
from manim import *
config.frame_size = (2000, 2000)


class Chess(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(20)
        self.camera.background_color = WHITE
        org_board = get_board("3R/1K1P/R1Pp/2Qr/2k1").shift(LEFT * 3)
        org_board = Group(SurroundingRectangle(org_board, BLACK), org_board)
        altered_board = get_board("3R/1K1P/R1Pp/2Qr/1qkq").shift(RIGHT * 3)
        altered_board = Group(SurroundingRectangle(altered_board, BLACK), altered_board)

        maxim = Text("Maksimert", color=BLACK).scale(0.8).next_to(altered_board, DOWN)
        queen = Text("'threat_opp_queen'", color=BLACK).scale(0.8).next_to(maxim, DOWN).shift(0.1)

        opp = Text("Opprinnelig", color=BLACK).scale(0.8).next_to(org_board, DOWN)
        opp.set_y(maxim.get_y())
        pos = Text("posisjon", color=BLACK).scale(0.8).next_to(opp, DOWN)
        pos.set_y(queen.get_y())
        self.add(opp, pos)

        self.add(maxim, queen)
        self.add(org_board, altered_board)