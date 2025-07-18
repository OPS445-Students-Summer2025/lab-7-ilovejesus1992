#!/usr/bin/env python3
# Student ID: 166335232
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.minute > 60:
        sum.minute = sum.minute - 60
        sum.hour = sum.hour + 1
    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while abs(time.second) >= 60: #create a loop when second larger than 60, both positive and negative
            if time.second >= 60: #this part is the same as original code
                time.second -= 60
                time.minute += 1
            elif time.second < 0:
                time.second += 60
                time.minute -= 1
        while time.minute < 0 or time.minute >= 60: #a loop to calculate whenever minute larger than 60 or smaller than 0
            if time.minute >= 60: #this part is the original 
                time.minute -= 60
                time.hour += 1
            elif time.minute < 0: #when seconds < 0, there is a point when minute will become negative value, we adjust the hour too
                time.minute += 60
                time.hour -= 1
        time.hour = time.hour % 24 if time.hour >= 0 else (time.hour % 24) #we must make sure that the hour is a valid number after ajustment
    return None
