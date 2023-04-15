import glm

from engine.animation import Animator, AnimationLerper, AnimationLerpFunction
from ui.image_plane import ImagePlane

DISPLACE = 0.001

class NextButton(ImagePlane):
    def __init__( self, ctx, camera_matrix, position, **kwargs):
        super().__init__(
            ctx, camera_matrix,
            position, glm.vec2(0.08, 0.08),
            "next_button.png", **kwargs)
        
        self.matrix = self.matrix
        self.animate_matrix = glm.mat4()
        self.position_animator = Animator(
            AnimationLerper(AnimationLerpFunction.linear, 1000),
            start_value=-DISPLACE,
            reversible=True
        )
        self.position_animator.start(DISPLACE)
    
    def set_active(self, active):
        self.click_detector.is_enabled = active
    
    def is_active(self):
        return self.click_detector.is_enabled
    
    def render(self, delta_time: int, opacity=1.0):
        d = self.position_animator.frame(delta_time)
        self.animate_matrix  = self.animate_matrix * glm.translate(glm.vec3(d, 0, 0))
        matrix = self.animate_matrix * self.matrix
        self.obj.shader["m_mvp"].write(matrix)
        super().render(delta_time)