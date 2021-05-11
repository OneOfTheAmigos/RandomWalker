import random

print("How many times do you want to run the simulation?")
numberoftrials = input()

totalamount = 0
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
    
    totalamount += trialnumber
    print("Number of tries: " + str(trialnumber))

avgamount = totalamount / int(numberoftrials)
print("The average number of tries was: " + str(avgamount))