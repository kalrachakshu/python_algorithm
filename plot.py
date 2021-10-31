import pandas as pd
import numpy as np
import folium
from code_snippets.GTFS.match_one_route_Stops import read_static_files


def get_route_id_details(route_id, routes, trips, stimes, stops):
    route_name = routes[routes.route_id == route_id].route_long_name.values[0]
    route_trip = trips[trips.route_id == route_id].trip_id.values[0]
    route_stops = stimes[stimes.trip_id == route_trip].stop_id.values
    route_stop_details = list()
    for sid in route_stops:
        stop_details = stops[stops.stop_id == sid][['stop_id', 'stop_name', 'stop_lat', 'stop_lon']].values[0]
        route_stop_details.append(stop_details)
    return route_name, np.array(route_stop_details)


def plot_route(route_details):
    m = folium.Map(location=[28.628833, 77.206805], zoom_start=10)
    for stop_detail in route_details:
        stop_id = stop_detail[0]
        stop_name = stop_detail[1]
        coord = stop_detail[2], stop_detail[3]
        popup = f'{stop_id}_{stop_name}'
        folium.Marker(coord, icon=folium.Icon(), popup=popup).add_to(m)


def get_route_stops_df(route_id, routes, trips, stimes, stops, make_csv=False):
    route_name, route_details = get_route_id_details(route_id, routes, trips, stimes, stops)
    route_stops_df = pd.DataFrame(columns=['stop_id', 'stop_name', 'stop_lat', 'stop_lon'], data=route_details)
    # if make_csv:
    #     route_stops_df.to_csv(f'{target_dir}{stop_id}_{route_name}.csv', index=False)
    return route_stops_df


def route_for_stop_id(stop_id, trips, stimes):
    trip = stimes[stimes.stop_id == stop_id].trip_id.values
    route_id = np.unique(trips[trips.trip_id.isin(trip)].route_id.values)
    return route_id
