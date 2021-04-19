def add_time(start, duration, day_week = ""):
    days_week= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    start_min = to_minutes(start)
    duration_min = to_minutes(duration)
    total_min = start_min + duration_min
    days = int(total_min/1440)
    clock = start[-2:]
    new_time = to_hours(start_min, duration_min, total_min, clock, days)
    if day_week != "":
        day_week = day_week.capitalize()
        i = days_week.index(day_week)
        i = (i + days)%7
        day_week = ", " + days_week[i]
    if days < 1:
        return new_time + day_week
    elif days == 1:
        return new_time + day_week + " (next day)"
    else:
        return new_time + day_week + " (" + str(days) + " days later)"

def to_minutes(time):
    colon = time.find(":")
    h = int(time[:colon])
    m = int(time[colon+1:colon+3])
    if time[-2:] == "PM":
        h = h + 12
    return h * 60 + m

def to_hours(m1, m2, tot, clock, days):
    hr = int((tot - 1440*days)/60)
    min = int(tot%60)

    if hr == 0:
        hr = 12
        clock = "AM"
    elif hr < 12:
        clock = "AM"
    else:
        clock = "PM"
        hr = hr - 12
        if hr == 0:
            hr = 12
    
    min = str(min)
    if len(min) == 1:
        min = "0" + str(min)
    hr = str(hr)
    return hr+":"+min+" "+clock
