def daysToYears(d):
    y = d//365
    d = d%365
    m = d//30
    print(y,"years &",m,"months")
daysToYears(87653)