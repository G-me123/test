student_list= []
stdent_dict= {}

student_name= input("Enter your name").capitalize
student_age= input("Enter your age")
student_grade= input("What grade are you studying") 
print(" Student information added successfully")

dict_item([('student_name', { "age:", student_age and "grade:", student_grade})])

name=input("Enter the name of the student you wanted to search:\n").capitalize
if name == student_name:
    print(dict_item)

else:
    print("Not been found")

a=input("Enter the name yo wanted to remove").capitalize
if remove_name in student_list:
    student_list.remove(remove_name)
    del books_dict[remove_name]
    print("name removed successfully!")

else:
    print("name not founed")
