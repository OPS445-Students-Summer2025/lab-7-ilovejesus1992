#!/usr/bin/env python3
# Student ID: 166335232
from lab7d import *
t1 = Time(8,0,0)
t2 = Time(8,55,0)
t3 = Time(9,50,0)
t4 = Time(9,50,0)

td = Time(0,50,0)

tsum1 = Time.sum_times(t1,td)
tsum2 = Time.sum_times(t2,td)
t3None = Time.change_time(t3,1800)   
t4None = Time.change_time(t4,-1800)
sec_time = sec_to_time(1800)

ft = Time.format_time
print(ft(t1),'+',ft(td),'-->',ft(tsum1))
print(ft(t2),'+',ft(td),'-->',ft(tsum2))
print('09:50:00 + 1800 sec','-->',ft(t3))
print('09:50:00 - 1800 sec','-->',ft(t4))
print(ft(sec_time))