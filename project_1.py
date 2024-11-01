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



# import ephem
# from datetime import date, datetime
# import calendar
# from info import bs_years_data as check_dict


# # Nepali week names
# nepali_weekdays = ["सोमबार", "मंगलबार", "बुधबार", "बिहीबार", "शुक्रबार", "शनिबार", "आइतबार"]

# # Special events dictionary
# IMPORTANT_EVENTS = {
#     (1, 1): "नयाँ वर्ष", (1, 11): "लोकतन्त्र दिवस", (1, 18): "विश्व मजदुर दिवस",
#     (1, 30): "श्रीपञ्चमी", (3, 8): "महिला दिवस", (5, 15): "कुशे औंशी",
#     (6, 3): "संबिधान दिवस", (6, 8): "विश्व वातावरण दिवस", (6, 11): "गणेश चतुर्थी",
#     (7, 1): "विश्व पर्यटन दिवस", (9, 1): "विश्व पर्यटन दिवस", (9, 7): "उधौली पर्व",
#     (9, 12): "मोहनी नख", (9, 15): "अन्नपूर्ण यात्रा", (9, 23): "यमरी पुन्ही",
#     (10, 1): "माघे संक्रान्ति", (11, 7): "प्रजातन्त्र दिवस"
# }

# # Tithi list for reference
# TITHI_LIST = {
#     1: "प्रतिपदा", 2: "द्वितीया", 3: "तृतीया", 4: "चतुर्थी", 5: "पञ्चमी",
#     6: "षष्ठी", 7: "सप्तमी", 8: "अष्टमी", 9: "नवमी", 10: "दशमी",
#     11: "एकादशी", 12: "द्वादशी", 13: "त्रयोदशी", 14: "चतुर्दशी", 15: "पूर्णिमा",
#     16: "प्रतिपदा", 17: "द्वितीया", 18: "तृतीया", 19: "चतुर्थी", 20: "पञ्चमी",
#     21: "षष्ठी", 22: "सप्तमी", 23: "अष्टमी", 24: "नवमी", 25: "दशमी",
#     26: "एकादशी", 27: "द्वादशी", 28: "त्रयोदशी", 29: "चतुर्दशी", 30: "औंसी"
# }

# # def create_nepali_calendar(year, month, bs_month_days, start_day_idx):
# #     weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# #     months = ["Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", 
# #               "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

# #     days_in_month = bs_month_days[year][month - 1]
# #     day_list = [" "] * (start_day_idx+1)

# #     for i in range(1, int(days_in_month) + 1):
# #         day_list.append(str(i))
# #     calendar_lines = []
# #     calendar_lines.append(f"{months[month - 1]} {year}".center(29))
# #     calendar_lines.append(" ".join(weekdays))
    
# #     for i in range(0, len(day_list), 7):
# #         calendar_lines.append(" ".join(day_list[i:i + 7]))
    
# #     return "\n".join(calendar_lines)


# # def create_nepali_calendar(year, month, bs_month_days, start_day_idx):
# #     weekdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
# #     months = ["Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", 
# #               "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

# #     days_in_month = bs_month_days[year][month - 1]
    
# #     # Adjust day_list to have initial spaces based on the start_day_idx
# #     day_list = ["  "] * (start_day_idx + 1)

# #     # Add days of the month, formatted to 2 characters for consistent spacing
# #     for i in range(1, int(days_in_month) + 1):
# #         day_list.append(f"{i:>2}")

# #     # Create the calendar layout
# #     calendar_lines = []
# #     calendar_lines.append(f"{months[month - 1]} {year}".center(29))
# #     calendar_lines.append(" ".join(weekdays))
    
# #     # Arrange days in rows of 7, separated by spaces
# #     for i in range(0, len(day_list), 7):
# #         calendar_lines.append(" ".join(day_list[i:i + 7]))
    
# #     return "\n".join(calendar_lines)


# def create_nepali_calendar(year, month, bs_month_days, start_day_idx):
#     weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
#     months = ["Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", 
#               "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

#     days_in_month = bs_month_days[year][month - 1]
    
#     # Create a list of days with the correct starting index
#     day_list = [" "] * start_day_idx

#     for i in range(1, int(days_in_month) + 1):
#         day_list.append(str(i))
    
#     calendar_lines = []
#     calendar_lines.append(f"{months[month - 1]} {year}".center(29))
#     calendar_lines.append(" ".join(weekdays))
    
#     for i in range(0, len(day_list), 7):
#         calendar_lines.append(" ".join(day_list[i:i + 7]))

#     return "\n".join(calendar_lines)

# def get_tithi(date_in):
#     observer = ephem.Observer()
#     observer.date = ephem.Date(date_in)
#     sun = ephem.Sun(observer)
#     sun.compute(observer)
#     solar_longitude = sun.hlon
#     moon = ephem.Moon(observer)
#     moon.compute(observer)
#     lunar_longitude = moon.hlon

#     tithi = int((lunar_longitude - solar_longitude) % (2 * ephem.pi) / (ephem.pi / 15)) + 1
#     paksha = "शुक्लपक्ष" if tithi <= 15 else "कृष्ण पक्ष"
    
#     return TITHI_LIST[tithi], paksha


# def main():
#     print("#" * 20)
#     print("<----------------- Welcome to Nepali Date Converter ------------------>")
#     engYear, engMonth, engDate = map(int, input("Enter English year, month, date separated by space: \n").split())

#     startingEngYear, startingEngMonth, startingEngDay = 1944, 1, 1
#     startingNepYear, startingNepMonth, startingNepDay = 2000, 9, 17
#     dayOfWeek = calendar.SATURDAY

#     date_ref = date(startingEngYear, startingEngMonth, startingEngDay)
#     date_provided = date(engYear, engMonth, engDate)
#     diff = (date_provided - date_ref).days

#     nepali_Year, nepali_Month, nepali_Day = startingNepYear, startingNepMonth, startingNepDay
#     day_count = dayOfWeek

#     while diff != 0:
#         daysInMonth = check_dict[nepali_Year][nepali_Month - 1]
#         nepali_Day += 1

#         if nepali_Day > daysInMonth:
#             nepali_Month += 1
#             nepali_Day = 1
#         if nepali_Month > 12:
#             nepali_Year += 1
#             nepali_Month = 1

#         day_count += 1
#         if day_count > 6:
#             day_count = 0
#         diff -= 1

#     event = IMPORTANT_EVENTS.get((nepali_Month, nepali_Day), "Nothing special on this day")
#     nepali_week_day = nepali_weekdays[day_count]
#     tithi, paksha = get_tithi(f"{engYear}/{engMonth}/{engDate}")

#     print(f"Nepali Date is: Year: {nepali_Year}/{nepali_Month}/{nepali_Day}")
#     print(f"The day in Nepali is: {nepali_week_day}")
#     print(f"Tithi on this day: {tithi}, {paksha}")
#     print(f"Special Event on this day: {event}")

#     current_time = datetime.now()
#     print("Current time is:", current_time.strftime("%H:%M:%S"))

#     # print(f"\nEnglish Calendar for Year {engYear}, Month {engMonth}:")
#     # print(calendar.month(engYear, engMonth))

#     print(f"\nNepali Calendar for Year {nepali_Year}, Month {nepali_Month}:")
#     nepali_calendar = create_nepali_calendar(nepali_Year, nepali_Month, check_dict, day_count)
#     print(nepali_calendar)


# # Main function call
# if __name__ == "__main__":
#     main()
