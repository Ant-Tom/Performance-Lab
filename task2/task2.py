
import math

def read_circle_data():
    with open("circle.txt") as f:
        data = f.readlines()
        x_center, y_center, radius = float(data[0]), float(data[1]), float(data[2])
    return x_center, y_center, radius


def read_points_data():
    with open("dot.txt") as f:
        data = f.readlines()
    points = [(float(line.split()[0]), float(line.split()[1])) for line in data]
    return points


def calculate_point_position(x_center, y_center, radius, x_point, y_point):
    distance = math.sqrt((x_point - x_center)**2 + (y_point - y_center)**2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    x_center, y_center, radius = read_circle_data()
    points = read_points_data()

    for x_point, y_point in points:
        position = calculate_point_position(x_center, y_center, radius, x_point, y_point)
        print(position)


if __name__ == "__main__":
    main()
