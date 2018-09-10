import random


employeeNames = ["Emek", "Emek",
                 "Shalev", "Shalev", "Shalev",
                 "Katriel", "Katriel", "Katriel", "Katriel", "Katriel",
                 "Andrey", "Andrey", "Andrey",
                 "Goldschmidt", "Goldschmidt", "Goldschmidt", "Goldschmidt", "Goldschmidt",
                 "Alex", "Alex", "Alex", "Alex", "Alex",
                 "Shmuel", "Shmuel", "Shmuel", "Shmuel", "Shmuel",
                 "Ram", "Ram", "Ram", "Ram", "Ram",
                 "Itay", "Itay", "Itay", "Itay", "Itay",
                 "Dean", "Dean", "Dean", "Dean", "Dean",
                 "Adam", "Adam",
                 "Ronen", "Ronen", "Ronen"]


proTools = "Itay"

FormerWeek = ["Adam"]


sundayMorningLimits = ["Andrey", "Emek", "Shalev", "Ronen"]
sundayEveningLimits = ["Andrey", "Emek", "Shalev", "Ronen"]
sundayNightLimits = ["Andrey", "Emek", "Shalev", "Ronen"]

mondayMorningLimits = ["Andrey", "Emek", "Shalev"]
mondayEveningLimits = ["Andrey", "Emek", "Shalev"]
mondayNightLimits = ["Andrey", "Emek", "Shalev"]

tuesdayMorningLimits = ["Emek", "Dean"]
tuesdayEveningLimits = ["Emek", "Dean"]
tuesdayNightLimits = ["Adam", "Alex", "Andrey", "Emek", "Dean"]

wednesdayMorningLimits = ["Adam", "Andrey", "Emek"]
wednesdayEveningLimits = ["Adam", "Andrey", "Emek", "Dean"]
wednesdayNightLimits = []

thursdayMorningLimits = ["Adam", "Emek"]
thursdayEveningLimits = ["Adam", "Emek", "Dean"]
thursdayNightLimits = ["Adam", "Emek", "Dean"]

fridayMorningLimits = ["Adam", "Katriel", "Shalev", "Ronen"]
fridayEveningLimits = ["Adam", "Katriel", "Shalev", "Ronen"]
fridayNightLimits = ["Adam", "Katriel", "Ronen", "Ram"]

saturdayMorningLimits = ["Adam", "Katriel", "Ram"]
saturdayEveningLimits = ["Adam", "Alex", "Katriel"]
saturdayNightLimits = ["Adam", "Katriel"]

SundayMorning = []
SundayEvening = []
SundayTurner = []
SundayNight = []
SundayProtools = []
SundayArabic = []

MondayMorning = []
MondayEvening = []
MondayTurner = []
MondayNight = []
MondayProtools = []
MondayArabic = []

TuesdayMorning = []
TuesdayEvening = []
TuesdayTurner = []
TuesdayNight = []
TuesdayProtools = []
TuesdayArabic = []

WednesdayMorning = []
WednesdayEvening = []
WednesdayTurner = []
WednesdayNight = []
WednesdayProtools = []
WednesdayArabic = []

ThursdayMorning = []
ThursdayEvening = []
ThursdayTurner = []
ThursdayNight = []
ThursdayProtools = []
ThursdayArabic = []

FridayMorning = []
FridayEvening = []
FridayTurner = []
FridayNight = []
FridayProtools = []
FridayArabic = []

SaturdayMorning = []
SaturdayEvening = []
SaturdayTurner = []
SaturdayNight = []
SaturdayProtools = []
SaturdayArabic = []


def sunday_protools(x):
    while len(SundayProtools) < x:
        SundayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", SundayProtools)


def monday_protools(x):
    while len(MondayProtools) < x:
        MondayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", MondayProtools)


def tuesday_protools(x):
    while len(TuesdayProtools) < x:
        TuesdayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", TuesdayProtools)


def wednesday_protools(x):
    while len(WednesdayProtools) < x:
        WednesdayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", WednesdayProtools)


