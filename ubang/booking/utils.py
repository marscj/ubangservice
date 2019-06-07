from datetime import date, datetime, timedelta

def get_days(start, end):
    duration = date(end.year, end.month, end.day) + timedelta(days=1) - date(start.year, start.month, start.day)
    return [date(start.year, start.month, start.day) + timedelta(days=index) for index in range(duration.days) ]
