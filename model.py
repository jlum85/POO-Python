import matplotlib.pyplot as plt
import json
import math

import matplotlib as mil
mil.use('TkAgg')


class Agent:

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)


class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        # We store the degree values, but we will be mostly using radians
        # because they are much more convenient for computation purposes.

        # assert : Lève une exception si renvoie False
        assert -180 <= longitude_degrees <= 180
        self.longitude_degrees = longitude_degrees

        assert -90 <= latitude_degrees <= 90
        self.latitude_degrees = latitude_degrees

    @property
    def longitude(self):
        # Longitude in radians
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        # Latitude in radians
        return self.latitude_degrees * math.pi / 180


class Zone:
    """
    A rectangular geographic area bounded by two corners. The corners can
    be top-left and bottom right, or top-right and bottom-left so you should be
    careful when computing the distances between them.
    """
    ZONES = []

    # Attributs de classe (constante si hors de la classe) car on fait cls.WIDTH_DEGREES
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1  # degrees of longitude
    HEIGHT_DEGREES = 1  # degrees of
    EARTH_RADIUS_KILOMETERS = 6371

    # S'il y a un attribut d'instance, il va dans __init__
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    @property
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        # Note that here we access the class attribute via "self" and it
        # doesn't make any difference
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population / self.area

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        # agreeableness = []
        # for inhabitant in self.inhabitants:
        #     agreeableness.append(inhabitant.agreableness)
        # return sum(agreeableness) / self.population
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def contains(self, position):
        """Return True if the zone contains this position"""
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(
                self.corner1.latitude, self.corner2.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            # Initialize zones automatically if necessary
            cls._initialize_zones()

        # Compute the index in the ZONES array that contains the given position
        longitude_index = int(
            (position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int(
            (position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES -
                              cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)  # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    @classmethod
    def _initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(
                    longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)


class BaseGraph:

    def __init__(self):
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "X-axis label"
        self.show_grid = True

    def show(self, zones):
        # x_values = gather only x_values from our zones
        # y_values = gather only y_values from our zones
        x_values, y_values = self.xy_values(zones)
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def xy_values(self, zones):
        raise NotImplementedError


class AgreeablenessGraph(BaseGraph):

    def __init__(self):
        # Call base constructor
        super(AgreeablenessGraph, self).__init__()
        # super().__init__()
        self.title = "Nice people live in the countryside"
        self.x_label = "population density"
        self.y_label = "agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values


def main():
    # Zone.initialize_zones()
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        # print(agent.agreeableness)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        # print("Zone population: ", zone.population)
        # print(zone.average_agreeableness())

    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)


main()

# agent = Agent(agent_attributes)
# print(agent.agreeableness)
# print(agent.neuroticism)
