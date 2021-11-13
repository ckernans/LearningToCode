# Today we focus on functions.
# Function to execute the pace converter, but cooler.
def mile_pace(a, b, c):
    import datetime
    """Returns the pace per mile based on time (in seconds), race distance, and type.
    a = time
    b = race distance
    c = race type (0 for miles, 1 for kilometers)
    """
    # First we want to convert the time string to seconds.
    # This will be helpful when we run the code on a dataset with time strings.

    date_time_output = datetime.datetime.strptime(a, "%H:%M:%S") # The output is 1900-01-01 H:M:S...
    a_timedelta = date_time_output - datetime.datetime(1900, 1, 1) # So, we have to remove the 1900-01-01...
    time_seconds = a_timedelta.total_seconds() # Then, we convert the H:M:S to total seconds.

    if c == 0:  # If the user's race was ran in miles.
        seconds_pace = (time_seconds / b)
        pace = str(datetime.timedelta(seconds=round(seconds_pace))) # We have to reconvert the seconds into a H:M:S string and round.
        print("Your pace for", b, "MI in", a, "minutes is:", pace, "minutes per mile.")
    elif c == 1:  # If the users race was ran in kilometers.
        seconds_pace = (time_seconds / (b * 0.621371))
        pace = str(datetime.timedelta(seconds=round(seconds_pace)))
        print("Your pace for", b, "KM in", a, "minutes is:", pace, "minutes per mile.")
    else:
        print('Please enter a valid integer (0 for miles, 1 for kilometers)')


print(mile_pace("00:23:40", 5, 1))
