import math

class Agent():
    def __init__(self, mediator):
        self.mediator = mediator  # An instance of Mediator class
        self.num_paths = mediator.num_paths
        self.all_stations = mediator.stations
        self.planned_paths = [[] for _ in range(self.num_paths)]    # List to store planned paths
    
    def generate_paths(self):
        pass  # Abstract method to be implemented by subclasses

    def find_closest(self, current_station, stations) ->None:
        closest = None
        min_distance = float('inf')
        for station in stations:
            distance = math.sqrt((station.position.left - current_station.position.left)**2 +
                                (station.position.top - current_station.position.top)**2)
            if distance < min_distance:
                min_distance = distance
                closest = station
        return closest
    
    def order_stations(self, station_list):
        if not station_list:
            return []

        ordered_list = [station_list[0]]  # Start with the first station
        remaining_stations = station_list[1:]  # Remaining stations to be ordered

        while remaining_stations:
            current_station = ordered_list[-1]  # Get the last added station
            next_station = self.find_closest(current_station, remaining_stations)
            ordered_list.append(next_station)
            remaining_stations.remove(next_station)

        return ordered_list
