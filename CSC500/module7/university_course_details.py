

class Universiy_courses:
    course_room = {}
    course_instructor = {}
    course_meeting = {}
    course_names = set()
    def __init__(self):
        self.load_courses_data()

    def load_courses_data(self):
        self.course_room = {
            "CSC101" : 3004,
            "CSC102": 4501,
            "CSC103": 6755,
            "NET110": 1244,
            "COM241": 1411
        }
        self.course_names.update(self.course_room.keys())

        self.course_instructor = {
            "CSC101" : "Haynes",
            "CSC102": "Alvarado",
            "CSC103": "Rich",
            "NET110": "Burke",
            "COM241": "Lee"
        }

        self.course_names.update(self.course_instructor.keys())
        self.course_meeting = {
            "CSC101" : "8:00 a.m.",
            "CSC102": "9:00 a.m.",
            "CSC103": "10:00 a.m.",
            "NET110": "11:00 a.m.",
            "COM241": "1:00 p.m."
        }
        
        self.course_names.update(self.course_meeting.keys())


if __name__ == "__main__":
    university = Universiy_courses()
    
    university.load_courses_data()
    print("University course details are loaded")
    
    university_courses = " , ".join( e for e in university.course_names)
    print(f"Available Courses in the University: {university_courses}")
    
    while True:
        user_input = str(input("Enter the course name (eg: CSC101, CSC102 ..), else 'q' to quit: ")).strip()
        if user_input == "q":
            exit(1)
            
        course_names = (course.strip().upper() for course in user_input.split(","))
            
        for course_name in course_names:
            if (course_name not in university.course_names):
                print(f"\n{course_name} not available in the University")
            else:
                print(f"\ncourseName: {course_name}")
                print("----------------")
                print(f" RoomNumber: {university.course_room.get(course_name)}\n InstructorName: {university.course_instructor.get(course_name)}\n MeetingTime:{university.course_meeting.get(course_name)}")