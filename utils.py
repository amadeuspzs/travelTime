import pandas as pd
# Return start of the week
def find_week_start(data):
    return find_day_start(data,1) # mondays

# Return start and end of week
def find_weeks(data):
    start = find_week_start(data)
    weeks = []
    for i in range(len(start)):
        if i < len(start)-1:
            weeks.append([start[i],start[i+1]-1])
        else:
            weeks.append([start[i],len(data)-1])
    return weeks

def find_day_start(data,day):
    days = []
    seek_day = True
    next_day = day + 1 if day < 6 else 0
    for index, row in data.iterrows():
        if seek_day is True and int(row.Timestamp.strftime("%w")) == day:
            days.append(index)
            seek_day = False
        elif seek_day is False and int(row.Timestamp.strftime("%w")) == next_day:
            seek_day = True
    return days

def find_days(data,day):
    days = []
    next_day = day + 1 if day < 6 else 0
    day_starts = find_day_start(data,day)
    # don't include next days that start before the first day
    # start next days search at beginning of data for first first day
    next_day_starts = find_day_start(data[day_starts[0]:],next_day)
    for i in range(len(day_starts)):
        days.append([day_starts[i], next_day_starts[i]-1 ])
    return days