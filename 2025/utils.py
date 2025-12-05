from typing import Generator


class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self._y = value

    def __str__(self) -> str:
        return f"Point(x:{self.x}|y:{self.y})"


class Grid:
    def __init__(self, array: list[list[str | int]], as_ints: bool = False) -> None:
        if as_ints:
            self._array = [[int(cell) for cell in row] for row in array]
        else:
            self._array = array
        self._height = len(array)
        self._width = len(array[0])

    @property
    def array(self) -> list[list[any]]:
        return self._array

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    def get_point(self, point: Point | tuple[int, int]) -> str | int:
        if isinstance(point, Point):
            return self._array[point.y][point.x]
        elif isinstance(point, tuple):
            return self._array[point[1]][point[0]]
        else:
            raise TypeError(
                f"Point must be either a Point objekt og at Tuple(x, y), point was {type(point)}"
            )

    def is_point_equal(self, point: Point, value: str | int) -> bool:
        return self._array[point.y][point.x] == value

    def in_bounds(self, point: Point) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def set_point(self, point: Point, value: str | int) -> None:
        self._array[point.y][point.x] = value

    def get_neighbors(self, point: Point, diagonals: bool = True) -> list[Point]:
        neighbors = []
        if diagonals:
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            ]  # left, right, up, down, and diagonals
        else:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
        for dx, dy in directions:
            new_x, new_y = point.x + dx, point.y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                neighbors.append(Point(new_x, new_y))
        return neighbors

    def iter_grid(self) -> Generator[Point, None, None]:
        for idy, row in enumerate(self.array):
            for idx, _ in enumerate(row):
                yield Point(idx, idy)

    def print_grid(self) -> None:
        for row in self.array:
            print("".join(row))
