from geopy.distance import geodesic


def distance_two_points(coords) -> dict:
    """
    Takes 2 sets of coordinates and calculates the
    distance between them by driving and flying
    """
    coords = [float(coord) for coord in coords]
    point1 = (coords[0], coords[1])
    point2 = (coords[2], coords[3])

    distance = geodesic(point1, point2).kilometers
    driving = distance / 60
    flying = distance / 800

    transport = {'distance': distance, 'driving': driving, 'flying': flying}
    return transport


def distance_three_points(coords) -> str:
    """
    Takes 3 sets of coordinates and calculates the distance between
    both before returning the shortest distance between them
    """
    coords = [float(coord) for coord in coords]
    point1 = (coords[0], coords[1])
    point2 = (coords[2], coords[3])
    point3 = (coords[4], coords[5])

    distance_one = geodesic(point1, point2).kilometers
    distance_two = geodesic(point1, point3).kilometers

    if distance_one > distance_two:
        return f'Shortest Route: Point 1 to Point 3 is {distance_two}'
    elif distance_one < distance_two:
        return f'Shortest Route: Point 1 to Point 2 is {distance_one}'
    else:
        return f'Both routes are the same distance'
