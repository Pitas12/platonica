import moderngl as mgl
from constants.colors import Colors
from constants.dimensions import SCREEN_DIMENSIONS
from engine.texture import get_texture
from puzzles.puzzle_graph import PuzzleGraph
from engine.renderable import Renderable
from models.tetra import Tetrahedron
from engine.camera import Camera

button_dimensions = (160, 40)
button_margin = 20


class TestScene(Renderable):
    def __init__(self, ctx: mgl.Context, switch_mode: callable):
        self.ctx = ctx
        self.switch_mode = switch_mode
        self.center = (
            SCREEN_DIMENSIONS[0] / 2,
            SCREEN_DIMENSIONS[1] / 2,
        )

    def init(self):
        self.camera = Camera(self.ctx)
        texture = get_texture(self.ctx, 'assets/textures/david-jorre-unsplash.png')
        self.subject = Tetrahedron(self.ctx, self.camera, texture)
        self.puzzle = PuzzleGraph.from_file_name("test-puzzle")

    def handle_events(self, delta_time: int):
        self.subject.handle_events(delta_time)

    def render(self, delta_time: int):
        self.ctx.clear(color=Colors.CHARCOAL)
        self.subject.render(delta_time)

    def destroy(self):
        self.subject.destroy()
