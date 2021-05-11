import random

print("How many times do you want to run the simulation?")
numberoftrials = input()

for ii in range(int(numberoftrials)):
    trackingaverage = 0 
    additionnumber = 0
    trialnumber = 0

    while trackingaverage > -3:
        additionnumber = random.randint(1, 2)
        if additionnumber == 1:
            trackingaverage += 1
        elif additionnumber == 2:
            trackingaverage -= 1
        trialnumber += 1
        if trackingaverage == 3:
            break

    print("Number of tries: " + str(trialnumber))
