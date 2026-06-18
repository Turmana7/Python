courses = {
    "Python": ["ანი", "ლუკა", "გიორგი"],
    "C++": ["მარი", "ნიკა"],
    "Java": ["დათო", "ალექსი", "ლაშა", "თამუნა"]
}

pop_subject = ""
max_students = 0

for subject, students in courses.items():
    if len(students) > max_students:
        max_students = len(students)
        pop_subject = subject

print(f"ყველაზე პოპულარული საგანია {pop_subject} ({max_students} სტუდენტი).")