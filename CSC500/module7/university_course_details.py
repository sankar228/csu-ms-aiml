

class Universiy_Cources:
    cource_room = {}
    cource_instructor = {}
    cource_meeting = {}
    cource_names = set()
    def __init__(self):
        self.load_cources_data()

    def load_cources_data(self):
        self.cource_room = {
            "CSC101" : 3004,
            "CSC102": 4501,
            "CSC103": 6755,
            "NET110": 1244,
            "COM241": 1411
        }
        self.cource_names.update(self.cource_room.keys())

        self.cource_instructor = {
            "CSC101" : "Haynes",
            "CSC102": "Alvarado",
            "CSC103": "Rich",
            "NET110": "Burke",
            "COM241": "Lee"
        }

        self.cource_names.update(self.cource_instructor.keys())
        self.cource_meeting = {
            "CSC101" : "8:00 a.m.",
            "CSC102": "9:00 a.m.",
            "CSC103": "10:00 a.m.",
            "NET110": "11:00 a.m.",
            "COM241": "1:00 p.m."
        }
        
        self.cource_names.update(self.cource_meeting.keys())


if __name__ == "__main__":
    university = Universiy_Cources()
    
    university.load_cources_data()
    print("University cource details are loaded")
    
    university_cources = " , ".join( e for e in university.cource_names)
    print(f"Available Courses in the University: {university_cources}")
    
    while True:
        user_input = str(input("Enter the cource name (eg: CSC101, CSC102 ..), else 'q' to quit: ")).strip()
        if user_input == "q":
            exit(1)
            
        cource_names = (cource.strip() for cource in user_input.split(","))
            
        for cource_name in cource_names:
            if (cource_name not in university.cource_names):
                print(f"{cource_name} not available in the University")
            else:
                print(f"\nCourceNamea: {cource_name}")
                print("----------------")
                print(f" RoomNumber: {university.cource_room.get(cource_name)}\n InstructorName: {university.cource_instructor.get(cource_name)}\n MeetinTime:{university.cource_meeting.get(cource_name)}")