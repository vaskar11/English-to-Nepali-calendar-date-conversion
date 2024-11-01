'''this is the practice one'''

# from datetime import date
# import datetime
# import calendar
# from info import bs_years_data as check_dict

# # Nepali week names
# nepali_weekdays = [ "सोमबार", "मंगलबार", "बुधबार", "बिहीबार", "शुक्रबार", "शनिबार"",आइतबार"]

# # Special events dictionary
# IMPORTANT_EVENTS = {
#     (1, 1): "नयाँ वर्ष",  
#     (1, 11): "लोकतन्त्र दिवस",  
#     (1, 18): "विश्व मजदुर दिवस",  
#     (1, 30): "श्रीपञ्चमी",  
#     (3, 8): "महिला दिवस",  
#     (5, 15): "कुशे औंशी",  
#     (6, 3): "संबिधान दिवस",  
#     (6, 8): "विश्व वातावरण दिवस",  
#     (6, 11): "गणेश चतुर्थी",  
#     (7, 1): "विश्व पर्यटन दिवस",  
#     (9, 1): "विश्व पर्यटन दिवस",  
#     (9, 7): "उधौली पर्व",  
#     (9, 12): "मोहनी नख",  
#     (9, 15): "अन्नपूर्ण यात्रा",  
#     (9, 23): "यमरी पुन्ही",  
#     (10, 1): "माघे संक्रान्ति",  
#     (11, 7): "प्रजातन्त्र दिवस"
# }

# # Tithi list
# TITHI_LIST = {
#     1: "Pratipada",
#     2: "Dwitiya",
#     3: "Tritiya",
#     4: "Chaturthi",
#     5: "Panchami",
#     6: "Shashthi",
#     7: "Saptami",
#     8: "Ashtami",
#     9: "Navami",
#     10: "Dashami",
#     11: "Ekadashi",
#     12: "Dwadashi",
#     13: "Trayodashi",
#     14: "Chaturdashi",
#     15: "Purnima",
#     16: "Pratipada",   # Krishna Paksha
#     17: "Dwitiya",     # Krishna Paksha
#     18: "Tritiya",     # Krishna Paksha
#     19: "Chaturthi",   # Krishna Paksha
#     20: "Panchami",    # Krishna Paksha
#     21: "Shashthi",    # Krishna Paksha
#     22: "Saptami",     # Krishna Paksha
#     23: "Ashtami",     # Krishna Paksha
#     24: "Navami",      # Krishna Paksha
#     25: "Dashami",     # Krishna Paksha
#     26: "Ekadashi",    # Krishna Paksha
#     27: "Dwadashi",    # Krishna Paksha
#     28: "Trayodashi",   # Krishna Paksha
#     29: "Chaturdashi",  # Krishna Paksha
#     30: "Amavasya"     # Krishna Paksha
# }
# # Initialize tithi index (assuming it starts at "प्रतिपदा")
# tithi_index = 0

# print("#"*20)
# print("<----------------- Welcome to Nepali Date convertor ------------------>")
# # User input
# engYear, engMonth, engDate = map(int, input("Enter English year, month, date separated by space: \n").split())

# print("The Output is:\n")
# print()

# # Reference English and Nepali date
# startingEngYear, startingEngMonth, startingEngDay = 1944, 1, 1
# startingNepYear, startingNepMonth, startingNepDay = 2000, 9, 17
# dayOfWeek = calendar.SATURDAY

# # Difference in days
# date_ref = date(startingEngYear, startingEngMonth, startingEngDay)
# date_provided = date(engYear, engMonth, engDate)
# diff = (date_provided - date_ref).days

# # Initialize Nepali date
# nepali_Year, nepali_Month, nepali_Day = startingNepYear, startingNepMonth, startingNepDay
# day_count = dayOfWeek

# # Adjust Nepali date
# while diff != 0:
#     daysInMonth = check_dict[nepali_Year][nepali_Month - 1]
#     nepali_Day += 1
#     tithi_index = (tithi_index + 1) % len(TITHI_LIST)  # Cycle through the tithi list

#     if nepali_Day > daysInMonth:
#         nepali_Month += 1
#         nepali_Day = 1
#     if nepali_Month > 12:
#         nepali_Year += 1
#         nepali_Month = 1

#     day_count += 1
#     if day_count > 6:
#         day_count = 0
#     diff -= 1

# # Check for special events
# event = IMPORTANT_EVENTS.get((nepali_Month, nepali_Day), "Nothing special on this day")

# # Nepali week day
# nepali_week_day = nepali_weekdays[day_count]

# # Tithi for the day
# current_tithi = TITHI_LIST[tithi_index]

# # Output the equivalent Nepali date
# print(f"Nepali Date is: Year: {nepali_Year}/{nepali_Month}/ {nepali_Day} ")
# print(f"The day in Nepali is: {nepali_week_day}")
# print(f"Tithi on this day: {current_tithi}")
# print(f"Special Event on this day: {event}")
# current_time = datetime.datetime.now()
# print("Current time is:")
# print(current_time.strftime("%H:%M:%S"))


# # Calendar module is used to print calendar
# print(f"\nEnglish Calendar for Year {nepali_Year}, Month {nepali_Month}:")
# print(calendar.month(engYear, engMonth)) 


import ephem
from datetime import date, datetime
import calendar
from info import bs_years_data as check_dict


