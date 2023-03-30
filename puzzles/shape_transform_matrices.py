import glm
from constants.shape import Shape

ShapeTransformMatrices: dict[Shape, glm.mat4x4] = {
  Shape.tetrahedron: glm.mat4x4
}

ShapeFaceRidges: dict[Shape, list[tuple[tuple[int,int,int], tuple[int,int,int]]]] = {
  Shape.tetrahedron: [
    # A & B
    ((0,0,0),(1,4,0)),
    ((0,1,0),(1,3,0)),
    ((0,2,0),(1,2,0)),
    ((0,3,0),(1,1,0)),
    ((0,4,0),(1,0,0)),
    # A & C
    ((0,0,4),(2,4,0)),
    ((0,1,4),(2,3,1)),
    ((0,2,4),(2,2,2)),
    ((0,3,4),(2,1,3)),
    ((0,4,4),(2,0,4)),
    # A & D
    ((0,0,0),(3,0,4)),
    ((0,0,1),(3,0,3)),
    ((0,0,2),(3,0,2)),
    ((0,0,3),(3,0,1)),
    ((0,0,4),(3,0,0)),

    # B + C
    ((1,0,0),(2,0,0)),
    ((1,0,1),(2,0,1)),
    ((1,0,2),(2,0,2)),
    ((1,0,3),(2,0,3)),
    ((1,0,4),(2,0,4)),

    # B * D
    ((1,0,4),(3,4,0)),
    ((1,1,3),(3,3,1)),
    ((1,2,2),(3,2,2)),
    ((1,3,1),(3,1,3)),
    ((1,4,0),(3,0,4)),

    # C * D
    ((2,0,0),(3,4,0)),
    ((2,1,0),(3,3,0)),
    ((2,2,0),(3,2,0)),
    ((2,3,0),(3,1,0)),
    ((2,4,0),(3,0,0)),
  ]
}
