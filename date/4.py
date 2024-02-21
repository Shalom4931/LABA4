from datetime import datetime

def date_difference_in_seconds(date1, date2):
  
    datetime1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    
    difference = datetime2 - datetime1

   
    difference_in_seconds = difference.total_seconds()

    return difference_in_seconds


date1 = "2024-02-20 12:00:00"
date2 = "2024-02-21 12:00:00"
difference_seconds = date_difference_in_seconds(date1, date2)
print( difference_seconds)