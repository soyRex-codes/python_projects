#filter(function, collection)=return all elements that pass a condition
def is_passing(grade): #filter function
    return grade>=60

grades = [91, 23, 44, 75, 56, 90, 67, 88]

passing_grades=list(filter(is_passing, grades))

print(passing_grades)