# Nepali week names
nepali_weekdays = ["सोमबार", "मंगलबार", "बुधबार", "बिहीबार", "शुक्रबार", "शनिबार", "आइतबार"]

# Special events dictionary
IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष", (1, 11): "लोकतन्त्र दिवस", (1, 18): "विश्व मजदुर दिवस",
    (1, 30): "श्रीपञ्चमी", (3, 8): "महिला दिवस", (5, 15): "कुशे औंशी",
    (6, 3): "संबिधान दिवस", (6, 8): "विश्व वातावरण दिवस", (6, 11): "गणेश चतुर्थी",
    (7, 1): "विश्व पर्यटन दिवस", (9, 1): "विश्व पर्यटन दिवस", (9, 7): "उधौली पर्व",
    (9, 12): "मोहनी नख", (9, 15): "अन्नपूर्ण यात्रा", (9, 23): "यमरी पुन्ही",
    (10, 1): "माघे संक्रान्ति", (11, 7): "प्रजातन्त्र दिवस"
}

# Tithi list for reference
TITHI_LIST = {
    # Sukla pakshya
    1: "प्रतिपदा", 2: "द्वितीया", 3: "तृतीया", 4: "चतुर्थी", 5: "पञ्चमी",
    6: "षष्ठी", 7: "सप्तमी", 8: "अष्टमी", 9: "नवमी", 10: "दशमी",
    11: "एकादशी", 12: "द्वादशी", 13: "त्रयोदशी", 14: "चतुर्दशी", 15: "पूर्णिमा",
    # Krishna pakshya
    16: "प्रतिपदा", 17: "द्वितीया", 18: "तृतीया", 19: "चतुर्थी", 20: "पञ्चमी",
    21: "षष्ठी", 22: "सप्तमी", 23: "अष्टमी", 24: "नवमी", 25: "दशमी",
    26: "एकादशी", 27: "द्वादशी", 28: "त्रयोदशी", 29: "चतुर्दशी", 30: "औंसी"
}

def get_tithi(date_in):
    
    '''The ephem library is a Python package used for performing high-precision astronomy calculations. It’s widely used for applications that need to calculate the positions of celestial objects, such as stars, planets, and moons, at a specific time and location on Earth'''
    observer = ephem.Observer()  #computer position of grahas
    observer.date = ephem.Date(date_in) #set observer date to input date which will br use to calculate sun and moon's positon of that time

    # Get solar longitude
    sun = ephem.Sun(observer)   #create a sun object linked with observer. this will represent position of sun reltive to observer's date 
    sun.compute(observer)   #compute sun's position for observer's date.
    solar_longitude = sun.hlon  #retrieves longitude of sun in radians as viewed from earth

    # Get lunar longitude
    moon = ephem.Moon(observer) #as samre as of sun
    moon.compute(observer)
    lunar_longitude = moon.hlon

    # Calculate Tithi based on the difference in longitude
    '''The difference in longitude between the Moon and the Sun is divided by 𝜋/15, which corresponds to 12 degrees, as each Tithi represents a 12° shift between the Sun and the Moon’s longitudinal positions.'''
    tithi = int((lunar_longitude - solar_longitude) % (2 * ephem.pi) / (ephem.pi / 15)) + 1
    #here at last 1 is added as tithi starts ar 1 instead of 0.
    paksha = "शुक्लपक्ष" if tithi <= 15 else "कृष्ण पक्ष"
    
    return TITHI_LIST[tithi], paksha


# Main function to convert English to Nepali date and calculate Tithi
def main():
    print("#" * 20)
    print("<----------------- Welcome to Nepali Date Converter ------------------>")
    engYear, engMonth, engDate = map(int, input("Enter English year, month, date separated by space: \n").split())

    # Reference English and Nepali date
    startingEngYear, startingEngMonth, startingEngDay = 1944, 1, 1
    startingNepYear, startingNepMonth, startingNepDay = 2000, 9, 17
    dayOfWeek = calendar.SATURDAY

    # Calculate days difference
    date_ref = date(startingEngYear, startingEngMonth, startingEngDay)
    date_provided = date(engYear, engMonth, engDate)
    diff = (date_provided - date_ref).days

    # Initialize Nepali date
    nepali_Year, nepali_Month, nepali_Day = startingNepYear, startingNepMonth, startingNepDay
    day_count = dayOfWeek

    # Adjust Nepali date based on the difference in days
    while diff != 0:
        daysInMonth = check_dict[nepali_Year][nepali_Month - 1]
        nepali_Day += 1

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

    # Nepali weekday
    nepali_week_day = nepali_weekdays[day_count]

    # Calculate Tithi for the provided date
    tithi, paksha = get_tithi(f"{engYear}/{engMonth}/{engDate}")

    # Output the equivalent Nepali date and Tithi
    print(f"Nepali Date is: Year: {nepali_Year}/{nepali_Month}/{nepali_Day}")
    print(f"The day in Nepali is: {nepali_week_day}")
    print(f"Tithi on this day: {tithi}, {paksha}")
    print(f"Special Event on this day: {event}")

    # Display current time
    current_time = datetime.now()
    print("Current time is:", current_time.strftime("%H:%M:%S"))

    # Display English calendar for provided year and month
    print(f"\nEnglish Calendar for Year {engYear}, Month {engMonth}:")
    print(calendar.month(engYear, engMonth))
    




# main function
if __name__ == "__main__":
    main()

