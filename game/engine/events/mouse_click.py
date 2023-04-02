import glm
from constants.dimensions import SCREEN_DIMENSIONS
from engine.events import emit_face_activated

def pointInOrOn(p1, p2, a, b):
    c1 = glm.cross(b - a, p1 - a)
    c2 = glm.cross(b - a, p2 - a)
    return glm.dot(c1, c2) >= 0

def pointInOrOnTriangle(p, a, b, c):
    test1 = pointInOrOn(p, a, b, c)
    test2 = pointInOrOn(p, b, c, a)
    test3 = pointInOrOn(p, c, a, b)
    return test1 and test2 and test3

def test_face_clicked(mouse_pos, camera, triangles):
    x = (2.0 * mouse_pos[0]) / SCREEN_DIMENSIONS[0] - 1.0;
    y = 1.0 - (2.0 * mouse_pos[1]) / SCREEN_DIMENSIONS[1];
    ray_clip = glm.vec4(x, y, -1.0, 1.0) # homogen clip coord
    inv_proj = glm.inverse(camera.projection_matrix)
    inv_vm = glm.inverse(camera.view_matrix)
    ray_eye = inv_proj * ray_clip
    ray_eye4 = glm.vec4(ray_eye.xy, -1.0, 0.0)
    ray_world = (inv_vm * ray_eye4).xyz #mouse ray
    i = 0
    f = 0
    found = -1
    while i < len(triangles):
        a = triangles[i]
        b = triangles[i+1]
        c = triangles[i+2]

        nv = glm.cross(b - a, c - a)
        mouse_distance = glm.dot(a - camera.position, nv) / glm.dot(ray_world , nv)
        p = mouse_distance * ray_world + camera.position
        if pointInOrOnTriangle(p, a, b, c) and nv.z < 0:
            found = f
            break
        f += 1
        i += 3

    if found >= 0:
        emit_face_activated(found)