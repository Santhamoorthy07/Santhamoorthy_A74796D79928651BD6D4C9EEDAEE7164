class Student:
  def __init__(self,name,rollno,cgpa):
    self.name=name
    self.rollno=rollno
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students

students=[
  Student("Ragulan","A123",7.8),
  Student("Deepak","A124",8.9),
  Student("Mani","A125",9.1),
  Student("Vignesh","A126",9.9)
]

sorted_students=sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll No: {}, CGPA: {}".format(student.name,student.rollno,student.cgpa))