def thursday_protools(x):
    while len(ThursdayProtools) < x:
        ThursdayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", ThursdayProtools)


def friday_protools(x):
    while len(FridayProtools) < x:
        FridayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", FridayProtools)


def saturday_protools(x):
    while len(SaturdayProtools) < x:
        SaturdayProtools.append(proTools)
        employeeNames.remove(proTools)
        print("ProTools: ", SaturdayProtools)


def sunday_morning(x):
    while len(SundayMorning) < x:
        a = random.choice(employeeNames)
        if a in sundayMorningLimits:
            pass
        elif a in FormerWeek:
            pass
        elif a in SundayProtools:
            pass
        elif a in SundayMorning:
            pass
        else:
            SundayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", SundayMorning)


def sunday_evening(x):
    while len(SundayEvening) < x:
        a = random.choice(employeeNames)
        if a in sundayEveningLimits:
            pass
        elif a in FormerWeek:
            pass
        elif a in SundayProtools:
            pass
        elif a in SundayMorning:
            pass
        elif a in SundayEvening:
            pass
        else:
            SundayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", SundayEvening)


def sunday_arabic(x):
    while len(SundayArabic) < x:
        a = random.choice(employeeNames)
        if a in sundayMorningLimits:
            pass
        elif a in sundayEveningLimits:
            pass
        elif a in FormerWeek:
            pass
        elif a in SundayProtools:
            pass
        elif a in SundayMorning:
            pass
        elif a in SundayEvening:
            pass
        elif a in SundayArabic:
            pass
        else:
            SundayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", SundayArabic)


def sunday_turner(x):
    while len(SundayTurner) < x:
        a = random.choice(employeeNames)
        if a in sundayMorningLimits:
            pass
        elif a in sundayEveningLimits:
            pass
        elif a in FormerWeek:
            pass
        elif a in SundayProtools:
            pass
        elif a in SundayMorning:
            pass
        elif a in SundayEvening:
            pass
        elif a in SundayArabic:
            pass
        elif a in SundayTurner:
            pass
        else:
            SundayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", SundayTurner)


def sunday_night(x):
    while len(SundayNight) < x:
        a = random.choice(employeeNames)
        if a in sundayNightLimits:
            pass
        elif a in SundayProtools:
            pass
        elif a in SundayMorning:
            pass
        elif a in SundayEvening:
            pass
        elif a in SundayTurner:
            pass
        elif a in SundayArabic:
            pass
        elif a in SundayNight:
            pass
        else:
            SundayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", SundayNight)


def monday_morning(x):
    while len(MondayMorning) < x:
        a = random.choice(employeeNames)
        if a in sundayMorningLimits:
            pass
        elif a in SundayNight:
            pass
        elif a in SundayEvening:
            pass
        elif a in MondayProtools:
            pass
        elif a in MondayMorning:
            pass
        else:
            MondayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", MondayMorning)


def monday_evening(x):
    while len(MondayEvening) < x:
        a = random.choice(employeeNames)
        if a in mondayEveningLimits:
            pass
        elif a in SundayNight:
            pass
        elif a in MondayProtools:
            pass
        elif a in MondayMorning:
            pass
        elif a in MondayEvening:
            pass
        else:
            MondayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", MondayEvening)


def monday_arabic(x):
    while len(MondayArabic) < x:
        a = random.choice(employeeNames)
        if a in mondayMorningLimits:
            pass
        elif a in mondayEveningLimits:
            pass
        elif a in SundayNight:
            pass
        elif a in MondayProtools:
            pass
        elif a in MondayMorning:
            pass
        elif a in MondayEvening:
            pass
        elif a in MondayArabic:
            pass
        else:
            MondayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", MondayArabic)


