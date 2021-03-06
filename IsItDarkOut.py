"Is it dark out?"
"by Will Schmidt"

import time

print("Is it dark outside?\n==================")

#month_number : sunset_hour
dark = {

    1: 16,
    2: 17,
    3: 18,
    4: 19,
    5: 19,
    6: 20,
    7: 20,
    8: 19,
    9: 18,
    10: 17,
    11: 16,
    12: 16

    }

#month_number : sunrise_hour
light = {

    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 4,
    7: 4,
    8: 5,
    9: 6,
    10: 6,
    11: 7,
    12: 8

    }

#get the structure containing the current time
time_now = time.localtime()

#use the 'light' and 'dark' dictionaries
#it's dark if the hour is later than or equal to the sunset time
#or earlier than the sunrise time.
if time_now.tm_hour >=dark[time_now.tm_mon] or time_now.tm_hour < light[time_now.tm_mon]:
    print("You should just look out a window, but if you really want to see if it is, Yes... you really need a bit of exercise though... :-)")
else:
    print("You should just look out a window, but if you really want to see if it is, Nope... you really need a bit of exercise though... :-)")
