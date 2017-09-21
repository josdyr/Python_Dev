COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}
def covers(set_of_topics):
    list_of_courses = []
    for key, value in COURSES.items():
        if value & set_of_topics:
            list_of_courses.append(course)
    return list_of_courses

def covers_all(single_set):
    new_list = []
    for key, value in COURSES.items():
        if (single_set & value)==single_set:
            new_list.append(key)
    return new_list