def monday_turner(x):
    while len(MondayTurner) < x:
        a = random.choice(employeeNames)
        if a in mondayMorningLimits:
            pass
        elif a in mondayEveningLimits:
            pass
        elif a in SundayNight:
            pass
        elif a in MondayProtools:
            pass
        elif a in MondayMorning:
            pass
        elif a in MondayEvening:
            pass
        elif a in MondayArabic:
            pass
        elif a in MondayTurner:
            pass
        else:
            MondayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", MondayTurner)


def monday_night(x):
    while len(MondayNight) < x:
        a = random.choice(employeeNames)
        if a in mondayNightLimits:
            pass
        elif a in MondayProtools:
            pass
        elif a in MondayMorning:
            pass
        elif a in MondayEvening:
            pass
        elif a in MondayTurner:
            pass
        elif a in MondayArabic:
            pass
        elif a in MondayNight:
            pass
        else:
            MondayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", MondayNight)


def tuesday_morning(x):
    while len(TuesdayMorning) < x:
        a = random.choice(employeeNames)
        if a in tuesdayMorningLimits:
            pass
        elif a in MondayNight:
            pass
        elif a in MondayEvening:
            pass
        elif a in TuesdayProtools:
            pass
        elif a in TuesdayMorning:
            pass
        else:
            TuesdayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", TuesdayMorning)


def tuesday_evening(x):
    while len(TuesdayEvening) < x:
        a = random.choice(employeeNames)
        if a in tuesdayEveningLimits:
            pass
        elif a in MondayNight:
            pass
        elif a in TuesdayProtools:
            pass
        elif a in TuesdayMorning:
            pass
        elif a in TuesdayEvening:
            pass
        else:
            TuesdayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", TuesdayEvening)


def tuesday_arabic(x):
    while len(TuesdayArabic) < x:
        a = random.choice(employeeNames)
        if a in tuesdayMorningLimits:
            pass
        elif a in tuesdayEveningLimits:
            pass
        elif a in MondayNight:
            pass
        elif a in TuesdayProtools:
            pass
        elif a in TuesdayMorning:
            pass
        elif a in TuesdayEvening:
            pass
        elif a in TuesdayArabic:
            pass
        else:
            TuesdayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", TuesdayArabic)


def tuesday_turner(x):
    while len(TuesdayTurner) < x:
        a = random.choice(employeeNames)
        if a in tuesdayMorningLimits:
            pass
        elif a in tuesdayEveningLimits:
            pass
        elif a in MondayNight:
            pass
        elif a in TuesdayProtools:
            pass
        elif a in TuesdayMorning:
            pass
        elif a in TuesdayEvening:
            pass
        elif a in TuesdayArabic:
            pass
        elif a in TuesdayTurner:
            pass
        else:
            TuesdayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", TuesdayTurner)


def tuesday_night(x):
    while len(TuesdayNight) < x:
        a = random.choice(employeeNames)
        if a in tuesdayNightLimits:
            pass
        elif a in TuesdayProtools:
            pass
        elif a in TuesdayMorning:
            pass
        elif a in TuesdayEvening:
            pass
        elif a in TuesdayTurner:
            pass
        elif a in TuesdayArabic:
            pass
        elif a in TuesdayNight:
            pass
        else:
            TuesdayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", TuesdayNight)


def wednesday_morning(x):
    while len(WednesdayMorning) < x:
        a = random.choice(employeeNames)
        if a in wednesdayMorningLimits:
            pass
        elif a in TuesdayNight:
            pass
        elif a in TuesdayEvening:
            pass
        elif a in WednesdayProtools:
            pass
        elif a in WednesdayMorning:
            pass
        else:
            WednesdayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", WednesdayMorning)


def wednesday_evening(x):
    while len(WednesdayEvening) < x:
        a = random.choice(employeeNames)
        if a in wednesdayEveningLimits:
            pass
        elif a in TuesdayNight:
            pass
        elif a in WednesdayProtools:
            pass
        elif a in WednesdayMorning:
            pass
        elif a in WednesdayEvening:
            pass
        else:
            WednesdayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", WednesdayEvening)


