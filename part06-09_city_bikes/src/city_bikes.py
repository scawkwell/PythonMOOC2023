# Write your solution here
def get_station_data(filename: str):
    output = {}
    with open(filename) as file:
        for row in file:
            parts = row.strip().split(";")
            if parts[0] == "Longitude":
                continue
            output[parts[3]] = (float(parts[0]), float(parts[1]))
    return output


def distance(stations: dict, station1: str, station2: str):
    station1_long, station1_lat = stations[station1][0], stations[station1][1]
    station2_long, station2_lat = stations[station2][0], stations[station2][1]
    
    import math
    x_km = (station1_long - station2_long) * 55.26
    y_km = (station1_lat - station2_lat) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    greatest_distance_km = 0
    far_station1 = ""
    far_station2 = ""

    for station1, long_and_lat1 in stations.items():
        for station2, long_and_lat2 in stations.items():
            if station1 == station2:
                continue

            distance_km = distance(stations, station1, station2)
            
            if distance_km > greatest_distance_km:
                greatest_distance_km = distance_km
                far_station1, far_station2 = station1, station2

    return (far_station1, far_station2, greatest_distance_km)



if __name__ == "__main__":
    # stations = get_station_data('stations1.csv')
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
