import pandas as pd
from dateutil import rrule, parser
from convertdate import hebrew

date1 = '2001-01-01'
date2 = '2020-01-01'
datesx = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(date1), until=parser.parse(date2)))

hebrewCalendar = pd.DataFrame()
hebrewCalendar['date'] = datesx

hebrewCalendar['hebrewDate'] = hebrewCalendar['date'].apply(lambda x: hebrew.from_gregorian(x.year, x.month, x.day))

hebrewCalendar['hebrewMonth'] =hebrewCalendar['hebrewDate'].apply(lambda x: x[1])
hebrewCalendar['hebrewYear'] =hebrewCalendar['hebrewDate'].apply(lambda x: x[0])

Hebrew_months={
1:'NISAN',
2:'IYYAR',
3:'SIVAN',
4:'TAMMUZ',
5:'AV',
6:'ELUL',
7:'TISHRI',
8:'HESHVAN',
9:'KISLEV',
10:'TEVETH',
11:'SHEVAT',
12:'ADAR',
13:'VEADAR'
}

hebrewCalendar["hebrewMonth"].replace(Hebrew_months, inplace=True)

hebrewCalendar.to_csv("hebrewCalendar.csv")
