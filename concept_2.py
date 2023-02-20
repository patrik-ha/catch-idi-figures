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
        board = get_board("3r/PPk1/p2p/2Pp/R1QK w - - 0 17")
        board = Group(SurroundingRectangle(board, BLACK), board)
        broken_1 = ImageMobject("firkant_1_o.png").scale(0.55).shift(LEFT * 2)
        broken_2 = ImageMobject("firkant_2_o.png").scale(0.55).shift(RIGHT * 2)
        small_rect = Rectangle(height=2.75, width=0.25, color=DARK_BLUE)
        small_arr = Arrow(LEFT, RIGHT, stroke_color=DARK_BLUE, fill_color=DARK_BLUE).next_to(small_rect, LEFT)
        small_arr.set_z(broken_1.get_z() - 1)
        small_arr_2 = Arrow(LEFT, RIGHT, stroke_color=DARK_BLUE, fill_color=DARK_BLUE).next_to(small_rect, RIGHT)
        small_arr_2.set_z(broken_2.get_z() - 1)
        broken = Group(broken_1, broken_2, small_rect, small_arr, small_arr_2)
        self.add(broken)
        self.bring_to_back(small_arr_2)
        self.bring_to_back(small_arr)
        self.add(board)
        arr = Arrow(LEFT, RIGHT, stroke_color=BLACK, fill_color=BLACK)
        arr.next_to(broken, LEFT)        
        board.next_to(arr, LEFT)        
        arr_right = Arrow(LEFT, RIGHT, stroke_color=BLACK, fill_color=BLACK)
        arr_right.next_to(board, RIGHT)
        self.add(arr)
        self.add(board)
        self.add(arr_right)
        top_arrow = Arrow(DOWN, UP * 2, stroke_color=BLACK, fill_color=BLACK).next_to(broken, UP)
        self.add(top_arrow)
        arr_right = Arrow(LEFT, RIGHT, stroke_color=BLACK, fill_color=BLACK)
        arr_right.next_to(broken, RIGHT)
        eval = Tex("$-0.2$", color=BLACK).scale(1.5).next_to(arr_right, RIGHT)
        self.add(matrix().next_to(top_arrow, UP), arr_right, eval)
