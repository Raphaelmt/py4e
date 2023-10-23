def add_time(start, duration, weekday = ""):
    s_hours = int(start.split(':')[0])
    s_minutes = start.split(':')[1].split()[0]
    s_minutes = int(s_minutes.split()[0])
    s_am_pm = start.split(':')[1].split()[1]

    d_hours = int(duration.split(':')[0])
    d_minutes = int(duration.split(':')[1])
    
    new_minutes = s_minutes + d_minutes
    new_hours = s_hours + d_hours
    new_am_pm = s_am_pm

    if new_minutes > 59:
        new_minutes = new_minutes - 60
        new_hours = new_hours + 1

    days_passed = 0
    if new_hours > 24:
        days_passed = new_hours // 24
        new_hours = new_hours - days_passed * 24
    

    if new_hours >= 12:
        new_hours = new_hours - 12
        if new_am_pm == 'AM':
            new_am_pm = 'PM'
        else:
            new_am_pm = 'AM'
            days_passed = days_passed + 1
        if new_hours == 0: new_hours = 12
        
    
    new_minutes = str(new_minutes)
    new_hours = str(new_hours)
    if len(new_minutes) == 1:
        new_minutes = '0' + new_minutes

    new_time = new_hours + ':' + new_minutes + ' ' + new_am_pm

    if weekday != '':
        weekdays = {'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4,
        'thursday': 5, 'friday': 6, 'saturday': 7}
        weekday = weekday.lower()
        
        day_number = days_passed
        if weekdays[weekday] + days_passed > 7:
            while day_number > 14:
                day_number = day_number % 7
                day_number = weekdays[weekday] + day_number
            if day_number > 7: day_number = day_number - 7
        else:
            day_number = weekdays[weekday] + days_passed
        
        keys = list(weekdays.keys())
        values = list(weekdays.values())
        weekday = keys[values.index(day_number)]
        

        new_time = new_time + ', ' + weekday.capitalize()

    
    if days_passed == 1:
        new_time = new_time + ' (next day)'
    elif days_passed > 1:
        new_time = new_time + ' (' + str(days_passed) + ' days later)'

    return new_time

print(add_time("11:59 PM", "24:05"))
