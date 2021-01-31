"""
To run this program run python2.7 noah_pandey_hw1.py

enter the year when prompted

note: this program only runs once (no while loop) so if you want
to test multiple years you will have to run it multiple times.


"""

#set initial condition and get input
leapyear = False

userin = int(input("Enter a year: "))

#check conditions for leapyear = True or leapyear = False

if userin%4 == 0:
  leapyear = True

  if userin%100 == 0:
    leapyear = False

    if userin%400 == 0:
      leapyear = True

#print out results

if leapyear == True:
  print userin, "is a leap year."

else:
  print userin, "is not a leap year."