def wednesday_arabic(x):
    while len(WednesdayArabic) < x:
        a = random.choice(employeeNames)
        if a in wednesdayMorningLimits:
            pass
        elif a in wednesdayEveningLimits:
            pass
        elif a in TuesdayNight:
            pass
        elif a in WednesdayProtools:
            pass
        elif a in WednesdayMorning:
            pass
        elif a in WednesdayEvening:
            pass
        elif a in WednesdayArabic:
            pass
        else:
            WednesdayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", WednesdayArabic)


def wednesday_turner(x):
    while len(WednesdayTurner) < x:
        a = random.choice(employeeNames)
        if a in wednesdayMorningLimits:
            pass
        elif a in wednesdayEveningLimits:
            pass
        elif a in TuesdayNight:
            pass
        elif a in WednesdayProtools:
            pass
        elif a in WednesdayMorning:
            pass
        elif a in WednesdayEvening:
            pass
        elif a in WednesdayArabic:
            pass
        elif a in WednesdayTurner:
            pass
        else:
            WednesdayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", WednesdayTurner)


def wednesday_night(x):
    while len(WednesdayNight) < x:
        a = random.choice(employeeNames)
        if a in wednesdayNightLimits:
            pass
        elif a in WednesdayProtools:
            pass
        elif a in WednesdayMorning:
            pass
        elif a in WednesdayEvening:
            pass
        elif a in WednesdayTurner:
            pass
        elif a in WednesdayArabic:
            pass
        elif a in WednesdayNight:
            pass
        else:
            WednesdayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", WednesdayNight)


def thursday_morning(x):
    while len(ThursdayMorning) < x:
        a = random.choice(employeeNames)
        if a in thursdayMorningLimits:
            pass
        elif a in WednesdayNight:
            pass
        elif a in WednesdayEvening:
            pass
        elif a in ThursdayProtools:
            pass
        elif a in ThursdayMorning:
            pass
        else:
            ThursdayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", ThursdayMorning)


def thursday_evening(x):
    while len(ThursdayEvening) < x:
        a = random.choice(employeeNames)
        if a in thursdayEveningLimits:
            pass
        elif a in WednesdayNight:
            pass
        elif a in ThursdayProtools:
            pass
        elif a in ThursdayMorning:
            pass
        elif a in ThursdayEvening:
            pass
        else:
            ThursdayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", ThursdayEvening)


def thursday_arabic(x):
    while len(ThursdayArabic) < x:
        a = random.choice(employeeNames)
        if a in thursdayMorningLimits:
            pass
        elif a in thursdayEveningLimits:
            pass
        elif a in WednesdayNight:
            pass
        elif a in ThursdayProtools:
            pass
        elif a in ThursdayMorning:
            pass
        elif a in ThursdayEvening:
            pass
        elif a in ThursdayArabic:
            pass
        else:
            ThursdayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", ThursdayArabic)


def thursday_turner(x):
    while len(ThursdayTurner) < x:
        a = random.choice(employeeNames)
        if a in thursdayMorningLimits:
            pass
        elif a in thursdayEveningLimits:
            pass
        elif a in WednesdayNight:
            pass
        elif a in ThursdayProtools:
            pass
        elif a in ThursdayMorning:
            pass
        elif a in ThursdayEvening:
            pass
        elif a in ThursdayArabic:
            pass
        elif a in ThursdayTurner:
            pass
        else:
            ThursdayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", ThursdayTurner)


def thursday_night(x):
    while len(ThursdayNight) < x:
        a = random.choice(employeeNames)
        if a in thursdayNightLimits:
            pass
        elif a in ThursdayProtools:
            pass
        elif a in ThursdayMorning:
            pass
        elif a in ThursdayEvening:
            pass
        elif a in ThursdayTurner:
            pass
        elif a in ThursdayArabic:
            pass
        elif a in ThursdayNight:
            pass
        else:
            ThursdayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", ThursdayNight)


