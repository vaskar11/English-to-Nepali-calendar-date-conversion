'''this is the practice one'''

from datetime import date
import datetime
import calendar
from info import bs_years_data as check_dict

# Nepali week names
nepali_weekdays = [ "सोमबार", "मंगलबार", "बुधबार", "बिहीबार", "शुक्रबार", "शनिबार"",आइतबार"]

# Special events dictionary
IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष",  
    (1, 11): "लोकतन्त्र दिवस",  
    (1, 18): "विश्व मजदुर दिवस",  
    (1, 30): "श्रीपञ्चमी",  
    (3, 8): "महिला दिवस",  
    (5, 15): "कुशे औंशी",  
    (6, 3): "संबिधान दिवस",  
    (6, 8): "विश्व वातावरण दिवस",  
    (6, 11): "गणेश चतुर्थी",  
    (7, 1): "विश्व पर्यटन दिवस",  
    (9, 1): "विश्व पर्यटन दिवस",  
    (9, 7): "उधौली पर्व",  
    (9, 12): "मोहनी नख",  
    (9, 15): "अन्नपूर्ण यात्रा",  
    (9, 23): "यमरी पुन्ही",  
    (10, 1): "माघे संक्रान्ति",  
    (11, 7): "प्रजातन्त्र दिवस"
}

# Tithi list
TITHI_LIST = {
    1: "Pratipada",
    2: "Dwitiya",
    3: "Tritiya",
    4: "Chaturthi",
    5: "Panchami",
    6: "Shashthi",
    7: "Saptami",
    8: "Ashtami",
    9: "Navami",
    10: "Dashami",
    11: "Ekadashi",
    12: "Dwadashi",
    13: "Trayodashi",
    14: "Chaturdashi",
    15: "Purnima",
    16: "Pratipada",   # Krishna Paksha
    17: "Dwitiya",     # Krishna Paksha
    18: "Tritiya",     # Krishna Paksha
    19: "Chaturthi",   # Krishna Paksha
    20: "Panchami",    # Krishna Paksha
    21: "Shashthi",    # Krishna Paksha
    22: "Saptami",     # Krishna Paksha
    23: "Ashtami",     # Krishna Paksha
    24: "Navami",      # Krishna Paksha
    25: "Dashami",     # Krishna Paksha
    26: "Ekadashi",    # Krishna Paksha
    27: "Dwadashi",    # Krishna Paksha
    28: "Trayodashi",   # Krishna Paksha
    29: "Chaturdashi",  # Krishna Paksha
    30: "Amavasya"     # Krishna Paksha
}
# Initialize tithi index (assuming it starts at "प्रतिपदा")
tithi_index = 0

print("#"*20)
print("<----------------- Welcome to Nepali Date convertor ------------------>")
# User input
engYear, engMonth, engDate = map(int, input("Enter English year, month, date separated by space: \n").split())

print("The Output is:\n")
print()

# Reference English and Nepali date
startingEngYear, startingEngMonth, startingEngDay = 1944, 1, 1
startingNepYear, startingNepMonth, startingNepDay = 2000, 9, 17
dayOfWeek = calendar.SATURDAY

# Difference in days
date_ref = date(startingEngYear, startingEngMonth, startingEngDay)
date_provided = date(engYear, engMonth, engDate)
diff = (date_provided - date_ref).days

# Initialize Nepali date
nepali_Year, nepali_Month, nepali_Day = startingNepYear, startingNepMonth, startingNepDay
day_count = dayOfWeek

# Adjust Nepali date
while diff != 0:
    daysInMonth = check_dict[nepali_Year][nepali_Month - 1]
    nepali_Day += 1
    tithi_index = (tithi_index + 1) % len(TITHI_LIST)  # Cycle through the tithi list

    if nepali_Day > daysInMonth:
        nepali_Month += 1
        nepali_Day = 1
    if nepali_Month > 12:
        nepali_Year += 1
        nepali_Month = 1

    day_count += 1
    if day_count > 6:
        day_count = 0
    diff -= 1

# Check for special events
event = IMPORTANT_EVENTS.get((nepali_Month, nepali_Day), "Nothing special on this day")

# Nepali week day
nepali_week_day = nepali_weekdays[day_count]

# Tithi for the day
current_tithi = TITHI_LIST[tithi_index]

# Output the equivalent Nepali date
print(f"Nepali Date is: Year: {nepali_Year}/{nepali_Month}/ {nepali_Day} ")
print(f"The day in Nepali is: {nepali_week_day}")
print(f"Tithi on this day: {current_tithi}")
print(f"Special Event on this day: {event}")
current_time = datetime.datetime.now()
print("Current time is:")
print(current_time.strftime("%H:%M:%S"))


# Calendar module is used to print calendar
print(f"\nEnglish Calendar for Year {nepali_Year}, Month {nepali_Month}:")
print(calendar.month(engYear, engMonth)) 

