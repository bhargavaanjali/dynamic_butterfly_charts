import pandas as pd
from package import ColumnName, Gender, ButterflyChart, FigureHandler, HistogramFactory
from package import DataFrameFilterColumnList, DataFrameFilterColumnValue, OperationType, AppGenerator
import numpy as np
import sys

def find(string: str, substring: str) -> bool:
    return string.find(substring) != -1

def main():
    filename = 'data/vehdrindcr.csv'

    df = pd.read_csv(filename, low_memory=False)
    column_names = df.columns.tolist()
    # print('Unfiltered columns:', len(column_names))
    column_names = [c for c in column_names if not (find(c, 'ID') or find(c, 'Id'))]
    # print('Filtered columns based on Id and ID:', len(column_names))
    column_names_str_formatted = '* ' + ('\n* '.join(map(str, column_names)))
    # print(column_names_str_formatted)

    # Filtering logic
    relevant_column_names = [
        ColumnName.age,
        ColumnName.gender,
        ColumnName.speed,
        ColumnName.number_of_fatalities,
        ColumnName.vehicle_year,
        ColumnName.vehicle_make,
        ColumnName.vehicle_model,
        ColumnName.vehicle_towed,
        ColumnName.vehicle_disabled,
        ColumnName.vehicle_plate_state,
        ColumnName.vehicle_oversize,
        ColumnName.vehicle_cargo_spill,
        ColumnName.vehicle_override,
        ColumnName.vehicle_underride,
        ColumnName.vehicle_speed_before_crash,
        ColumnName.vehicle_speed_limit,
        ColumnName.vehicle_maximum_safe_speed,
        ColumnName.initial_impact,
        ColumnName.direction_of_travel,
        ColumnName.first_event,
        ColumnName.second_event,
        ColumnName.third_event,
        ColumnName.fourth_event,
        ColumnName.most_harmful_event,
        ColumnName.city,
        ColumnName.state,
        ColumnName.license_state,
        ColumnName.defective_driver_ind,
        ColumnName.year,
        ColumnName.crash_type_name,
        ColumnName.alcohol,
        ColumnName.cmv,
        ColumnName.pedestrian,
        ColumnName.bicycle,
        ColumnName.motorcycle,
        ColumnName.moped,
        ColumnName.train_related,
        ColumnName.number_vehicles,
        ColumnName.school_zone,
        ColumnName.work_zone,
        ColumnName.teen_driver_involved,
        ColumnName.distraction_involved,
        ColumnName.driver_texting_involved,
        ColumnName.driver_using_cell_phone,
        ColumnName.unbelted_fatalities,
        ColumnName.unbelted_serious_injury,
        ColumnName.alcohol_related_name,
        ColumnName.hour,
        ColumnName.month_name,
        ColumnName.day_name,
        ColumnName.three_hour_label,
        ColumnName.crash_date,
        ColumnName.county_name,
        ColumnName.city_name,
        ColumnName.town_name,
        ColumnName.crash_date_time,
        ColumnName.mile_marker,
        ColumnName.address_number,
        ColumnName.secondary_location,
        ColumnName.at_intersection,
        ColumnName.national_highway_system,
        ColumnName.route_signing,
        ColumnName.functional_class_code,
        ColumnName.route_type_description,
        ColumnName.location_type_name,
        ColumnName.route_number,
        ColumnName.route_name,
        ColumnName.postal_city_name,
        ColumnName.older_driver_inv,
        ColumnName.older_fatals,
        ColumnName.older_injured,
        ColumnName.lrg_truck,
        ColumnName.unrestrained_fatals,
        ColumnName.unrestained_injuries,
        ColumnName.ped_fatals,
        ColumnName.ped_injuries,
        ColumnName.mc_fatals,
        ColumnName.mc_injuries,
        ColumnName.bk_fatals,
        ColumnName.bk_injuries,
        ColumnName.dd_fatals,
        ColumnName.dd_injuries,
        ColumnName.unbelted_injury,
        ColumnName.number_of_injuries,
        ColumnName.child_fatals_under_8,
        ColumnName.young_driver_aged_15_to_20_in_fatal_crashes,
        ColumnName.alcohol_impaired_driver_involved,
        ColumnName.serious_injury_count,
        ColumnName.crash_time,
        ColumnName.is_secondary_crash,
        ColumnName.lane_clearance_date_time,
        ColumnName.scene_clearance_date_time,
        ColumnName.department,
        ColumnName.vahso_region,
    ]
    df = DataFrameFilterColumnList.filter(df, relevant_column_names)

    # Create app
    ag = AppGenerator(df)
    app = ag.create_app()
    app.run_server(debug=True)

if __name__ == '__main__':
    main()