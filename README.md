# Nepali Calendar Converter
#### This project is a Python-based tool to convert an English (Gregorian) date to its equivalent Nepali (Bikram Sambat) date. It also includes features to display additional details such as the corresponding tithi (lunar day), special events on that date, and Nepali weekday names with the Nepali calendar of that day.

## Features
1. English to Nepali Date Conversion: Convert any given English date (from 1944/01/01 onwards) into the Nepali (Bikram Sambat) equivalent.
2. Tithi Calculation: Displays the corresponding Nepali lunar day (Tithi) based on the Nepali calendar.
3. Nepali Weekdays: Outputs the Nepali name of the day of the week (e.g., सोमबार, मंगलबार).
4. Special Events: If the date coincides with any pre-defined important events or festivals, they are displayed.
5. Calendar Display: Prints the Nepali calendar for the provided date.

### Installation
Prerequisites
1. Python 3.x
2. info.py containing the Bikram Sambat year data (bs_years_data dictionary)

### info.py Structure
The info.py file must include a dictionary named bs_years_data that contains the mapping of Nepali years, months, and the corresponding number of days in each month.

### Usage
Run the nepali_calendar.py script to convert an English date to its Nepali equivalent with Nepali calendar of that day. After running, input the date in the format: year month day (e.g., 2024 10 21).


## Contributing
Feel free to fork the project, create a new branch, and submit a pull request with any improvements or fixes. All contributions are welcome!

1. Fork the project.
2. Create your feature branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Open a pull request.


