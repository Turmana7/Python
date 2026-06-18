data = {"cs": {1: {"python": []}}}

def add_subject(faculty, course, subject):
    if faculty not in data:
        data[faculty] = {}
    if course not in data[faculty]:
        data[faculty][course] = {}
    if subject not in data[faculty][course]:
        data[faculty][course][subject] = []

add_subject("cs", 1, "java")
add_subject("math", 1, "calculus")
print(data)