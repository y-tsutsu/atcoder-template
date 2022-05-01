def is_collinear(p1, p2, p3):
    return 0 == (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def calc_triangle_area(p1, p2, p3):
    return abs((p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])) / 2
