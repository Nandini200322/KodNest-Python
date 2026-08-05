#Read marks, attendance and project completion status 1

marks = int(input())
attendence = int(input())
project = input()

#Check the academic requirements
if marks >= 60 and attendence >= 75:
  if project == "yes":
   print("Eligible")
  else :
   print("Not Eligible")
else:
 print("Not Eligible")