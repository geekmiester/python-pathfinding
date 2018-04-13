from pathfinding.core.util import bresenham, raytrace


def test_bresenham():
    """
    test bresenham path interpolation
    """
    assert bresenham([0, 0], [2, 5]) == [
        [0, 0], [0, 1],
        [1, 2], [1, 3],
        [2, 4], [2, 5]
    ]
    assert bresenham([0, 1], [0, 4]) == [
        [0, 1], [0, 2], [0, 3], [0, 4]
    ]


def test_raytrace():
    """
    test raytrace path interpolation
    """
    assert raytrace([0, 0], [2, 5]) == [
        [0, 0], [0, 1],
        [1, 1], [1, 2], [1, 3], [1, 4],
        [2, 4], [2, 5]
    ]
    assert raytrace([0, 1], [0, 4]) == [
        [0, 1], [0, 2], [0, 3], [0, 4]
    ]