def friday_morning(x):
    while len(FridayMorning) < x:
        a = random.choice(employeeNames)
        if a in fridayMorningLimits:
            pass
        elif a in ThursdayNight:
            pass
        elif a in TuesdayEvening:
            pass
        elif a in FridayProtools:
            pass
        elif a in FridayMorning:
            pass
        else:
            FridayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", FridayMorning)


def friday_evening(x):
    while len(FridayEvening) < x:
        a = random.choice(employeeNames)
        if a in fridayEveningLimits:
            pass
        elif a in ThursdayNight:
            pass
        elif a in FridayProtools:
            pass
        elif a in FridayMorning:
            pass
        elif a in FridayEvening:
            pass
        else:
            FridayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", FridayEvening)


def friday_arabic(x):
    while len(FridayArabic) < x:
        a = random.choice(employeeNames)
        if a in fridayMorningLimits:
            pass
        elif a in fridayEveningLimits:
            pass
        elif a in ThursdayNight:
            pass
        elif a in FridayProtools:
            pass
        elif a in FridayMorning:
            pass
        elif a in FridayEvening:
            pass
        elif a in FridayArabic:
            pass
        else:
            FridayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", FridayArabic)


def friday_turner(x):
    while len(FridayTurner) < x:
        a = random.choice(employeeNames)
        if a in fridayMorningLimits:
            pass
        elif a in fridayEveningLimits:
            pass
        elif a in ThursdayNight:
            pass
        elif a in FridayProtools:
            pass
        elif a in FridayMorning:
            pass
        elif a in FridayEvening:
            pass
        elif a in FridayArabic:
            pass
        elif a in FridayTurner:
            pass
        else:
            FridayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", FridayTurner)


def friday_night(x):
    while len(FridayNight) < x:
        a = random.choice(employeeNames)
        if a in fridayNightLimits:
            pass
        elif a in FridayProtools:
            pass
        elif a in FridayMorning:
            pass
        elif a in FridayEvening:
            pass
        elif a in FridayTurner:
            pass
        elif a in FridayArabic:
            pass
        elif a in FridayNight:
            pass
        else:
            FridayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", FridayNight)


def saturday_morning(x):
    while len(SaturdayMorning) < x:
        a = random.choice(employeeNames)
        if a in saturdayMorningLimits:
            pass
        elif a in FridayNight:
            pass
        elif a in FridayEvening:
            pass
        elif a in SaturdayProtools:
            pass
        elif a in SaturdayMorning:
            pass
        else:
            SaturdayMorning.append(a)
            employeeNames.remove(a)
    print("Morning: ", SaturdayMorning)


def saturday_evening(x):
    while len(SaturdayEvening) < x:
        a = random.choice(employeeNames)
        if a in saturdayEveningLimits:
            pass
        elif a in FridayNight:
            pass
        elif a in SaturdayProtools:
            pass
        elif a in SaturdayMorning:
            pass
        elif a in SaturdayEvening:
            pass
        else:
            SaturdayEvening.append(a)
            employeeNames.remove(a)
    print("Evening: ", SaturdayEvening)


def saturday_arabic(x):
    while len(SaturdayArabic) < x:
        a = random.choice(employeeNames)
        if a in saturdayMorningLimits:
            pass
        elif a in saturdayEveningLimits:
            pass
        elif a in FridayNight:
            pass
        elif a in SaturdayProtools:
            pass
        elif a in SaturdayMorning:
            pass
        elif a in SaturdayEvening:
            pass
        elif a in SaturdayArabic:
            pass
        else:
            SaturdayArabic.append(a)
            employeeNames.remove(a)
    print("Arabic: ", SaturdayArabic)


def saturday_turner(x):
    while len(SaturdayTurner) < x:
        a = random.choice(employeeNames)
        if a in saturdayMorningLimits:
            pass
        elif a in saturdayEveningLimits:
            pass
        elif a in FridayNight:
            pass
        elif a in SaturdayProtools:
            pass
        elif a in SaturdayMorning:
            pass
        elif a in SaturdayEvening:
            pass
        elif a in SaturdayArabic:
            pass
        elif a in SaturdayTurner:
            pass
        else:
            SaturdayTurner.append(a)
            employeeNames.remove(a)
    print("Turner: ", SaturdayTurner)


