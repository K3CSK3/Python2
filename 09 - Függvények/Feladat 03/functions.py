import datetime

def kiiras(text:str, num:int) -> float:
    yearNow = (datetime.date.today()).year
    monthNow = (datetime.date.today()).month
    age = (yearNow - 1) + (monthNow - (num * 12))/12
    text = text.title()
    print(f"{text} ön idén {age} éves")