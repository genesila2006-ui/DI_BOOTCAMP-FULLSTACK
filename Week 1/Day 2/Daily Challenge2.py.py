import calendar
from datetime import datetime

# 1. Ask for user's birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# 2. Parse birthdate and calculate current age
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.now()

# Age calculation taking into account whether birthday has occurred this year
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# 3. Calculate candles based on the last digit of the age
num_candles = age % 10

# 4. Construct the dynamic candles line
candles_line = "i" * num_candles
top_layer = f"___{candles_line}___".center(11)

cake = f"""
       {top_layer}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# 5. Print the cake (and a second one if born on a leap year)
print(cake)

if calendar.isleap(birthdate.year):
    print(cake)