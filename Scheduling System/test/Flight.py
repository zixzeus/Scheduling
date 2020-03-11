import pandas as pd
import numpy as np


class FlightInfo():
    def __init__(self, flight):
        self.flight_id = flight['flight_id']
        self.company_abbr = flight['company_abbr']
        self.flight_number = flight['flight_number']
        self.aircraft_attribute = flight['aircraft_attribute']
        self.flight_type = flight['flight_type']
        self.aircraft_type = flight['aircraft_type']
        self.aircraft_number = flight['aircraft_number']
        self.in_or_out = flight['in_or_out']
        self.expect_arrival_time = flight['expect_arrival_time']
        self.modify_arrival_time = flight['modify_arrival_time']
        self.real_arrival_time = flight['real_arrival_time']
        self.expect_departure_time = flight['expect_departure_time']
        self.modify_departure_time = flight['modify_departure_time']
        self.real_departure_time = flight['real_departure_time']
        self.no_passengers = flight['no_passengers']
        self.boarding_number = flight['boarding_number']
        self.boarding_type = flight['boarding_type']
        self.has_passengers_special = flight['has_passengers_special']
        self.no_passengers_special = flight['no_passengers_special']


class FlightOnline():
    def __init__(self, flight_id, company_abbr, flight_number, aircraft_attribute, flight_type, aircraft_type,
                 aircraft_number,
                 in_or_out, expect_arrival_time, modify_arrival_time, real_arrival_time, expect_departure_time,
                 modify_departure_time, real_departure_time, no_passengers, boarding_number, boarding_type,
                 has_passengers_special=None, no_passengers_special=None):
        self.flight_id = flight_id
        self.company_abbr = company_abbr
        self.flight_number = flight_number
        self.aircraft_attribute = aircraft_attribute
        self.flight_type = flight_type
        self.aircraft_type = aircraft_type
        self.aircraft_number = aircraft_number
        self.in_or_out = in_or_out
        self.expect_arrival_time = expect_arrival_time
        self.modify_arrival_time = modify_arrival_time
        self.real_arrival_time = real_arrival_time
        self.expect_departure_time = expect_departure_time
        self.modify_departure_time = modify_departure_time
        self.real_departure_time = real_departure_time
        self.no_passengers = no_passengers
        self.boarding_number = boarding_number
        self.boarding_type = boarding_type
        self.has_passengers_special = has_passengers_special
        self.no_passengers_special = no_passengers_special


class FlightInfoTable():
    def __init__(self, FlightInfo):
        self.FlightInfoTable = pd.read_excel(FlightInfo, sheet_name='flights',
                                             names=['flight_id', 'company_abbr', 'flight_number', 'aircraft_attribute',
                                                    'flight_type', 'aircraft_type', 'aircraft_number', 'in_or_out',
                                                    'expect_arrival_time',
                                                    'modify_arrival_time', 'real_arrival_time', 'expect_departure_time',
                                                    'modify_departure_time', 'real_departure_time',
                                                    'no_passengers', 'boarding_number', 'boarding_type',
                                                    'has_passengers_special', 'no_passengers_special'])

    def show(self):
        print(self.FlightInfoTable)

    def content(self):
        return self.FlightInfoTable

class FlightOnlineTable():
    def __init__(self):
        pass
