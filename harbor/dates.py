from datetime import date, timedelta


def week_start(day):
    return day - timedelta(days=day.weekday())


def week_label(day):
    start = week_start(day)
    end = start + timedelta(days=6)
    return start.strftime("%b %d") + " to " + end.strftime("%b %d")


def parse_day(text):
    year, month, day = text.split("-")
    return date(int(year), int(month), int(day))
