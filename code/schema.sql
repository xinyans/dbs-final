DROP SCHEMA IF EXISTS project_data CASCADE;
CREATE SCHEMA project_data;
ALTER ROLE dbms_project_user SET search_path TO project_data, public;

CREATE TABLE Location
(
    year    Integer,
    municipality    VARCHAR(127),
    station_ID  Integer,
    county VARCHAR(127),
    Volume_count Integer,
    road_name VARCHAR(255),
    PRIMARY KEY(road_name,station_ID,year)
);
CREATE TABLE Road_info
(
    road_name VARCHAR(255),
    station_ID Integer,
    signing VARCHAR(127),
    beginning_description TEXT,
    ending_description TEXT,
    length Integer,
    functional_class Integer,
    ramp VARCHAR(1),
    bridge VARCHAR(1),
    railroad_crossing VARCHAR(1),
    one_way VARCHAR(1),
    PRIMARY KEY(road_name,station_ID)
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
