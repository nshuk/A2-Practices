# heres an input of student details of three guys with their test scores, class, course on a dictionary
# mind the use of curly and straight brackets
studentDetails = {"Amin":[78,"Class 4", "Engineering"], "Naqib":[67, "Class 4", "Engineering"], "Ghazali":[89, "Class 4", "ProSc"]}
print(studentDetails)

# lets display a student's data as a whole
wholeDetails = studentDetails["Amin"]
print(wholeDetails)

# now im displaying amin's data on specific aspects only
scoreDetails = studentDetails["Amin"][0] # 0 means index 0 which refers to test score only
print(scoreDetails)

classDetails = studentDetails["Amin"][1] # index 1 refers to their class only
print(classDetails)

# now i want to change naqib's class to class 8
studentDetails["Naqib"][1] = "Class 8"
print(studentDetails)

# now i want to delete jali's whole details from the dictionary
del studentDetails["Ghazali"]
print(studentDetails)
