import random

# Basic variable introduction and print.
HelloWorld = "Hello World!"
print(HelloWorld)

# Printing based on random number generator.
RanNum = random.randrange(0, 10)
if RanNum > 4:
    print("Wow! the number is greater than four.", RanNum)
else:
    print("The value is less four or less.", RanNum)

# Printing based on a random choice in a list and boolean operator.
random_list = ['Red', 'Yellow', 'Blue', 'Green']
color = random.choice(random_list)
like_or_not = random.getrandbits(1)

if like_or_not == 0:
    print("I love the color", color)
else:
    print("I hate the color", color)

# Calculate pace/mile based on time and type of race (random numbers used instead of user entry).
mile = random.getrandbits(1)  # 0 is KM, 1 is MI
time = random.randrange(300, 1440)  # Random rime in second from 5 minutes to 24 minutes
distance = random.randrange(1, 5)
pace = 0

if mile == 1: # If the user's race was ran in miles.
    pace = (time / distance) / 60
    time = time / 60
    pace = '%.2f' % (pace) # Truncates the pace and time so we are not left with a long string of numbers. The output is much more readable.
    time = '%.2f' % (time)
    print("Your pace for", distance, "MI in", time, "minutes is:", pace, "minutes per mile")
else: # If the users race was ran in kilometers.
    pace = (time / (distance * 0.621371)) / 60
    time = time / 60
    pace = '%.2f'%(pace)
    time = '%.2f' % (time)
    print("Your pace for", distance, "KM in", time, "minutes is:", pace, "minutes per mile")
