def format_duration(seconds):
    if seconds == 0:
        return "now"
    elif seconds < 60:
        return "{} seconds".format(seconds) if seconds > 1 else "{} second".format(seconds)
    else: 
        actualYears = seconds // 31536000
        actualDays = (seconds % 31536000) // 86400
        actualHours = ((seconds % 31536000) % 86400) // 3600
        actualMinutes = (((seconds % 31536000) % 86400) % 3600) // 60
        actualSeconds = (((seconds % 31536000) % 86400) % 3600) % 60
        ret = ""
        if actualYears != 0:
            if actualYears == 1:
                ret += "{} year".format(actualYears)
            else:
                ret += "{} years".format(actualYears)
        if actualDays != 0:
            if actualHours == 0 and actualMinutes == 0 and actualSeconds == 0 and actualYears != 0:
                ret += " and "
            elif actualYears != 0:
                ret += ", "
            
            if actualDays == 1:
                ret += "{} day".format(actualDays)
            else:
                ret += "{} days".format(actualDays)
        if actualHours != 0:
            if actualMinutes == 0 and actualSeconds == 0 and actualDays != 0 and actualYears != 0:
                ret += " and "
            elif actualDays != 0 or actualYears != 0:
                ret += ", "
            
            if actualHours == 1:
                ret += "{} hour".format(actualHours)
            else:
                ret += "{} hours".format(actualHours)
        if actualMinutes != 0:
            if actualSeconds == 0 and (actualHours != 0 or actualDays != 0 or actualYears != 0):
                ret += " and "
            elif actualHours != 0 or actualDays != 0 or actualYears != 0:
                ret += ", "
            
            if actualMinutes == 1:
                ret += "{} minute".format(actualMinutes)
            else:
                ret += "{} minutes".format(actualMinutes)
        if actualSeconds != 0:
            ret += " and "
            if actualSeconds == 1:
                ret += "{} second".format(actualSecond as)
            else:
                ret += "{} seconds".format(actualSeconds)
        return ret
            
            
                
# Some test cases         
# assert_equals(format_duration(1), "1 second")
# assert_equals(format_duration(62), "1 minute and 2 seconds")
# assert_equals(format_duration(120), "2 minutes")
# assert_equals(format_duration(3600), "1 hour")
# assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")