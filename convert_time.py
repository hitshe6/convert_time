#Convert 24 hours in 12 hours
#competative code

from datetime import datetime

def time_converter(railway_time):
  railway_time.strftime("%I:%M")
  print(railway_time.strftime("%I"+'H' ":" "%M"+'M' " %p"))

railway_time = datetime.strptime(input("Enter Time: "), "%H:%M")
time_converter(railway_time)
