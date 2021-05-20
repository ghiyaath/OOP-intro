from datetime import date

def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


print(calculate_age(date(2000, 12, 23)))
