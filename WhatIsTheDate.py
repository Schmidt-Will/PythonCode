"What is the date?"
"by Will Schmidt"

import time

currentTime = time.localtime()

print ("What is the date?")
print ("================")
print ("The date is -", currentTime.tm_mon, "/", currentTime.tm_mday, "/", currentTime.tm_year)
print ("The time is -", currentTime.tm_hour, ":", currentTime.tm_min)
