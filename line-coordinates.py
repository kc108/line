import itertools

class Point():
    '''
    An object to represent a point in 2-dimensional space (x,y)

    Methods:
        is_between(self, point1, point2):
            Return True if the point is between point1 and point2.  Note that order matters -
            so checking point1, point2 and point2, point1 is recommended!
    '''
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def is_between(self, point1, point2):
        if (point1.x < self.x < point2.x) and (point1.y < self.y < point2.y):
            return True
        return False

class Line():
    '''
    An object to represent a line in 2-dimensional space between two points (p1, p2)

    Methods:
        is_on_line(self, point):
            Return True if the point is on the line represented by the object and is between
            the two points that make up the line (in other words, the line is infinite, so check
            if the point is actually between the beginning and end point of the line.
    '''

    def __init__(self, p1, p2):
        self.point1 = Point(p1)
        self.point2 = Point(p2)

    def __str__(self):
        return f'Line: {self.point1.x},{self.point1.y} -> {self.point2.x},{self.point2.y}'

    def is_on_line(self, point):
        dist_x_point = point.x - self.point1.x
        dist_y_point = point.y - self.point1.y

        dist_x_line = self.point2.x - self.point1.x
        dist_y_line = self.point2.y - self.point1.y

        if (dist_x_point * dist_y_line - dist_y_point * dist_x_line == 0) and point.is_between(self.point1, self.point2):
            return True
        return False


def main():
    # Define our set of points that we will evaluate
    point_set = { (1,1), (2,2), (3,3), (3,3), (2,3), (4,4), (1,2) }

    # Initialize a list of lines that pass through at least three of the given points
    three_point_lines = []

    # Use itertools.permutations to iterate through all possible 2-element combinations of the point set
    for p1, p2 in itertools.permutations(point_set, 2):

        # Create a line based on the current iteration
        line = Line(p1, p2)

        # Walk through all points in the point set
        for point in point_set:
            curr_point = Point(point)

            # Evaluate the current point to see if it is on the line and not already captured in the results
            if line.is_on_line(curr_point) and line not in three_point_lines:
                    three_point_lines.append(line)

    # Display the results
    for line in three_point_lines:
        print(f'{line}')


if __name__ == '__main__':
    main()