import random
from agents.agent import Agent

class DummyAgent(Agent):
    def generate_paths(self):
        # Assign each station to at least one path randomly
        for station in self.all_stations:
            selected_path_id = random.randint(0,self.num_paths-1)
            self.planned_paths[selected_path_id].append(station)
        # Ensure all the lines connect to at least two different stations
        for station_list in self.planned_paths:
            if len(station_list) < 1:
                station_id = random.randint(0, len(self.all_stations)-1)
                station_list.append(self.all_stations[station_id])
            if len(station_list) < 2:
                station_id = random.randint(0, len(self.all_stations)-1)
                while self.all_stations[station_id] == station_list[0]:
                    station_id = random.randint(0, len(self.all_stations)-1)
                station_list.append(self.all_stations[station_id])
        
        # Optionally, each path can randomly include additional stations
        for station_list_id in range(len(self.planned_paths)):
            station_list = self.planned_paths[station_list_id]
            additional_stations = random.sample(self.all_stations, random.randint(0, len(self.all_stations) // 2))
            whether_loop = False
            for station in additional_stations:
                if station==station_list[0]:
                    whether_loop = True
                if self.mediator.check_whether_not_crossed(station, station_list):
                    station_list.append(station)
            # Order the List
            self.planned_paths[station_list_id] = self.order_stations(station_list)
            if whether_loop:
                self.planned_paths[station_list_id].append(self.planned_paths[station_list_id][0])