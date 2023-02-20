from manim_chess.chess import get_board

from manim import *
config.frame_size = (2000, 2000)

class Chess(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(20)
        self.camera.background_color = WHITE
        fens = ["4/k3/4/K1R1/4 b - - 2 28", "3r/PPk1/p2p/2Pp/R1QK w - - 0 17", "2kr/P3/pPpp/2PR/RQ1K w - - 4 15"]
        groups = []
        for fen in fens:
            other_board = get_board(fen)
            group = Group(SurroundingRectangle(other_board, BLACK), other_board)
            group.shift(DOWN * 5)
            groups.append(group)
        
        groups[0].shift(LEFT * 5)
        groups[-1].shift(RIGHT * 5)

        divider = Rectangle(width=8, height=1, stroke_color=BLACK, fill_color=WHITE, fill_opacity=1)
        text = Text("...", color=BLACK)
        self.add(divider, text)
        self.add(*groups)
        main_board = get_board("rqkr/pppp/4/PPPP/RQKR w - - 0 1")
        rect = SurroundingRectangle(main_board, BLACK)
        main_group = Group(main_board, rect).shift(UP * 4)
        self.add(main_group)
        mid_line = Line(ORIGIN, main_group.get_bottom(), color=BLACK)
        mid_line.set_z_index(divider.z_index - 10)
        self.add(mid_line)
        mid_line = Line(ORIGIN, groups[1].get_top(), color=BLACK)
        mid_line.set_z_index(divider.z_index - 10)
        self.add(mid_line)
        mid_line = Line(ORIGIN, DOWN * 5 + RIGHT * 5 + group.height / 2 * UP, color=BLACK)
        mid_line.set_z_index(divider.z_index - 10)
        self.add(mid_line)

        mid_line = Line(ORIGIN, DOWN * 5  + LEFT * 5 + group.height / 2 * UP, color=BLACK)
        mid_line.set_z_index(divider.z_index - 10)
        self.add(mid_line)



