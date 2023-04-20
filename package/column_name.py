from dataclasses import dataclass, fields, field
from typing import List

@dataclass(frozen=True)
class ColumnName:
    age: str = 'DriverAge'
    gender: str = 'GenderID'
    speed: str = 'Speed'
    number_of_fatalities: str = 'Number_Of_Fatalities'
    vehicle_year: str = 'VehicleYear'
    vehicle_make: str = 'VehicleMake'
    vehicle_model: str = 'VehicleModel'
    vehicle_disabled: str = 'VehicleDisabled'
    vehicle_towed : str = 'VehicleTowed'
    vehicle_plate_state: str = 'VehiclePlateState'
    vehicle_oversize: str = 'VehicleOversize'
    vehicle_cargo_spill: str = 'VehicleCargoSpill'
    vehicle_override : str = 'VehicleOverride'
    vehicle_underride: str = 'VehicleUnderride'
    vehicle_speed_before_crash: str = 'VehicleSpeedBeforeCrash'
    vehicle_speed_limit: str = 'VehicleSpeedLimit'
    vehicle_maximum_safe_speed: str = 'VehicleMaximumSafeSpeed'
    initial_impact: str = 'InitialImpact'
    direction_of_travel: str = 'DirectionOfTravel'
    first_event: str = 'FirstEvent'
    second_event: str = 'SecondEvent'
    third_event : str = 'ThirdEvent'
    fourth_event: str = 'FourthEvent'












