def process_results(name):
    avg = (time1+time2+time3+time4+time5)/5
    var = (time1-avg)**2 + (time2-avg)**2 + (time3-avg)**2 + (time4-avg)**2 + (time5-avg)**2
    var /= 5
    skew = (time1-avg)**3 + (time2-avg)**3 + (time3-avg)**3 + (time4-avg)**3 + (time5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew

name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles

time1 = 34
time2 = 34
time3 = 35
time4 = 31
time5 = 29

print ("{0}'s running times have a skew of {1:.2f}".format(name_1, process_results(name_1)))

name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles

time1 = 30
time2 = 31
time3 = 29
time4 = 29
time5 = 28

print ("{0}'s running times have a skew of {1:.2f}".format(name_2, process_results(name_2)))

name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time1 = 36
time2 = 31
time3 = 32
time4 = 33
time5 = 33

print ("{0}'s running times have a skew of {1:.2f}".format(name_3, process_results(name_3)))

name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time1 = 33
time2 = 32
time3 = 34
time4 = 31
time5 = 35

print ("{0}'s running times have a skew of {1:.2f}".format(name_4, process_results(name_4)))

name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time1 = 27
time2 = 29
time3 = 29
time4 = 28
time5 = 30

print ("{0}'s running times have a skew of {1:.2f}".format(name_5, process_results(name_5)))


'''
# Process results for the first person
avg = (time1_1+time2_1+time3_1+time4_1+time5_1)/5
var = (time1_1-avg)**2 + (time2_1-avg)**2 + (time3_1-avg)**2 + (time4_1-avg)**2 + (time5_1-avg)**2
var /= 5
skew = (time1_1-avg)**3 + (time2_1-avg)**3 + (time3_1-avg)**3 + (time4_1-avg)**3 + (time5_1-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew))


## Process for the second person
avg = (time1_2+time2_2+time3_2+time4_2+time5_2)/5
var = (time1_2-avg)**2 + (time2_2-avg)**2 + (time3_2-avg)**2 + (time4_2-avg)**2 + (time5_2-avg)**2
var /= 5
skew = (time1_2-avg)**3 + (time2_2-avg)**3 + (time3_2-avg)**3 + (time4_2-avg)**3 + (time5_2-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew))

## Process for the third person
avg = (time1_3+time2_3+time3_3+time4_3+time5_3)/5
var = (time1_3-avg)**2 + (time2_3-avg)**2 + (time3_3-avg)**2 + (time4_3-avg)**2 + (time5_3-avg)**2
var /= 5
skew = (time1_3-avg)**3 + (time2_3-avg)**3 + (time3_3-avg)**3 + (time4_3-avg)**3 + (time5_3-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew))


## Process for the fourth person
avg = (time1_4+time2_4+time3_4+time4_4+time5_4)/5
var = (time1_4-avg)**2 + (time2_4-avg)**2 + (time3_4-avg)**2 + (time4_4-avg)**2 + (time5_4-avg)**2
var /= 5
skew = (time1_4-avg)**3 + (time2_4-avg)**3 + (time3_4-avg)**3 + (time4_4-avg)**3 + (time5_4-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew))


## Process for the fifth person
avg = (time1_5+time2_5+time3_5+time4_5+time5_5)/5
var = (time1_5-avg)**2 + (time2_5-avg)**2 + (time3_5-avg)**2 + (time4_5-avg)**2 + (time5_5-avg)**2
var /= 5
skew = (time1_5-avg)**3 + (time2_5-avg)**3 + (time3_5-avg)**3 + (time4_5-avg)**3 + (time5_5-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew))
'''
