def rectVertex(point, la, lb, lc, ld, rot):
    rot = math.radians(rot)
    a = circlepos(rot, la, point)
    b = circlepos(rot - math.pi, lc, point)
    return [circlepos(rot - math.pi / 2, lb, a), circlepos(rot - math.pi / 2, lb, b), circlepos(rot + math.pi / 2, ld, b), circlepos(rot + math.pi / 2, ld, a)]
