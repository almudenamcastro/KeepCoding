# WHAT YEAR DAY IS IT TODAY?
# This program asks the user for a date and returns the number of days that have passed since the beginning of the year.

month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# ask for a date
day = int(input("dia: "))
month = int(input("mes: "))
year = int(input("año: "))

# is it a leap year?
def is_leap (year):
  '''
  input: year (four digits)
  output: boolean value, is it a leap-year? 
  '''
  if year%4 != 0:
    return False
  if year%400 == 0: 
    return True
  elif year%100 ==0: 
    return False
  else: 
    return True
  
if is_leap(year): 
  month_length[1] = 29

# start counter
day_count = 0

# add days of the passed months
i = 1
while i < month:
    day_count += month_length[i-1]
    i += 1

# add the passed days of the month
day_count += day

#pritn result
print(day_count)

