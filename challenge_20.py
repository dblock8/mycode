# create wordbank list
wordbank= ["indentation", "spaces"] 

# create student list
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


# add integer 4 to the wordbank
wordbank.append(4)


# prompt user for number 0-20 be sure convert to int
num = input("Pick a number")

num = int(input=("Pick a number"))

# Use number from user to slice list
choice= int(input("Pick a student number!"))
student_name= tlgstudents[choice]


# print output
print(f'{student_name} always uses, {wordbank[1]} {wordbank[2]}, to indent.')


