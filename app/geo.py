from __future__ import division
__author__ = 'deonheyns'
from geopy import Point
from geopy.distance import VincentyDistance


def point_on_a_radius(lat, lon, dist_miles=0.5, bearing=0):
    """
    Returns a tuple of Longitude, Latitude given the dist_miles (radius) and bearing (degree)
    """
    X, Y, b = VincentyDistance(miles=dist_miles).destination(Point(lat, lon), bearing)
    return Y, X


def points_on_a_radius(lat, lon, dist_miles, num_of_points):
    """
    Returns a list with the num_of_points of tuples of Longitude, Latitude given the dist_miles (radius)
    """
    result = []
    degree = 360 / num_of_points
    increment = degree
    for i in range(0, int(num_of_points)):
        result.append(point_on_a_radius(lat, lon, dist_miles, increment))
        increment += degree

    return result
