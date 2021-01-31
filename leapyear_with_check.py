"""
To run this program run python3 noah_pandey_hw1.py

enter the year when prompted

note: this program only runs once (no while loop) so if you want
to test multiple years you will have to run it multiple times.
In the event of an error (ValueError) the program will raise
an exception and then quit (this is intentional)


"""

#set initial condition and get input
leapyear = False
try:
  userin = int(input("Enter a year: "))

except ValueError:
  print("Input is not a number or is negative! ")
  quit()
  


#check conditions for leapyear = True or leapyear = False

if userin%4 == 0:
  leapyear = True

  if userin%100 == 0:
    leapyear = False

    if userin%400 == 0:
      leapyear = True

#print out results

if leapyear == True:
  print (userin, "is a leap year.")

else:
  print (userin, "is not a leap year.")