def saturday_night(x):
    while len(SaturdayNight) < x:
        a = random.choice(employeeNames)
        if a in saturdayNightLimits:
            pass
        elif a in SaturdayProtools:
            pass
        elif a in SaturdayMorning:
            pass
        elif a in SaturdayEvening:
            pass
        elif a in SaturdayTurner:
            pass
        elif a in SaturdayArabic:
            pass
        elif a in SaturdayNight:
            pass
        else:
            SaturdayNight.append(a)
            employeeNames.remove(a)
    print("Night: ", SaturdayNight)


'''
def former():
    FormerWeek.append(input("input an emplyee name: \n"))
    FormerWeek.append(input("input another employee name: \n"))


former()
'''


def run():
    # print(employeeNames)
    print(len(employeeNames))
    print("Sunday")
    sunday_protools(0)
    sunday_morning(2)
    sunday_evening(2)
    sunday_arabic(1)
    sunday_turner(1)
    sunday_night(2)
    # print(employeeNames)
    print("\n")
    print("Monday")
    monday_protools(0)
    monday_morning(2)
    monday_evening(2)
    monday_arabic(1)
    monday_turner(1)
    monday_night(1)
    # print(employeeNames)
    print("\n")
    print("Tuesday")
    tuesday_protools(0)
    tuesday_morning(2)
    tuesday_evening(2)
    tuesday_arabic(1)
    tuesday_turner(1)
    tuesday_night(1)
    # print(employeeNames)
    print("\n")
    print("Wednesday")
    wednesday_protools(1)
    wednesday_morning(2)
    wednesday_evening(2)
    wednesday_arabic(1)
    wednesday_turner(1)
    wednesday_night(1)
    # print(employeeNames)
    print("\n")
    print("Thursday")
    thursday_protools(0)
    thursday_morning(2)
    thursday_evening(2)
    thursday_arabic(1)
    thursday_turner(1)
    thursday_night(1)
    # print(employeeNames)
    print("\n")
    print("Friday")
    friday_protools(0)
    friday_morning(2)
    friday_evening(2)
    friday_arabic(0)
    friday_turner(0)
    friday_night(1)
    # print(employeeNames)
    print("\n")
    print("Saturday")
    saturday_protools(0)
    saturday_morning(2)
    saturday_evening(2)
    saturday_arabic(0)
    saturday_turner(0)
    saturday_night(0)
    print("Remaining Employees", employeeNames)

    lenSunday = len(SundayMorning + SundayEvening + SundayNight + SundayArabic + SundayTurner + SundayProtools)
    lenMonday = len(MondayMorning + MondayEvening + MondayNight + MondayArabic + MondayTurner + MondayProtools)
    lenTuesday = len(TuesdayMorning + TuesdayEvening + TuesdayNight + TuesdayArabic + TuesdayTurner + TuesdayProtools)
    lenWednesday = len(WednesdayMorning + WednesdayEvening + WednesdayNight +
                       WednesdayArabic + WednesdayTurner + WednesdayProtools)
    lenThursday = len(ThursdayMorning + ThursdayEvening + ThursdayNight +
                      ThursdayArabic + ThursdayTurner + ThursdayProtools)
    lenFriday = len(FridayMorning + FridayEvening + FridayNight + FridayArabic + FridayTurner + FridayProtools)
    lenSaturday = len(SaturdayMorning + SaturdayEvening + SaturdayNight +
                      SaturdayArabic + SaturdayTurner + SaturdayProtools)

    print(lenSunday + lenMonday + lenTuesday + lenWednesday + lenThursday + lenFriday + lenSaturday)


run()
save = input("Do you wish to save the current work schedule as Sidoor.txt? \n")
if save in ("y", "Y"):
    file = open('Sidoor.txt', 'w')
    file.write(str(print(run())))
    file.close()
else:
    pass
