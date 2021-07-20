# -*- coding: utf-8 -*-

import datetime

class Time_Sequence:

    def __init__(self, start_Time, end_Time, time_step):
        self.__setup_ts(self.__parse_string_to_date(start_Time),
                        self.__parse_string_to_date(end_Time),
                        datetime.timedelta(minutes = int(time_step)))
                        
    def __parse_string_to_date(self, date_str):
        splitted_date = date_str.split()
        date_days = splitted_date[0].split('-')
        date_hours = splitted_date[1].split(':')
        return datetime.datetime(int(date_days[0]),
                                 int(date_days[1]),
                                 int(date_days[2]),
                                 int(date_hours[0]),
                                 int(date_hours[1]))
        
    def __setup_ts(self, start_Time, end_Time, time_step):
        self.start_Time = start_Time
        self.end_Time = end_Time
        self.time_step = time_step