from manim_chess.chess import get_board

from manim import *
config.frame_size = (2000, 2000)

class Chess(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(20)
        self.camera.background_color = WHITE
        board = get_board("3r/PPk1/p2p/2Pp/R1QK w - - 0 17")
        board = Group(SurroundingRectangle(board, BLACK), board)
        self.add(board)
        model = Rectangle(BLACK, fill_color=WHITE, fill_opacity=1)
        arr = Arrow(LEFT, RIGHT, stroke_color=BLACK, fill_color=BLACK)
        arr.next_to(model, LEFT)
        board.next_to(arr, LEFT)
        model_text = Tex("$f(x)$", color=DARK_BLUE).scale(1.25)
        model_text.set_z_index(model.get_z() + 1)
        arr_right = Arrow(LEFT, RIGHT, stroke_color=BLACK, fill_color=BLACK)
        arr_right.next_to(model, RIGHT)
        eval = Tex("$-0.2$", color=BLACK).scale(1.5).next_to(arr_right, RIGHT)
        self.add(model, board, arr, model_text, arr_right, eval)



