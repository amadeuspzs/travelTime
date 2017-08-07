import pandas as pd
# Return start of the week
def return_week_start(data):
    if not isinstance(data,pd.DataFrame):
        return "Requires pandas dataframe"

    weeks = []
    seek_monday = True
    for index, row in data.iterrows():
        if seek_monday is True and row.Timestamp.strftime("%w") == '1':
            weeks.append(index)
            seek_monday = False
        elif seek_monday is False and row.Timestamp.strftime("%w") == '0':
            seek_monday = True
    return weeks

# Return start and end of week
def return_weeks(data):
    start = return_week_start(data)
    weeks = []
    for i in range(len(start)):
        if i < len(start)-1:
            weeks.append([start[i],start[i+1]-1])
        else:
            weeks.append([start[i],len(data)-1])
    return weeks