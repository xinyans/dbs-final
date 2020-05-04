DROP SCHEMA IF EXISTS project_data CASCADE;
CREATE SCHEMA project_data;

CREATE TABLE Location_volume_temp
(
    year    Integer,
    station_ID Integer,
    county VARCHAR(127),
    signing VARCHAR(127),
    state_route VARCHAR(127),
    county_road VARCHAR(127),
    road_name VARCHAR(255),
    beginning_description TEXT,
    ending_description TEXT,
    municipality    VARCHAR(127),
    length Integer,
    functional_class Integer,
    ramp VARCHAR(1),
    bridge VARCHAR(1),
    railroad_crossing VARCHAR(1),
    one_way VARCHAR(1),
    Volume_count Integer
);

CREATE TABLE Location_volume
(
    year    Integer,
    station_ID Integer,
    county VARCHAR(127),
    signing VARCHAR(127),
    state_route VARCHAR(127),
    county_road VARCHAR(127),
    road_name VARCHAR(255),
    beginning_description TEXT,
    ending_description TEXT,
    municipality    VARCHAR(127),
    length Integer,
    functional_class Integer,
    ramp VARCHAR(1),
    bridge VARCHAR(1),
    railroad_crossing VARCHAR(1),
    one_way VARCHAR(1),
    Volume_count Integer,
    PRIMARY KEY(station_ID,year)
);

CREATE TABLE Car_crash
(
    year Integer,
    crash_descriptor TEXT,
    incident_time TIME,
    incident_date DATE,
    day_of_week VARCHAR(127),
    police_report TEXT,
    lighting_condition VARCHAR(127),
    municipality VARCHAR(127),
    collision_type_descriptor TEXT,
    county VARCHAR(127),
    road_descriptor TEXT,
    weather_conditions TEXT,
    traffic_control_device VARCHAR(127),
    road_surface_condition TEXT,
    DOT_reference_marker_location TEXT,
    pedestrian_bicyclist_action TEXT,
    event_descriptor TEXT,
    number_of_vehicles Integer
);
