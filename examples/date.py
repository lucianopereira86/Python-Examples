# Importing libraries
from datetime import datetime, timedelta
# Current datetime
now = datetime.now()
print('Now = ' + str(now))

# Yesterday
one_day = timedelta(days=1)
yesterday = now - one_day
print('Yesterday = ' + str(yesterday))

# Last week
one_week = timedelta(weeks=1)
last_week = now - one_week
print('Last week = ' + str(last_week))

# Formatting date
day = now.day
month = now.month
year = now.year
print(f'Date = {day}/{month}/{year}')

# Formatting time
hour = now.hour
minute = now.minute
second = now.second
print(f'Time = {hour}:{minute}:{second}')

# Input date
input_date = input('Type a date with the format: (dd/mm/yyyy)\n')
real_date = datetime.strptime(input_date, '%d/%m/%Y')
print('Your date is {0}'.format(str(real_date)))

# Input time
input_time = input('Type a time with the format: (hh:mm)\n')
real_time = datetime.strptime(input_time, '%H:%M')
print('Your time is {0}'.format(str(real_time)))
