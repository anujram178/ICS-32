def getDayTillYear(year):
	return year*365


def getDayTillMonth(month):
    num = 0
    if month == 1:
        num += 0
    elif month == 2:
        num += 31
    elif month == 3:
        num += 59
    elif month == 4:
        num += 90
    elif month == 5:
        num += 120
    elif month == 6:
        num += 151
    elif month == 7:
        num += 181
    elif month == 8:
        num += 212
    elif month == 9:
        num += 243
    elif month == 10:
        num += 273
    elif month == 11:
        num += 304
    elif month == 12:
        num += 334
    return num

def getLeapTillYear(year):
	num = 0
	num += year//4
	num -= year//100
	num+= year//400
	return num

def isValid(month: int, day: int, year: int) -> bool:
    if month == 1:
        if 1<= day <= 31:
            return True
        else:
            return False
    elif month == 2:
        if type(year/4) == int or type(year/400) == int:
            if 1 <= day <= 29:
                return True
        elif 1 <= day <= 28:
            return True
        else:
            return False
    elif month == 3:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 4:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 5:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 6:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 7:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 8:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 9:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 10:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 11:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 12:
        if 1 <= day <= 31:
            return True
        else:
            return False
    else:
        return False

def isLeapYear(year: int) -> bool:
    if year%4 == 0 and year%100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def isValidMonth(month: int) -> bool:
    if 1<= month <= 12:
        return True
    else:
        return False

def getDayOfWeek(month: int, day: int, year:int) -> str:
    num = 0
    if isValid(month,day,year) == True:
        num += getDayTillYear(year) + getDayTillMonth(month) + getLeapTillYear(year) + day
        if num%7 == 0:
            return("Saturday")
        elif num%7 == 1:
            return("Sunday")
        elif num%7 == 2:
            return("Monday")
        elif num%7 == 3:
            return("Tuesday")
        elif num%7 == 4:
            return("Wednesday")
        elif num%7 == 5:
            return("Thursday")
        elif num%7 == 6:
            return("Friday")

def getThanksgivingDate(year:int) -> int:
    counter = 0
    month = 11
    for day in range(1,31):
        if getDayOfWeek(month,day,year) == "Thursday":
            counter += 1
            if counter == 4:
                return day
        

def getDayTillYear(year):
	return year*365


def getDayTillMonth(month):
    num = 0
    if month == 1:
        num += 0
    elif month == 2:
        num += 31
    elif month == 3:
        num += 59
    elif month == 4:
        num += 90
    elif month == 5:
        num += 120
    elif month == 6:
        num += 151
    elif month == 7:
        num += 181
    elif month == 8:
        num += 212
    elif month == 9:
        num += 243
    elif month == 10:
        num += 273
    elif month == 11:
        num += 304
    elif month == 12:
        num += 334
    return num

def getLeapTillYear(year):
	num = 0
	num += year//4
	num -= year//100
	num+= year//400
	return num



