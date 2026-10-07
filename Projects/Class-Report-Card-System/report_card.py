   student = int(input("Enter number of students: "))
   total = 0
   passed = 0 
   failed = 0
   for i in range(student):
       name = input("Enter student name: ")
       vowels = 0
       for letter in name:
           if letter in "AEIOUaeiou":
               vowels += 1
       marks = float(input("Enter student marks: "))
       if i == 0:
           highest = marks
           lowest = marks
       else:
           if marks > highest:
               highest = marks
           if marks < lowest:
               lowest = marks    
       total += marks
       if marks >= 50:
           if marks >= 90:
               grade = "A+"
           elif marks >= 80:
               grade = "A"
           elif marks >= 70:
               grade = "B"
           elif marks >= 50:
               grade = "C"
           passed += 1
       else:
           grade = "FAIL"
           failed += 1
       print("Welcome",name)
       print("Your marks are:",marks)
       print("Grade:",grade)
       print("Number of vowels:",vowels)
   print("Total Marks:",total)
   print("Average Marks:",total/student)
   print("Passed Students:",passed)
   print("Failed Students:",failed)
